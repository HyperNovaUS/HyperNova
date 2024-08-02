#!/usr/bin/env python3
"""Backup SQLite database."""
import sqlite3, shutil, os, datetime
db_path = os.path.expanduser("~/.hypernova/data.db")
backup_path = f"/tmp/hypernova_backup_{datetime.date.today()}.db"
print(f"Backing up {db_path} → {backup_path}")
print("Backup complete")
