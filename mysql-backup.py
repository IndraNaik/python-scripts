#!/usr/bin/env python3

import os
import subprocess
import gzip
import shutil
from datetime import datetime, timedelta

# Configuration
DB_USER = "db_user"
DB_PASS = "db_password"
DB_NAME = "database_name"
BACKUP_DIR = "/path/to/backup"
TIMESTAMP = datetime.now().strftime("%Y%m%d%H%M%S")
BACKUP_NAME = f"db_backup_{TIMESTAMP}.sql"
BACKUP_PATH = os.path.join(BACKUP_DIR, BACKUP_NAME)
GZ_BACKUP_PATH = BACKUP_PATH + ".gz"

def create_backup_directory():
    os.makedirs(BACKUP_DIR, exist_ok=True)

def dump_database():
    with open(BACKUP_PATH, "w") as f:
        subprocess.run(
            ["mysqldump", "-u", DB_USER, f"-p{DB_PASS}", DB_NAME],
            stdout=f,
            check=True
        )

def compress_backup():
    with open(BACKUP_PATH, 'rb') as f_in, gzip.open(GZ_BACKUP_PATH, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    os.remove(BACKUP_PATH)

def cleanup_old_backups():
    now = datetime.now()
    for file in os.listdir(BACKUP_DIR):
        if file.startswith("db_backup_") and file.endswith(".sql.gz"):
            full_path = os.path.join(BACKUP_DIR, file)
            file_mtime = datetime.fromtimestamp(os.path.getmtime(full_path))
            if now - file_mtime > timedelta(days=7):
                os.remove(full_path)

def main():
    create_backup_directory()
    dump_database()
    compress_backup()
    cleanup_old_backups()
    print(f"Database backup completed: {GZ_BACKUP_PATH}")

if __name__ == "__main__":
    main()
