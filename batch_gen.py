#!/usr/bin/env python3
"""Batch generate cartoon illustrations for lesson sentences via ComfyUI."""

import json
import os
import time
import urllib.request

HOST = "http://172.23.0.1:8190"
WORKFLOW_PATH = "/mnt/d/hermes/deepeng/web/sdxl_workflow.json"
LESSONS_PATH = "/mnt/d/hermes/deepeng/web/lessons.json"
IMAGES_BASE = "/mnt/d/hermes/deepeng/web/images"

# Style prefix for all prompts
STYLE_PREFIX = "simple cartoon illustration, children's book style, cute and clean, soft pastel colors, flat vector art"

# Negative prompt for all
NEGATIVE = "ugly, blurry, low quality, deformed, watermark, text, photograph, realistic, complex details, cropped, bad anatomy"

def load_workflow():
    with open(WORKFLOW_PATH) as f:
        return json.load(f)

def submit_prompt(workflow, prompt_text, seed=None):
    """Submit a prompt to ComfyUI and return prompt_id."""
    wf = json.loads(json.dumps(workflow))  # deep copy
    wf["6"]["inputs"]["text"] = f"{STYLE_PREFIX}, {prompt_text}"
    wf["7"]["inputs"]["text"] = NEGATIVE
    wf["3"]["inputs"]["steps"] = 25
    wf["3"]["inputs"]["seed"] = seed if seed else int(time.time() * 1000) % 999999999
    wf["5"]["inputs"]["width"] = 768
    wf["5"]["inputs"]["height"] = 768

    payload = {"prompt": wf, "client_id": f"batch-{int(time.time())}"}
    req = urllib.request.Request(
        f"{HOST}/prompt",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    try:
        resp = urllib.request.urlopen(req, timeout=60)
        result = json.loads(resp.read())
        if "prompt_id" in result:
            return result["prompt_id"]
        else:
            print(f"  Submit error: {result}")
            return None
    except Exception as e:
        print(f"  Submit failed: {e}")
        return None

def wait_for_completion(prompt_id, timeout=120):
    """Poll until the prompt completes."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            req = urllib.request.Request(f"{HOST}/history/{prompt_id}")
            resp = urllib.request.urlopen(req, timeout=10)
            history = json.loads(resp.read())
            entry = history.get(prompt_id, {})
            status = entry.get("status", {})
            if status.get("completed"):
                return entry.get("outputs", {})
            if status.get("status_str") == "error":
                error_msg = entry.get("error", {}).get("message", "unknown error")
                print(f"  Execution error: {error_msg}")
                return None
        except urllib.error.HTTPError as e:
            if e.code == 404:
                pass  # Not in history yet
            else:
                print(f"  HTTP error: {e}")
        except Exception as e:
            print(f"  Poll error: {e}")
        time.sleep(2)
    print(f"  Timeout for {prompt_id}")
    return None

def download_image(prompt_id, output_path):
    """Download the generated image from a completed prompt."""
    try:
        req = urllib.request.Request(f"{HOST}/history/{prompt_id}")
        resp = urllib.request.urlopen(req, timeout=10)
        history = json.loads(resp.read())
        entry = history.get(prompt_id, {})
        outputs = entry.get("outputs", {})
        
        for node_id, node_out in outputs.items():
            for img_info in node_out.get("images", []):
                filename = img_info["filename"]
                subfolder = img_info.get("subfolder", "")
                img_type = img_info.get("type", "output")
                
                params = f"filename={filename}&subfolder={subfolder}&type={img_type}"
                dl_url = f"{HOST}/view?{params}"
                
                req_dl = urllib.request.Request(dl_url)
                resp_dl = urllib.request.urlopen(req_dl, timeout=60)
                data = resp_dl.read()
                
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, "wb") as f:
                    f.write(data)
                return len(data)
    except Exception as e:
        print(f"  Download failed: {e}")
        return None

def generate_image(workflow, prompt_text, output_path, seed=None):
    """Full pipeline: submit, wait, download for one image."""
    print(f"  Submitting...")
    prompt_id = submit_prompt(workflow, prompt_text, seed)
    if not prompt_id:
        return False
    
    print(f"  Waiting (ID: {prompt_id[:8]})...")
    outputs = wait_for_completion(prompt_id)
    if outputs is None:
        return False
    
    size = download_image(prompt_id, output_path)
    if size:
        print(f"  ✓ Saved: {output_path} ({size//1024}KB)")
        return True
    return False


def get_prompt_for_sentence(sentence):
    """Create a visual prompt describing the sentence content."""
    en = sentence["en"]
    
    prompt_map = {
        # Lesson 02 missing
        "I am a student.": "a cute young boy or girl wearing a school backpack and uniform, standing happily in front of a school building, smiling",
        "I study at school.": "a child sitting at a desk in a colorful classroom, reading a book with a pencil, chalkboard in background",
        "We have dinner together every evening.": "a happy family of three sitting around a dinner table with plates of food, warm cozy dining room, smiling faces",
        
        # Lesson 03
        "Today I go to the market with my mother.": "a mother and child walking hand in hand towards a colorful outdoor market full of stalls",
        "The market is big and busy.": "a bustling outdoor market scene with many colorful stalls and people shopping, fruits displayed everywhere",
        "There are many people there.": "a busy market street with many diverse people walking and shopping at various stalls",
        "We see fresh fruits and vegetables.": "a colorful market stall overflowing with fresh apples, oranges, bananas, carrots and leafy greens",
        "I like red apples and yellow bananas.": "close up of bright red apples and yellow bananas arranged beautifully on a wooden market table",
        "My mother buys some oranges and milk.": "a mother at a market stall picking up fresh oranges and a bottle of milk from the vendor",
        "We also buy bread and eggs for breakfast.": "a shopping bag containing fresh bread loaf and brown eggs, with a smiling child holding the bag",
        "I help my mother carry the bags.": "a happy child helping their mother carry shopping bags, both walking together from the market",
        "She says I am a good boy.": "a mother smiling warmly and patting a child's head, proud and affectionate moment, heartwarming scene",
        
        # Lesson 04
        "My best friend is Tom.": "two cute cartoon children, one boy with brown hair and one boy with glasses, standing together side by side as best friends",
        "He is ten years old like me.": "two happy cartoon children holding up ten fingers, both the same age, joyful expression, celebrating friendship",
        "We go to the same school.": "two children walking together towards a colorful school building, backpacks on, morning sunshine",
        "We sit next to each other in class.": "two children sitting at adjacent desks in a bright classroom, sharing a smile and a book",
        "After school, we play soccer in the park.": "two children playing soccer on a green grassy field in a sunny park, kicking a ball",
        "Tom is very funny.": "one child telling a funny story while the other child laughs joyfully, playful cartoon scene",
        "He makes me laugh every day.": "two children laughing together uncontrollably, happy tears, warm friendship moment",
        "Sometimes we do homework together.": "two children sitting at a desk doing homework together, helping each other, books and pencils scattered",
        "I am happy to have a friend like Tom.": "two children hugging each other warmly, smiling faces, sparkles of friendship around them",
        "Friends make life better.": "a group of diverse cartoon children holding hands in a circle, happy faces, rainbow and sunshine background",
        
        # Lesson 05
        "The weather changes every day.": "a split scene showing different weather: sun, rain clouds, and a rainbow, cute weather icons",
        "In spring, it is warm and rainy.": "a beautiful spring garden with colorful flowers blooming under a gentle rain and soft sun",
        "Flowers begin to grow.": "small green sprouts and colorful flowers pushing up from brown soil, sunshine above, cute gardening scene",
        "In summer, it is hot and sunny.": "a bright sunny summer day with a big yellow sun, children playing outside, ice cream and lemonade",
        "I like to swim in the pool.": "a happy child swimming in a blue swimming pool with floaties, splashing water, summer fun",
        "In autumn, the leaves turn yellow and red.": "a beautiful autumn tree with orange, red and yellow leaves falling, calm nature scene",
        "They fall from the trees.": "colorful autumn leaves gently falling from a tall tree, swirling in the breeze, soft warm colors",
        "In winter, it is cold and snowy.": "a snowy winter landscape with snowflakes falling, a cute snowman with a scarf and hat",
        "I wear a warm coat and play in the snow.": "a bundled-up child in a warm winter coat, scarf, and mittens playing joyfully in the snow",
        "Every season is special.": "four panels showing spring flowers, summer sun, autumn leaves, and winter snow, all beautiful and unique",
    }
    
    return prompt_map.get(en, f"cute cartoon style scene of: {en}")


def main():
    # Load lessons
    with open(LESSONS_PATH) as f:
        data = json.load(f)
    
    # Load workflow once
    workflow = load_workflow()
    
    # Only process lessons 2-5 (1 is done)
    for lesson in data["lessons"]:
        lid = lesson["id"]
        if lid not in [2, 3, 4, 5]:
            continue
        
        sentences = lesson["sentences"]
        lesson_dir = f"{IMAGES_BASE}/lesson_{lid:02d}"
        os.makedirs(lesson_dir, exist_ok=True)
        
        print(f"\n{'='*60}")
        print(f"Lesson {lid:02d}: {lesson['title']} ({len(sentences)} sentences)")
        print(f"{'='*60}")
        
        for i, sentence in enumerate(sentences, 1):
            output_path = f"{lesson_dir}/s_{i}.png"
            
            # Skip if already exists
            if os.path.exists(output_path):
                print(f"  [{i}/{len(sentences)}] ✓ Already exists, skipping")
                continue
            
            en = sentence["en"]
            prompt = get_prompt_for_sentence(sentence)
            print(f"\n  [{i}/{len(sentences)}] {en}")
            print(f"      Prompt: {prompt}")
            
            ok = generate_image(workflow, prompt, output_path)
            if not ok:
                print(f"  ✗ Failed for sentence {i}, retrying once...")
                ok = generate_image(workflow, prompt, output_path, seed=int(time.time()))
                if not ok:
                    print(f"  ✗ Failed twice, moving on")
            
            # Small delay between generations
            time.sleep(1)
    
    print(f"\n{'='*60}")
    print("Batch generation complete!")
    
    # Summary
    print("\nFinal file counts:")
    for lid in [2, 3, 4, 5]:
        d = f"{IMAGES_BASE}/lesson_{lid:02d}"
        files = [f for f in os.listdir(d) if f.endswith('.png')] if os.path.exists(d) else []
        print(f"  Lesson {lid:02d}: {len(files)}/{len(next(l['sentences'] for l in data['lessons'] if l['id']==lid))} images")


if __name__ == "__main__":
    main()
