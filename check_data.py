import json

# Check lessons.json sentences
with open('/mnt/d/hermes/deepeng/web/lessons.json', 'r') as f:
    data = json.load(f)

print("=== lessons.json ===")
for l in data['lessons'][:6]:
    print(f"Lesson {l['id']}: {l['title']} ({l['zh_title']}) - {len(l.get('sentences',[]))} sentences")

# Check data.js sentences
with open('/mnt/d/hermes/deepeng/web/data.js', 'r') as f:
    content = f.read()

js_str = content[content.index('['):]
end = js_str.rindex('];') + 1
lessons = json.loads(js_str[:end])

print("\n=== data.js ===")
for l in lessons[:6]:
    print(f"Lesson {l['id']}: {l['title']} - {len(l.get('sentences',[]))} sentences")

# Find image references in index.html
with open('/mnt/d/hermes/deepeng/web/index.html', 'r') as f:
    html = f.read()

# Search for image-related patterns
import re
for pattern in ['img', 'src', 'image', '.png', '.jpg', 's_', 'lesson']:
    matches = [(i, line) for i, line in enumerate(html.split('\n'), 1) if pattern in line.lower()]
    if matches:
        print(f"\n=== index.html: '{pattern}' references ===")
        for lineno, line in matches[:10]:
            print(f"  L{lineno}: {line.strip()[:120]}")
