#!/bin/python3
import subprocess
package="php"
result = subprocess.run(["dpkg","-l",package], capture_output=True, text=True)

if package in result.stdout:
    print(f"{package} is installed")
else:
    print(f"{package} is not installed")
