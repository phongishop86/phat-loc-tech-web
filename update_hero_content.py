import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = """<div class="max-w-4xl">
                <h1 class="text-4xl md:text-5xl lg:text-[56px] xl:text-[64px] font-montserrat font-black uppercase leading-[1.25] tracking-tight mb-8">
                    <span class="text-white drop-shadow-md">CÔNG NGHỆ TOÀN DIỆN</span><br/>
                    <span class="text-[#1e3a8a] drop-shadow-md">GIẢI PHÁP BỀN VỮNG</span>
                </h1>
                
                <p class="text-slate-200 text-sm md:text-base lg:text-lg leading-relaxed mb-5 max-w-3xl font-medium">
                    Phát Lộc Tech cung cấp hệ sinh thái công nghệ toàn diện dành cho cá nhân, hộ kinh doanh và doanh nghiệp vừa và nhỏ. Từ máy tính, máy chủ, hệ thống camera giám sát, hạ tầng mạng, phần mềm bản quyền đến dịch vụ IT thuê ngoài, chúng tôi mang đến những giải pháp đồng bộ, ổn định và phù hợp với nhu cầu thực tế của từng khách hàng.
                </p>

                <p class="text-slate-200 text-sm md:text-base lg:text-lg leading-relaxed mb-10 max-w-3xl font-medium">
                    Với phương châm "Công nghệ toàn diện – Giải pháp bền vững", Phát Lộc Tech không chỉ cung cấp sản phẩm và dịch vụ, mà còn đồng hành lâu dài trong quá trình vận hành, bảo mật và phát triển hệ thống công nghệ thông tin của khách hàng.
                </p>
            </div>"""

# Replace the block
# We want to replace from `<div class="max-w-4xl">` up to the `</div>` that closes it.
# The `</div>` that closes `max-w-4xl` is followed by `</div>\n      </section>`
pattern = re.compile(r'<div class="max-w-4xl">.*?</div>\s*</div>\s*</section>', re.DOTALL)
replacement = new_content + "\n          </div>\n      </section>"

content = pattern.sub(replacement, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero content updated successfully.")
