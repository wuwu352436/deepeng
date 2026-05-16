#!/usr/bin/env python3
"""Generate missing scene images (6-9) for Lesson 1."""
import json, subprocess, time, random, os

# Prompts for sentences 6-9
new_prompts = {
    6: ("He sees his friend Ann.",
        "A young boy Tom meeting his friend Ann on the path near school, waving hello, school building in background, sunny day, children's book illustration, cute cartoon, warm soft colors"),
    7: ("They go to class together.",
        "Two children Tom and Ann walking into a classroom together, desks and blackboard, happy atmosphere, children's book illustration style, cute cartoon, warm colors"),
    8: ("Tom likes school.",
        "A young boy Tom sitting at a desk in classroom, smiling, raising his hand, books on desk, friendly teacher, children's book illustration style, cute cartoon, bright warm colors"),
    9: ("He feels happy.",
        "A young boy Tom walking home from school with a big smile, backpack, sunset, butterflies, peaceful happy scene, children's book illustration style, cute cartoon, warm golden light"),
}

# Load base workflow
with open("/mnt/d/hermes/deepeng/web/workflows/sdxl_deepeng_template.json") as f:
    base = json.load(f)

for num in [6, 7, 8, 9]:
    sentence, prompt_text = new_prompts[num]
    
    wf = json.loads(json.dumps(base))
    wf["6"]["inputs"]["text"] = prompt_text
    wf["3"]["inputs"]["seed"] = random.randint(1, 2**31)
    wf["9"]["inputs"]["filename_prefix"] = f"deepeng_lesson1_s{num}"
    
    payload = json.dumps({"prompt": wf}, ensure_ascii=False)
    tmp = f"D:\\deepeng_batch_s{num}.json"
    with open(tmp.replace("D:\\", "/mnt/d/"), "w", encoding="utf-8") as f:
        f.write(payload)
    
    print(f"[GEN] 句子{num}: {sentence}...", end=" ", flush=True)
    r = subprocess.run(
        ["cmd.exe", "/c", f"curl.exe -s -X POST http://127.0.0.1:8190/prompt -H \"Content-Type: application/json\" -d @{tmp}"],
        capture_output=True, text=True, timeout=15
    )
    resp = r.stdout.strip()
    
    if '"prompt_id"' not in resp:
        print(f"FAILED: {resp[:200]}")
        continue
    
    data = json.loads(resp)
    pid = data["prompt_id"]
    errs = data.get("node_errors", {})
    if errs:
        print(f"ERRORS: {errs}")
        continue
    
    print(f"OK (id={pid[:8]}...)")
    
    # Poll until done
    timeout = 90
    start = time.time()
    while time.time() - start < timeout:
        time.sleep(2)
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
                    # Copy to correct destination
                    dst = f"/mnt/d/hermes/deepeng/web/images/lesson_01/s_{num}.png"
                    subprocess.run(["cp", full.replace("D:\\", "/mnt/d/"), dst])
                    print(f"   DONE → s_{num}.png ({round(time.time()-start,1)}s)")
                break
        except:
            continue
    else:
        print(f"   TIMEOUT")
    
    time.sleep(1)

print("\n✅ All remaining images generated!")
