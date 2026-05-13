"""Wait for ComfyUI to be ready and test connection"""
import urllib.request
import json
import time
import sys

host = "http://172.23.0.1:8188"

for attempt in range(1, 15):
    try:
        req = urllib.request.Request(f"{host}/system_stats")
        resp = urllib.request.urlopen(req, timeout=5)
        data = json.loads(resp.read())
        print(f"Attempt {attempt}: READY!")
        print(f"System: {data.get('system', {}).get('name', 'unknown')}")
        print(f"Devices: {json.dumps(data.get('devices', {}), indent=2)[:200]}")
        
        # Check available models
        try:
            req2 = urllib.request.Request(f"{host}/object_info/CheckpointLoaderSimple")
            resp2 = urllib.request.urlopen(req2, timeout=5)
            info = json.loads(resp2.read())
            ckpts = info.get("CheckpointLoaderSimple", {}).get("input", {}).get("required", {}).get("ckpt_name", [[]])[0]
            print(f"\nAvailable checkpoints ({len(ckpts)} total):")
            for c in ckpts[:30]:
                print(f"  {c}")
        except Exception as e:
            print(f"Checkpoint query error: {e}")
        
        sys.exit(0)
    except Exception as e:
        print(f"Attempt {attempt}: {type(e).__name__}")
        time.sleep(5)

print("FAILED: ComfyUI did not become ready")
sys.exit(1)
