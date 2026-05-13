"""Minimal connectivity test"""
import socket
import sys

host = "172.23.0.1"
port = 8188

print(f"Attempting socket connect to {host}:{port}...")
sys.stdout.flush()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
try:
    s.connect((host, port))
    print("CONNECTED! Sending HTTP request...")
    sys.stdout.flush()
    s.sendall(b"GET /system_stats HTTP/1.0\r\nHost: localhost\r\n\r\n")
    data = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk
        if len(data) > 10000:
            break
    print(f"Received {len(data)} bytes")
    print(data.decode('utf-8', errors='replace')[:2000])
except socket.timeout:
    print("TIMEOUT: Could not connect within 5 seconds")
except ConnectionRefusedError:
    print("REFUSED: Connection refused - ComfyUI may not be running")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
finally:
    s.close()
