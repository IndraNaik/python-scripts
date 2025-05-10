#!/usr/bin/env python3

import os
import tarfile
import boto3
from datetime import datetime

# Configuration
source_dir = "/path/to/source"
backup_dir = "/path/to/backup"
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
backup_filename = f"backup_{timestamp}.tar.gz"
backup_path = os.path.join(backup_dir, backup_filename)
s3_bucket = "your-s3-bucket-name"

def create_backup():
    os.makedirs(backup_dir, exist_ok=True)
    with tarfile.open(backup_path, "w:gz") as tar:
        tar.add(source_dir, arcname=".")
    print(f"Backup created at {backup_path}")

def upload_to_s3():
    s3 = boto3.client("s3")
    s3.upload_file(backup_path, s3_bucket, backup_filename)
    print(f"Backup uploaded to S3: s3://{s3_bucket}/{backup_filename}")

def cleanup():
    os.remove(backup_path)
    print(f"Local backup file removed: {backup_path}")

if __name__ == "__main__":
    create_backup()
    upload_to_s3()
    cleanup()
