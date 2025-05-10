#!/usr/bin/env python3

import subprocess

def update_and_upgrade():
    print("This is updating package")

    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        print("System updated successfully")

        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        print("System upgraded successfully")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_and_upgrade()
