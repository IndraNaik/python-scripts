#!/usr/bin/env python3

import subprocess

SERVER = "google.com"
PING_COUNT = "4"

print(f"Pinging {SERVER}...")

try:
    subprocess.run(["ping", "-c", PING_COUNT, SERVER], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"{SERVER} is reachable.")
except subprocess.CalledProcessError:
    print(f"Failed to reach {SERVER}.")

===========================================================================================================================

#!/usr/bin/env python3

import socket

HOST = "localhost"
START_PORT = 1
END_PORT = 1024

print(f"Scanning open ports on {HOST} from {START_PORT} to {END_PORT}...")

for port in range(START_PORT, END_PORT + 1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)  # Optional: reduce for faster scan
        result = sock.connect_ex((HOST, port))
        if result == 0:
            print(f"Port {port} is open")
