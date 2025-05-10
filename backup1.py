#!/usr/bin/env python3

import os
import shutil
import smtplib
import socket
from datetime import datetime
from email.message import EmailMessage

# Configuration
source_dir = "/home/ubuntu/scripts"
destination_dir = "/home/ubuntu/backups"
log_file = "/var/log/backups.log"
admin_email = "example@abc.com"

def log_message(message):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

def send_email_notification(subject, message):
    try:
        email = EmailMessage()
        email.set_content(message)
        email["Subject"] = subject
        email["From"] = f"noreply@{socket.gethostname()}"
        email["To"] = admin_email

        # Change or configure the SMTP server as needed
        with smtplib.SMTP("localhost") as smtp:
            smtp.send_message(email)
    except Exception as e:
        log_message(f"Failed to send email: {e}")

def create_backup():
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    backup_filename = f"backup_{timestamp}.zip"
    backup_path = os.path.join(destination_dir, backup_filename)

    try:
        os.makedirs(destination_dir, exist_ok=True)
        shutil.make_archive(backup_path.replace(".zip", ""), 'zip', source_dir)
        log_message(f"Backup successful: {backup_path}")
    except Exception as e:
        error_msg = f"Backup failed: {e}"
        log_message(error_msg)
        send_email_notification("Backup Failed!", f"Backup process failed on {socket.gethostname()} at {datetime.now()}.\nError: {e}\nCheck logs at {log_file}.")

if __name__ == "__main__":
    create_backup()
