import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

perfect_footer = """<footer class="w-full bg-[#003380] text-white pt-16 pb-8 border-t border-[#003380]">
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
                    <li><a href="#thiet-bi" class="hover:text-white transition cursor-pointer">Thiết bị Tin học</a></li>
                    <li><a href="#ha-tang" class="hover:text-white transition cursor-pointer">Camera An Ninh & Mạng</a></li>
                    <li><a href="#dich-vu" class="hover:text-white transition cursor-pointer">Dịch Vụ IT</a></li>
                    <li><a href="#phan-mem" class="hover:text-white transition cursor-pointer">Tài Khoản Số & Bản Quyền</a></li>
                </ul>
            </div>

            <!-- Column 3: Chính sách -->
            <div class="lg:col-span-2">
                <h4 class="font-bold text-lg mb-4">Chính sách</h4>
                <ul class="space-y-3 text-sm text-white/80">
                    <li><a class="policy-btn hover:text-white transition cursor-pointer" data-policy="baomat">Chính sách bảo mật</a></li>
                    <li><a class="policy-btn hover:text-white transition cursor-pointer" data-policy="dieukien">Điều kiện giao dịch</a></li>
                    <li><a class="policy-btn hover:text-white transition cursor-pointer" data-policy="vanchuyen">Vận chuyển & giao nhận</a></li>
                    <li><a class="policy-btn hover:text-white transition cursor-pointer" data-policy="thanhtoan">Phương thức thanh toán</a></li>
                    <li><a class="policy-btn hover:text-white transition cursor-pointer" data-policy="baohanh">Chính sách bảo hành</a></li>
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

# Replace the current footer entirely
footer_pattern = re.compile(r'<footer.*?</footer>', re.DOTALL)
content = footer_pattern.sub(perfect_footer, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update script.js to handle the new policies
with open('script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# I will replace the custom alert logic for policy Type
new_js_logic = """if (policyType === 'baohanh') {
            title = "Chính Sách: Bảo hành 1 đổi 1";
            content = "Cam kết bảo hành 1 đổi 1 đối với tất cả thiết bị phần cứng do Phát Lộc Tech cung cấp trong vòng 30 ngày đầu tiên nếu phát sinh lỗi từ nhà sản xuất. Sau 30 ngày, sản phẩm sẽ được bảo hành theo đúng tiêu chuẩn và thời hạn của hãng (12-36 tháng).";
        } else if (policyType === 'hotro') {
            title = "Chính Sách: Hỗ trợ tận nơi (Ad-hoc)";
            content = "Cung cấp dịch vụ hỗ trợ kỹ thuật tận nơi (Ad-hoc) nhanh chóng trong vòng 2-4 giờ làm việc (giờ hành chính). Dịch vụ xử lý sự cố máy tính, cấu hình mạng, camera và máy chủ linh hoạt theo từng lần yêu cầu mà không cần ký hợp đồng bảo trì dài hạn.";
        } else if (policyType === 'thanhtoan') {
            title = "Chính Sách: Thanh toán & Vận chuyển";
            content = "Hỗ trợ đa dạng phương thức thanh toán: Tiền mặt, Chuyển khoản hoặc Thanh toán qua thẻ tín dụng. Đặc biệt, miễn phí giao hàng và lắp đặt tận nơi tại khu vực nội thành cho các đơn hàng thiết bị và máy bộ trị giá trên 2,000,000 VNĐ.";
        } else if (policyType === 'baomat') {
            title = "Chính sách: Bảo mật thông tin";
            content = "Chúng tôi cam kết bảo mật hoàn toàn thông tin cá nhân và dữ liệu doanh nghiệp của khách hàng. Không chia sẻ thông tin cho bất kỳ bên thứ ba nào khi chưa có sự đồng ý.";
        } else if (policyType === 'dieukien') {
            title = "Điều kiện giao dịch chung";
            content = "Tất cả giao dịch mua bán đều được thực hiện dựa trên sự thỏa thuận và hợp đồng rõ ràng. Khách hàng vui lòng kiểm tra kỹ sản phẩm trước khi nhận hàng và thanh toán.";
        } else if (policyType === 'vanchuyen') {
            title = "Vận chuyển & Giao nhận";
            content = "Miễn phí vận chuyển cho đơn hàng trên 2 triệu đồng trong nội thành. Thời gian giao hàng từ 1-3 ngày tùy thuộc vào vị trí địa lý của khách hàng.";
        }"""

js_pattern = re.compile(r"if \(policyType === 'baohanh'\) \{.*?\} else if \(policyType === 'thanhtoan'\) \{.*?\}", re.DOTALL)
js_content = js_pattern.sub(new_js_logic, js_content, count=1)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Footer and scripts updated successfully.")
