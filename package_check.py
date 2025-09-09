#!/bin/python3
import subprocess
package=input("Enter Package Name :").lower()
result = subprocess.run(["dpkg","-l",package], capture_output=True, text=True)

if package in result.stdout:
1    print(f"{package} is installed")
else:
    print(f"{package} is not installed")
