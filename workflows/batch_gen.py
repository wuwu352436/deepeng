#!/usr/bin/env python3
"""Batch generate Lesson 1 scene images via ComfyUI API bridge."""
import json, subprocess, sys, os, time, random

# All 5 prompts
prompts = [
    ("1", "Tom opens his eyes.",
     "A young boy Tom lying in bed opening his eyes, morning sunlight streaming through window, cozy bedroom, children's book illustration style, cute cartoon, warm soft colors, simple composition"),
    ("2", "It is morning.",
     "A bright morning scene outside a window, sunrise sky with soft orange and pink clouds, simple children's book illustration, peaceful atmosphere, warm colors"),
    ("3", "He gets up.",
     "A young boy Tom sitting up in bed, stretching his arms, bedroom background, morning light, children's book illustration style, cute cartoon, warm cozy feel"),
    ("4", "He eats bread and drinks milk.",
     "A young boy Tom sitting at a kitchen table, eating bread and drinking a glass of milk, simple breakfast scene, children's book illustration style, cute cartoon, warm cozy kitchen"),
    ("5", "Then he walks to school.",
     "A young boy Tom walking on a path with a backpack, trees and houses in background, going to school, sunny day, children's book illustration style, cute cartoon, bright colors"),
]

# Load base workflow
with open("/mnt/d/hermes/deepeng/web/workflows/sdxl_deepeng_template.json") as f:
    base = json.load(f)

results = []

for num, sentence, prompt_text in prompts:
    # Skip if already generated (check output dir)
    out_file = f"D:\\ComfyUI-aki\\ComfyUI\\output\\deepeng_scene_{num.zfill(5)}_.png"
    check = subprocess.run(
        ["cmd.exe", "/c", f"if exist {out_file} (echo EXISTS) else (echo MISSING)"],
        capture_output=True, text=True, timeout=5
    )
    if "EXISTS" in check.stdout:
        print(f"[SKIP] 句子{num}: {sentence} — already exists")
        results.append((num, sentence, out_file, "skipped"))
        continue

    # Prepare workflow
    wf = json.loads(json.dumps(base))  # deep copy
    wf["6"]["inputs"]["text"] = prompt_text
    wf["3"]["inputs"]["seed"] = random.randint(1, 2**31)
    wf["9"]["inputs"]["filename_prefix"] = f"deepeng_scene_{num}"

    payload = json.dumps({"prompt": wf}, ensure_ascii=False)

    # Write to temp file on D:
    tmp = f"D:\\deepeng_batch_{num}.json"
    with open(tmp.replace("D:\\", "/mnt/d/"), "w", encoding="utf-8") as f:
        f.write(payload)

    # Queue
    print(f"[GEN] 句子{num}: {sentence}...", end=" ", flush=True)
    r = subprocess.run(
        ["cmd.exe", "/c", f"curl.exe -s -X POST http://127.0.0.1:8190/prompt -H \"Content-Type: application/json\" -d @{tmp}"],
        capture_output=True, text=True, timeout=15
    )
    resp = r.stdout.strip()
    if '"prompt_id"' in resp:
        data = json.loads(resp)
        pid = data["prompt_id"]
        errs = data.get("node_errors", {})
        if errs:
            print(f"QUEUED WITH ERRORS: {errs}")
            results.append((num, sentence, str(errs), "error"))
            continue
        print(f"OK (id={pid[:8]}...)")

        # Poll until done
        timeout = 120
        start = time.time()
        while time.time() - start < timeout:
            time.sleep(3)
            hr = subprocess.run(
                ["cmd.exe", "/c", f"curl.exe -s http://127.0.0.1:8190/history/{pid}"],
                capture_output=True, text=True, timeout=10
            )
            try:
                hist = json.loads(hr.stdout)
                if pid in hist and hist[pid].get("status", {}).get("completed"):
                    imgs = hist[pid].get("outputs", {}).get("9", {}).get("images", [])
                    if imgs:
                        fn = imgs[0]["filename"]
                        full = f"D:\\ComfyUI-aki\\ComfyUI\\output\\{fn}"
                        print(f"   DONE → {fn} ({round(time.time()-start,1)}s)")
                        results.append((num, sentence, full, "done"))
                    else:
                        print(f"   DONE but no image output")
                        results.append((num, sentence, "no_image", "error"))
                    break
            except (json.JSONDecodeError, KeyError):
                continue
        else:
            print(f"   TIMEOUT after {timeout}s")
            results.append((num, sentence, "timeout", "error"))
    else:
        print(f"FAILED: {resp[:200]}")
        results.append((num, sentence, resp[:200], "error"))
    
    # Small delay between jobs
    time.sleep(2)

# Summary
print("\n" + "="*60)
print("BATCH GENERATION SUMMARY")
print("="*60)
for num, sentence, path, status in results:
    icon = "✅" if status == "done" else ("⏭️" if status == "skipped" else "❌")
    print(f"{icon} 句子{num}: {sentence} → {status}")
    if status == "done":
        print(f"      File: {path}")
print("="*60)
