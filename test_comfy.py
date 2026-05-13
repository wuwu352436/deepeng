"""Test ComfyUI connectivity after fresh launch"""
import urllib.request
import json
import time

host = "http://172.23.0.1:8188"
print("Testing ComfyUI connectivity...")

for attempt in range(1, 13):  # Wait up to 60 seconds
    try:
        req = urllib.request.Request(f"{host}/system_stats", headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=8)
        d = json.loads(resp.read())
        print(f"READY after {attempt*5}s!")
        print(f"System: {d.get('system', {}).get('name', 'unknown')}")
        
        # Check models
        req2 = urllib.request.Request(f"{host}/object_info/CheckpointLoaderSimple", 
                                       headers={"User-Agent": "Mozilla/5.0"})
        resp2 = urllib.request.urlopen(req2, timeout=5)
        info = json.loads(resp2.read())
        ckpts = info.get("CheckpointLoaderSimple", {}).get("input", {}).get("required", {}).get("ckpt_name", [[]])[0]
        print(f"\nAvailable checkpoints ({len(ckpts)} total):")
        for c in ckpts[:30]:
            print(f"  {c}")
        
        # Also check the queue
        try:
            qr = urllib.request.Request(f"{host}/queue", headers={"User-Agent": "Mozilla/5.0"})
            qrsp = urllib.request.urlopen(qr, timeout=3)
            print(f"\nQueue: {qrsp.read().decode()[:200]}")
        except:
            pass
        
        break
    except Exception as e:
        print(f"  Attempt {attempt}: {type(e).__name__}")
        time.sleep(5)
else:
    print("FAILED: Could not connect to ComfyUI after 60 seconds")
