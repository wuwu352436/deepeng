"""Test ComfyUI connectivity using socket-level approach"""
import socket
import urllib.request
import json
import sys
import time

host = "172.23.0.1"
port = 8188

# First try socket connect
print(f"Testing socket connect to {host}:{port}...")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((host, port))
    print("Socket connect: OK")
    s.close()
except Exception as e:
    print(f"Socket connect FAILED: {e}")

# Try urllib with longer timeout
print(f"\nTrying HTTP GET /system_stats...")
try:
    req = urllib.request.Request(f"http://{host}:{port}/system_stats")
    resp = urllib.request.urlopen(req, timeout=10)
    data = json.loads(resp.read())
    print(f"HTTP OK! System: {json.dumps(data.get('system',{}), indent=2)[:300]}")
except Exception as e:
    print(f"HTTP failed: {e}")

# Try wget
print(f"\nTrying wget...")
import subprocess
try:
    r = subprocess.run(["wget", "-q", "-O", "-", f"http://{host}:{port}/system_stats"], 
                       capture_output=True, text=True, timeout=10)
    if r.returncode == 0:
        data = json.loads(r.stdout)
        print(f"wget OK! {json.dumps(data, indent=2)[:500]}")
    else:
        print(f"wget failed: {r.stderr[:200]}")
except Exception as e:
    print(f"wget error: {e}")

# Try curl with -m flag
print(f"\nTrying curl...")
try:
    r = subprocess.run(["curl", "-s", "-m", "10", f"http://{host}:{port}/system_stats"],
                       capture_output=True, text=True, timeout=15)
    if r.returncode == 0 and r.stdout:
        data = json.loads(r.stdout)
        print(f"curl OK! system: {data.get('system',{}).get('name','')}")
    else:
        print(f"curl failed: rc={r.returncode}, stderr={r.stderr[:200]}")
except Exception as e:
    print(f"curl error: {e}")
