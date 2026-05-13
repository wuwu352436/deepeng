"""Check ComfyUI health and available models via REST API"""
import urllib.request
import json
import sys

try:
    # Check system stats
    req = urllib.request.Request("http://172.23.0.1:8188/system_stats")
    resp = urllib.request.urlopen(req, timeout=10)
    data = json.loads(resp.read())
    print("=== ComfyUI System Stats ===")
    print(f"System: {json.dumps(data.get('system', {}), indent=2)}")
    print(f"Devices: {json.dumps(data.get('devices', {}), indent=2)}")

    # Check queue
    req2 = urllib.request.Request("http://172.23.0.1:8188/queue")
    resp2 = urllib.request.urlopen(req2, timeout=5)
    print(f"\nQueue: {resp2.read().decode()}")

    # Check available checkpoints via object_info
    req3 = urllib.request.Request("http://172.23.0.1:8188/object_info/CheckpointLoaderSimple")
    resp3 = urllib.request.urlopen(req3, timeout=5)
    info = json.loads(resp3.read())
    ckpts = info.get("CheckpointLoaderSimple", {}).get("input", {}).get("required", {}).get("ckpt_name", [[]])[0]
    print(f"\n=== Available Checkpoints (first 20) ===")
    for c in ckpts[:20]:
        print(f"  {c}")

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
