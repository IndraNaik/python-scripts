#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

# Directories
source_dir = "/home/ubuntu/scripts"
destination_dir = "/home/ubuntu/backups"

def create_backup():
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # Construct backup zip file path
    backup_filename = f"backup_{timestamp}.zip"
    backup_path = os.path.join(destination_dir, backup_filename)

    # Create zip archive
    shutil.make_archive(backup_path.replace(".zip", ""), 'zip', source_dir)

    print("Backup completed successfully")

if __name__ == "__main__":
    create_backup()
