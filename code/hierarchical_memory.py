"""Structured STM/LTM/WM storage using SQLite from the Python standard library."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class HierarchicalMemory:
    def __init__(self, database: str | Path):
        self.database = str(database)
        self.connection = sqlite3.connect(self.database)
        self.connection.execute("""CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            layer TEXT NOT NULL CHECK(layer IN ('STM', 'LTM')),
            record_key TEXT NOT NULL,
            config_object TEXT,
            payload TEXT NOT NULL,
            validated INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL
        )""")
        self.connection.execute("CREATE INDEX IF NOT EXISTS idx_memory_lookup ON memory(layer, config_object, validated)")
        self.connection.commit()

    def put(self, layer: str, record_key: str, payload: dict[str, Any], *, config_object: str = "", validated: bool = False) -> None:
        if layer not in {"STM", "LTM"}:
            raise ValueError("layer must be STM or LTM")
        if layer == "LTM" and not validated:
            raise ValueError("only validated records may enter LTM")
        self.connection.execute(
            "INSERT INTO memory(layer, record_key, config_object, payload, validated, created_at) VALUES (?, ?, ?, ?, ?, ?)",
            (layer, record_key, config_object, json.dumps(payload, ensure_ascii=False), int(validated), datetime.now(timezone.utc).isoformat()),
        )
        self.connection.commit()

    def recent_stm(self, limit: int = 20) -> list[dict[str, Any]]:
        rows = self.connection.execute("SELECT record_key, payload FROM memory WHERE layer='STM' ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
        return [{"record_key": key, **json.loads(payload)} for key, payload in reversed(rows)]

    def retrieve_ltm(self, config_object: str = "", limit: int = 20) -> list[dict[str, Any]]:
        rows = self.connection.execute(
            "SELECT record_key, payload FROM memory WHERE layer='LTM' AND (config_object='' OR config_object=?) ORDER BY id DESC LIMIT ?",
            (config_object, limit),
        ).fetchall()
        return [{"record_key": key, **json.loads(payload)} for key, payload in rows]

    def working_memory(self, config_object: str = "", *, stm_limit: int = 20, ltm_limit: int = 20) -> dict[str, Any]:
        return {"STM": self.recent_stm(stm_limit), "LTM": self.retrieve_ltm(config_object, ltm_limit)}

    def close(self) -> None:
        self.connection.close()
