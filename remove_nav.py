import glob
import re

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove Báo Giá 1 tab
    new_content = re.sub(r'\s*<div class="relative flex items-center h-full group py-6">\s*<a href="bao-gia-1\.html"[^>]*>.*?Báo Giá 1</a>\s*</div>', '', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Removed Báo Giá 1 from {file}")
