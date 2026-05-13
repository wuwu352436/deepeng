"""Check network connectivity from WSL to Windows"""
import socket

host = "172.23.0.1"

# Test common ports
for port_name, port in [("HTTP", 80), ("ComfyUI", 8188), ("RDP", 3389), ("SMB", 445)]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((host, port))
        print(f"{port_name} ({port}): CONNECTED")
        s.close()
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        print(f"{port_name} ({port}): {type(e).__name__}")

# Check WSL IP
import subprocess
r = subprocess.run(["ip", "addr", "show", "eth0"], capture_output=True, text=True)
print(f"\nWSL IP info:\n{r.stdout[:200]}")

# Test ping to gateway
r2 = subprocess.run(["ping", "-c", "1", "-W", "2", host], capture_output=True, text=True)
print(f"\nPing result: {r2.stdout[:100]}")

# Check if there's a different gateway
r3 = subprocess.run(["ip", "route"], capture_output=True, text=True)
print(f"\nRoutes:\n{r3.stdout}")
