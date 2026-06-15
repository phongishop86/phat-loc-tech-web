import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Ecosystem Heading
# We look for the h2 tag that contains "HỆ SINH THÁI" or its mojibake equivalent.
eco_pattern = re.compile(r'<h2[^>]*>\s*(?:HỆ SINH THÁI|H.*SINH TH.*).*?</h2>', re.IGNORECASE | re.DOTALL)
new_eco_heading = """<h2 class="text-4xl md:text-5xl lg:text-[56px] xl:text-[64px] font-black uppercase leading-[1.1] tracking-tight mb-8">
                          <span class="text-slate-900 drop-shadow-sm">HỆ SINH THÁI GIẢI PHÁP</span><br/>
                          <span class="text-[#0ea5e9] drop-shadow-sm">CÔNG NGHỆ TOÀN DIỆN</span>
                      </h2>"""
content = eco_pattern.sub(new_eco_heading, content, count=1)

# 2. Replace Tại Sao Chọn Heading
why_pattern = re.compile(r'<h2[^>]*>\s*(?:Tại Sao Chọn|T.*i Sao Ch.*n).*?</h2>', re.IGNORECASE | re.DOTALL)
new_why_heading = """<h2 class="text-4xl md:text-5xl lg:text-[56px] xl:text-[64px] font-black uppercase leading-[1.1] tracking-tight mb-8">
                        <span class="text-slate-900 drop-shadow-sm">TẠI SAO CHỌN</span><br/>
                        <span class="text-[#0ea5e9] drop-shadow-sm">PHÁT LỘC TECH?</span>
                    </h2>"""
content = why_pattern.sub(new_why_heading, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Headings synchronized successfully.")
