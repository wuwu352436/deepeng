#!/usr/bin/env python3
"""Simple HTTP tunnel using a public relay service."""
import http.server
import socketserver
import urllib.request
import threading
import json
import sys
import time

PORT = 8081
WORKDIR = "/mnt/d/hermes/deepeng/web"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WORKDIR, **kwargs)
    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]} {args[1]} {args[2]}")

# Start HTTP server
httpd = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
thread = threading.Thread(target=httpd.serve_forever, daemon=True)
thread.start()
print(f"✅ HTTP server running on http://0.0.0.0:{PORT}")
print(f"   Local WSL: http://172.23.12.184:{PORT}")

# Try to get public URL via different tunnel services
def try_tunnel():
    services = [
        ("https://boringssl.com/tunnel", None),  # placeholder
    ]
    print(f"\n📱 Phone access:")
    print(f"   If phone is on same WiFi  → http://192.168.2.177:{PORT}")
    print(f"   If not, need internet tunnel")
    print(f"\n   Trying pyngrok...")
    try:
        from pyngrok import ngrok
        tunnel = ngrok.connect(PORT, bind_tls=True)
        print(f"   ✅ ngrok URL: {tunnel.public_url}")
        return
    except Exception as e:
        print(f"   ❌ pyngrok failed: {e}")

try_tunnel()

print(f"\n💡 Keep this terminal open. Press Ctrl+C to stop.")
while True:
    time.sleep(1)
