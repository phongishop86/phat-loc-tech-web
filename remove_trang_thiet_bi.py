import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<!-- Bottom Dark Section \(TRANG THIẾT BỊ\) -->.*?(</div>\s*</section>\s*<!-- Partner Brands Section -->)'

if re.search(pattern, content, flags=re.DOTALL):
    content = re.sub(pattern, r'\1', content, flags=re.DOTALL)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully removed the Trang Thiet Bi section.")
else:
    print("Could not find the target section.")
