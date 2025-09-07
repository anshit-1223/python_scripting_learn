#!/bin/python3
import subprocess
service="apache2"
status = subprocess.run(["systemctl","is-active",service], capture_output=True, text=True)
if status.stdout.strip()=="active":
    print(f"{service} is running ✅")
else:
    print(f"{service} is not running ❌")
    