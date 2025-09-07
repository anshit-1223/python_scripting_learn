#!/bin/python3
import shutil
total,used,free = shutil.disk_usage("/")

def convert_bytes(bytes):
    return round(bytes / (2**30),2)

print("📦 Disk Usage for '/'")
print(f"Total: {convert_bytes(total)} GB")
print(f"Used:  {convert_bytes(used)} GB")
print(f"Free:  {convert_bytes(free)} GB")