import os
import sqlite3
from pathlib import Path

DB_PATH = Path("output/website_with_categories.db")


def init_db():
    os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
CREATE TABLE websites (
    url TEXT PRIMARY KEY,
    category TEXT
)
"""
    )


def save_result(url: str, category: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
INSERT OR REPLACE INTO websites (url, category)
VALUES (?, ?)
""",
        (url, category),
    )
    conn.commit()
    conn.close()
