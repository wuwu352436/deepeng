#!/usr/bin/env python3
"""Simple HTTP server for DeepEng web frontend.
Serves proper MIME types for .wav and .mp3 audio files.
Works on both Windows and WSL/Linux."""
import http.server
import os
import sys
import socket
import mimetypes

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
DIR = os.path.dirname(os.path.abspath(__file__))

# Ensure correct MIME types for audio
mimetypes.add_type('audio/wav', '.wav')
mimetypes.add_type('audio/mpeg', '.mp3')

os.chdir(DIR)

class DeepEngHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        base, ext = os.path.splitext(path)
        if ext == '.wav':
            return 'audio/wav'
        if ext == '.mp3':
            return 'audio/mpeg'
        return super().guess_type(path)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"DeepEng HTTP server")
print(f"  Local:   http://localhost:{PORT}")
print(f"  Network: http://{local_ip}:{PORT}")
print(f"  Dir:     {DIR}")
print(f"Ctrl+C to stop")
httpd = http.server.HTTPServer(("0.0.0.0", PORT), DeepEngHandler)
httpd.serve_forever()
