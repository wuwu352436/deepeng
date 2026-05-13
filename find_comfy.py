"""Find and launch ComfyUI from WSL"""
import subprocess
import os

# Find the ComfyUI installation
r = subprocess.run(["find", "/mnt/d/", "-maxdepth", "5", "-name", "main.py", "-path", "*ComfyUI*"], 
                   capture_output=True, text=True, timeout=30)
print("=== ComfyUI main.py locations ===")
print(r.stdout)
print(r.stderr[:200] if r.stderr else "")

# Also search for the aki bundle
r2 = subprocess.run(["find", "/mnt/d/", "-maxdepth", "4", "-iname", "*ComfyUI*aki*", "-type", "d"],
                   capture_output=True, text=True, timeout=30)
print("\n=== Aki bundle directories ===")
print(r2.stdout)
