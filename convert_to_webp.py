"""
DeepEng 图片批量转 WebP 工具
用法: python3 convert_to_webp.py [--quality 82] [--dry-run]
"""
import sys
from pathlib import Path
from PIL import Image

BASE = Path(__file__).parent
DIRS = [BASE / "images", BASE / "scenes"]

QUALITY = 82
DRY_RUN = False

for arg in sys.argv[1:]:
    if arg.startswith("--quality="):
        QUALITY = int(arg.split("=")[1])
    elif arg == "--dry-run":
        DRY_RUN = True

stats = {"total_o": 0, "total_n": 0, "ok": 0, "skip": 0, "err": 0}

for img_dir in DIRS:
    if not img_dir.exists():
        print(f"SKIP: {img_dir} not found")
        continue

    for png in sorted(img_dir.rglob("*.png")):
        orig = png.stat().st_size
        stats["total_o"] += orig
        if orig == 0:
            print(f"SKIP (empty): {png.relative_to(BASE)}")
            stats["skip"] += 1
            continue

        webp = png.with_suffix(".webp")
        if DRY_RUN:
            print(f"WOULD CONVERT: {png.relative_to(BASE)} ({orig//1024}KB)")
            continue

        try:
            img = Image.open(png)
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGB")
            img.save(webp, "WEBP", quality=QUALITY)
            new = webp.stat().st_size
            stats["total_n"] += new
            stats["ok"] += 1
            pct = (1 - new / orig) * 100
            print(f"OK: {png.name} ({orig//1024}KB→{new//1024}KB, -{pct:.0f}%)")
        except Exception as e:
            stats["err"] += 1
            print(f"ERR: {png.name} — {e}")

print("\n" + "=" * 55)
if DRY_RUN:
    print(f"Would convert: {stats['ok']} files")
else:
    print(f"Converted: {stats['ok']} | Skipped: {stats['skip']} | Errors: {stats['err']}")
    print(f"Original: {stats['total_o']//1024}KB → WebP: {stats['total_n']//1024}KB")
    if stats["total_o"] > 0:
        print(f"Reduction: {(1-stats['total_n']/stats['total_o'])*100:.1f}%")
