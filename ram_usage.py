#!/bin/python
import psutil

def bytes_to_gb(bytes_value):
    return round(bytes_value / (2**30), 2)

mem = psutil.virtual_memory()

print("🖥️ RAM Usage:")
print(f"Total RAM:     {bytes_to_gb(mem.total)} GB")
print(f"Used RAM:      {bytes_to_gb(mem.used)} GB")
print(f"Free RAM:      {bytes_to_gb(mem.free)} GB")
print(f"Available RAM: {bytes_to_gb(mem.available)} GB")
print(f"RAM Usage:     {mem.percent}%")
