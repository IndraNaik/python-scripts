#!/usr/bin/env python3

import subprocess
import getpass

print("============== CREATE USERS ===============")

# Get username and password securely
username = input("Enter the username: ")
password = getpass.getpass("Enter the password: ")

try:
    # Create the user with a home directory
    subprocess.run(["sudo", "useradd", "-m", username], check=True)
    
    # Set the user's password
    subprocess.run(
        ["sudo", "chpasswd"],
        input=f"{username}:{password}".encode(),
        check=True
    )

    print("============== USER CREATED ===============")

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
