import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'class="w-full max-w-\[1200px\] max-h-\[75vh\] aspect-video object-contain relative z-10 drop-shadow-2xl hover:scale-\[1\.01\] transition-transform duration-500 rounded-2xl"'
replacement = 'class="w-full max-w-[1200px] h-auto relative z-10 drop-shadow-2xl hover:scale-[1.01] transition-transform duration-500 rounded-2xl"'

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully restored the original aspect ratio.")
else:
    print("Could not find the target class string.")
