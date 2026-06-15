import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Quy Trình Triển Khai Heading
# Find the Quy Trình h2 tag
pattern_quy_trinh = re.compile(r'<h2[^>]*>\s*(?:QUY TRÌNH|QUY TR.*NH).*?</h2>', re.IGNORECASE | re.DOTALL)
new_quy_trinh = """<h2 class="text-4xl md:text-5xl lg:text-[56px] xl:text-[64px] font-black uppercase leading-[1.1] tracking-tight mb-8">
                    <span class="text-slate-900 drop-shadow-sm">QUY TRÌNH</span><br/>
                    <span class="text-[#1e3a8a] drop-shadow-sm">TRIỂN KHAI</span>
                </h2>"""
content = pattern_quy_trinh.sub(new_quy_trinh, content, count=1)

# 2. Update ALL other headings that currently use #0ea5e9 to use Navy (#1e3a8a)
# Hero: NÂNG TẦM DOANH NGHIỆP
content = content.replace('text-[#0ea5e9]', 'text-[#1e3a8a]')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Headings updated to Navy.")
