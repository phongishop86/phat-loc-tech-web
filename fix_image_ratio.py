import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<img src="kien-tao-ha-tang-so.png".*?/>'
replacement = '<img src="kien-tao-ha-tang-so.png" alt="Kiến tạo hạ tầng số" class="w-full max-w-[1200px] max-h-[75vh] aspect-video object-contain relative z-10 drop-shadow-2xl hover:scale-[1.01] transition-transform duration-500 rounded-2xl" />'

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated the image aspect ratio.")
else:
    print("Could not find the image tag.")
