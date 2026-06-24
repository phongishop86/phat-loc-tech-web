import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Finding the exact block using regex since there might be slight variations
# The block is inside the first h1
# We look for KIẾN TẠO HẠ TẦNG SỐ and NÂNG TẦM DOANH NGHIỆP
pattern = re.compile(r'(<span class="text-white drop-shadow-md">)[^<]+(</span><br/>\s*<span class="text-\[#1e3a8a\] drop-shadow-md">)[^<]+(</span>)')

new_content = r'\g<1>CÔNG NGHỆ TOÀN DIỆN –\g<2>GIẢI PHÁP BỀN VỮNG\g<3>'

content = pattern.sub(new_content, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero title updated successfully.")
