import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Column 2 and Column 3
# Current HTML for Col 2 & 3:
# <!-- Column 2: Dịch vụ -->
# <div class="lg:col-span-2">
#     <h4 class="font-bold text-lg mb-4">Dịch vụ</h4>
#     <ul class="space-y-3 text-sm text-white/80">
#         <li><a href="#thiet-bi" class="hover:text-white transition">Máy tính doanh nghiệp</a></li>
#         <li><a href="#ha-tang" class="hover:text-white transition">Camera giám sát</a></li>
#         <li><a href="#ha-tang" class="hover:text-white transition">Hạ tầng mạng</a></li>
#         <li><a href="#dich-vu" class="hover:text-white transition">IT thuê ngoài</a></li>
#     </ul>
# </div>
#
# <!-- Column 3: Chính sách -->
# <div class="lg:col-span-2">
#     <h4 class="font-bold text-lg mb-4">Chính sách</h4>
#     <ul class="space-y-3 text-sm text-white/80">
#         <li><a href="#" class="hover:text-white transition">Bảo hành</a></li>
#         <li><a href="#" class="hover:text-white transition">Đổi trả</a></li>
#         <li><a href="#" class="hover:text-white transition">Bảo mật thông tin</a></li>
#     </ul>
# </div>

new_col2_3 = """<!-- Column 2: Dịch vụ -->
            <div class="lg:col-span-2">
                <h4 class="font-bold text-lg mb-4">Dịch vụ</h4>
                <ul class="space-y-3 text-sm text-white/80">
                    <li><a href="#thiet-bi" class="hover:text-white transition">Thiết bị Tin học</a></li>
                    <li><a href="#ha-tang" class="hover:text-white transition">Camera An Ninh & Mạng</a></li>
                    <li><a href="#dich-vu" class="hover:text-white transition">Dịch Vụ IT</a></li>
                    <li><a href="#phan-mem" class="hover:text-white transition">Tài Khoản Số & Bản Quyền</a></li>
                </ul>
            </div>

            <!-- Column 3: Chính sách -->
            <div class="lg:col-span-2">
                <h4 class="font-bold text-lg mb-4">Chính sách & Quy định</h4>
                <ul class="space-y-3 text-sm text-white/80">
                    <li><a href="chinh-sach-bao-mat.html" class="hover:text-white transition">Chính sách bảo mật</a></li>
                    <li><a href="dieu-kien-giao-dich.html" class="hover:text-white transition">Điều kiện giao dịch chung</a></li>
                    <li><a href="chinh-sach-van-chuyen.html" class="hover:text-white transition">Chính sách vận chuyển và giao nhận</a></li>
                    <li><a href="phuong-thuc-thanh-toan.html" class="hover:text-white transition">Các phương thức thanh toán</a></li>
                    <li><a class="policy-btn hover:text-white transition cursor-pointer" data-policy="baohanh">Chính sách bảo hành (Tóm tắt)</a></li>
                </ul>
            </div>"""

# Replace the block using regex
pattern = re.compile(r'<!-- Column 2.*?</div>\s*</div>', re.DOTALL)
content = pattern.sub(new_col2_3, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Footer links updated successfully.")
