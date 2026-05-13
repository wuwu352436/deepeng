import json

with open("/mnt/d/hermes/deepeng/web/data.js", "r") as f:
    content = f.read()
js_str = content[content.index("["):]
end = js_str.rindex("];") + 1
lessons = json.loads(js_str[:end])

for l in lessons[:5]:
    print(f"--- Lesson {l['id']}: {l['title']} ({len(l['sentences'])} sentences) ---")
    for s in l['sentences']:
        print(f"  s_{s['id']}: {s['en']}")
