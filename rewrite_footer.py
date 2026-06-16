import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_footer = """<footer class="w-full bg-[#003380] text-white pt-16 pb-8 border-t border-[#003380]">
    <div class="container mx-auto px-4 max-w-[1400px]">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-10 mb-12">
            
            <!-- Column 1: Info -->
            <div class="lg:col-span-4">
                <h4 class="font-bold text-lg mb-4">CÔNG TY TNHH PHÁT LỘC TECH</h4>
                <p class="text-white/80 text-sm leading-relaxed mb-6">
                    Đối tác công nghệ toàn diện cho doanh nghiệp vừa và nhỏ. Chuyên cung cấp giải pháp máy tính, camera, hạ tầng mạng và phần mềm.
                </p>
                <ul class="space-y-2 text-sm text-white/90">
                    <li><span class="font-semibold">Người đại diện:</span> NGUYỄN THANH PHONG</li>
                    <li><span class="font-semibold">MST:</span> 0319347662</li>
                    <li><span class="font-semibold">Địa chỉ:</span> Số 491/1 Trường Chinh, Phường Tân Bình, Thành phố Hồ Chí Minh, Việt Nam</li>
                    <li><span class="font-semibold">Hotline:</span> 0932 685 794</li>
                    <li><span class="font-semibold">Email:</span> phatloctech.ltd@gmail.com</li>
                </ul>
            </div>

            <!-- Column 2: Dịch vụ -->
            <div class="lg:col-span-2">
                <h4 class="font-bold text-lg mb-4">Dịch vụ</h4>
                <ul class="space-y-3 text-sm text-white/80">
                    <li><a href="#thiet-bi" class="hover:text-white transition">Máy tính doanh nghiệp</a></li>
                    <li><a href="#ha-tang" class="hover:text-white transition">Camera giám sát</a></li>
                    <li><a href="#ha-tang" class="hover:text-white transition">Hạ tầng mạng</a></li>
                    <li><a href="#dich-vu" class="hover:text-white transition">IT thuê ngoài</a></li>
                </ul>
            </div>

            <!-- Column 3: Chính sách -->
            <div class="lg:col-span-2">
                <h4 class="font-bold text-lg mb-4">Chính sách</h4>
                <ul class="space-y-3 text-sm text-white/80">
                    <li><a href="#" class="hover:text-white transition">Bảo hành</a></li>
                    <li><a href="#" class="hover:text-white transition">Đổi trả</a></li>
                    <li><a href="#" class="hover:text-white transition">Bảo mật thông tin</a></li>
                </ul>
            </div>

            <!-- Column 4: Bản đồ -->
            <div class="lg:col-span-4">
                <h4 class="font-bold text-lg mb-4">Bản đồ</h4>
                <div class="w-full h-40 rounded-xl overflow-hidden shadow-lg border border-white/20">
                    <iframe src="https://maps.google.com/maps?q=V%C4%83n%20ph%C3%B2ng%20%E1%BA%A3o%20T%C3%A2n%20B%C3%ACnh%20-%20SeaOffice&t=&z=16&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                </div>
            </div>

        </div>

        <div class="border-t border-white/10 pt-8 text-center text-xs text-white/60">
            <p>© 2026 Phát Lộc Tech. All rights reserved.</p>
        </div>
    </div>
</footer>"""

# Use regex to replace the old footer block
footer_pattern = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL)
content = footer_pattern.sub(new_footer, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Footer replaced successfully.")
