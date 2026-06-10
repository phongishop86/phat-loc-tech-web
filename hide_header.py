import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<header class="w-full bg-white/95 backdrop-blur-lg z-50 shadow-sm sticky top-0 border-b border-slate-200">'
replacement = '<header class="hidden w-full bg-white/95 backdrop-blur-lg z-50 shadow-sm sticky top-0 border-b border-slate-200">'

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully hidden the top menu bar.")
else:
    print("Could not find the header tag.")
