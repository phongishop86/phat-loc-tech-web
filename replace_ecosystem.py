import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The pattern spans from the start of the title div to the end of the 4 Solution Cards
pattern = r'<div class="text-center mb-16 reveal">.*?<!-- 4 Solution Cards -->.*?</div>\s*</div>'

new_content = """<div class="w-full max-w-[1200px] mx-auto reveal flex justify-center pb-20">
                <img src="he-sinh-thai-giai-phap.jpg" alt="Hệ Sinh Thái Giải Pháp Công Nghệ Toàn Diện" class="w-full h-auto rounded-[32px] shadow-2xl shadow-blue-900/10 border border-slate-200" />
            </div>"""

# Replace
if re.search(pattern, content, flags=re.DOTALL):
    content = re.sub(pattern, new_content, content, flags=re.DOTALL)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced HTML section with the image.")
else:
    print("Could not find the pattern to replace.")
