#!/usr/bin/env python3
"""Simple HTTP server for DeepEng web frontend.
Works on both Windows and WSL/Linux."""
import http.server
import os
import sys
import socket

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIR)
handler = http.server.SimpleHTTPRequestHandler

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"DeepEng HTTP server")
print(f"  Local:   http://localhost:{PORT}")
print(f"  Network: http://{local_ip}:{PORT}")
print(f"  Dir:     {DIR}")
print(f"Ctrl+C to stop")
httpd = http.server.HTTPServer(("0.0.0.0", PORT), handler)
httpd.serve_forever()
