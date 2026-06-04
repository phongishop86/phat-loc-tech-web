import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Split around main
head_header = re.split(r'<main.*?>', html)[0] + '<main class="flex-1">'
footer_tail = re.split(r'</main>', html)[1]

# Modify title
head_header = re.sub(r'<title>.*?</title>', '<title>Bảng Giá Dịch Vụ & Thiết Bị | Phát Lộc Tech</title>', head_header)

main_content = """
        <!-- Hero Section -->
        <section class="pt-32 pb-16 bg-gradient-to-b from-zinc-950 to-zinc-900 border-b border-white/5 relative overflow-hidden">
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[500px] bg-brand-green/5 blur-[120px] rounded-full pointer-events-none"></div>
            <div class="container mx-auto px-4 text-center relative z-10 reveal">
                <span class="inline-block py-1 px-3 rounded-full bg-brand-green/10 text-brand-green border border-brand-green/20 text-xs font-bold uppercase tracking-widest mb-6">Minh bạch - Rõ ràng</span>
                <h1 class="text-4xl md:text-6xl font-serif font-bold text-white mb-6">Bảng Giá <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-green to-emerald-400">Dịch Vụ & Thiết Bị</span></h1>
                <p class="text-zinc-400 max-w-2xl mx-auto mb-10 text-lg">Cam kết mang lại giá trị thiết thực nhất cho doanh nghiệp với chi phí được tối ưu hóa. Bảng giá dưới đây mang tính chất tham khảo, có thể thay đổi theo khảo sát thực tế.</p>
                
                <div class="flex justify-center gap-4">
                    <a href="#bao-tri-it" class="px-6 py-3 bg-zinc-900 hover:bg-brand-green hover:text-white border border-zinc-700 hover:border-brand-green text-zinc-300 rounded-lg transition-all font-semibold">Dịch Vụ IT</a>
                    <a href="#combo-thiet-bi" class="px-6 py-3 bg-zinc-900 hover:bg-brand-purple hover:text-white border border-zinc-700 hover:border-brand-purple text-zinc-300 rounded-lg transition-all font-semibold">Thiết Bị & Camera</a>
                </div>
            </div>
        </section>

        <!-- IT Maintenance Cards -->
        <section id="bao-tri-it" class="py-24 relative bg-zinc-950">
            <div class="container mx-auto px-4 max-w-7xl reveal">
                <div class="text-center mb-16">
                    <h2 class="text-3xl font-bold text-white mb-4">Gói Bảo Trì Hệ Thống IT (Hàng Tháng)</h2>
                    <p class="text-zinc-400">Giải pháp toàn diện giúp hệ thống máy tính doanh nghiệp vận hành ổn định 24/7.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Basic -->
                    <div class="bg-zinc-900/50 rounded-2xl border border-zinc-800 p-8 hover:border-brand-green/50 transition-colors">
                        <h3 class="text-xl font-bold text-white mb-2">Gói Cơ Bản</h3>
                        <p class="text-sm text-zinc-400 mb-6">Phù hợp văn phòng nhỏ (Dưới 10 máy tính)</p>
                        <div class="text-4xl font-black text-white mb-6">1.500.000<span class="text-lg text-zinc-500 font-normal">đ/tháng</span></div>
                        <ul class="space-y-4 mb-8">
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-green mt-1"></i><span class="text-zinc-300 text-sm">Kiểm tra định kỳ 1 lần/tháng</span></li>
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-green mt-1"></i><span class="text-zinc-300 text-sm">Hỗ trợ từ xa (Ultraview/Anydesk) không giới hạn</span></li>
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-green mt-1"></i><span class="text-zinc-300 text-sm">Có mặt xử lý sự cố tận nơi trong 4H</span></li>
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-green mt-1"></i><span class="text-zinc-300 text-sm">Vệ sinh PC 6 tháng/lần</span></li>
                        </ul>
                        <a href="#nhan-bao-gia" class="block w-full py-3 text-center bg-zinc-800 hover:bg-brand-green text-white font-bold rounded-xl transition-colors">Chọn Gói Này</a>
                    </div>
                    
                    <!-- Pro (Recommended) -->
                    <div class="bg-zinc-900 rounded-2xl border border-brand-purple p-8 transform md:-translate-y-4 shadow-[0_0_30px_rgba(139,92,246,0.15)] relative">
                        <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-brand-purple to-indigo-500 text-white text-xs font-bold px-4 py-1.5 rounded-full uppercase tracking-wider">Khuyên Dùng</div>
                        <h3 class="text-xl font-bold text-white mb-2">Gói Chuyên Nghiệp</h3>
                        <p class="text-sm text-zinc-400 mb-6">Phù hợp công ty vừa (10 - 30 máy tính)</p>
                        <div class="text-4xl font-black text-white mb-6">3.500.000<span class="text-lg text-zinc-500 font-normal">đ/tháng</span></div>
                        <ul class="space-y-4 mb-8">
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-purple mt-1"></i><span class="text-zinc-300 text-sm">Kiểm tra định kỳ 2 lần/tháng</span></li>
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-purple mt-1"></i><span class="text-zinc-300 text-sm">Bảo trì cả Server & Máy chấm công</span></li>
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-purple mt-1"></i><span class="text-zinc-300 text-sm">Có mặt xử lý sự cố tận nơi trong 2H</span></li>
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-purple mt-1"></i><span class="text-zinc-300 text-sm">Backup dữ liệu quan trọng định kỳ</span></li>
                        </ul>
                        <a href="#nhan-bao-gia" class="block w-full py-3 text-center bg-brand-purple hover:bg-brand-purple-dark text-white font-bold rounded-xl transition-colors shadow-lg shadow-brand-purple/25">Chọn Gói Này</a>
                    </div>
                    
                    <!-- Enterprise -->
                    <div class="bg-zinc-900/50 rounded-2xl border border-zinc-800 p-8 hover:border-brand-orange/50 transition-colors">
                        <h3 class="text-xl font-bold text-white mb-2">Gói Doanh Nghiệp</h3>
                        <p class="text-sm text-zinc-400 mb-6">Phù hợp quy mô lớn (> 30 máy & Server)</p>
                        <div class="text-4xl font-black text-white mb-6">Liên Hệ</div>
                        <ul class="space-y-4 mb-8">
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-orange mt-1"></i><span class="text-zinc-300 text-sm">Khảo sát & thiết kế giải pháp riêng</span></li>
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-orange mt-1"></i><span class="text-zinc-300 text-sm">Bố trí IT Helpdesk ngồi tại công ty (Tùy chọn)</span></li>
                            <li class="flex items-start gap-3"><i class="ph-fill ph-check-circle text-brand-orange mt-1"></i><span class="text-zinc-300 text-sm">Quản trị Firewall, Camera, Network toàn diện</span></li>
                        </ul>
                        <a href="#nhan-bao-gia" class="block w-full py-3 text-center bg-zinc-800 hover:bg-brand-orange text-white font-bold rounded-xl transition-colors">Yêu Cầu Khảo Sát</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Ad-hoc Services Table -->
        <section class="py-20 border-t border-white/5 bg-zinc-950/30">
            <div class="container mx-auto px-4 max-w-4xl reveal">
                <h3 class="text-2xl font-bold text-white mb-8 text-center">Bảng Giá Dịch Vụ Lẻ (Ad-hoc)</h3>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="border-b border-zinc-700 bg-zinc-900 text-zinc-400 text-sm uppercase tracking-wider">
                                <th class="p-4 font-semibold rounded-tl-lg">Tên dịch vụ</th>
                                <th class="p-4 font-semibold">Đơn vị</th>
                                <th class="p-4 font-semibold text-right rounded-tr-lg">Đơn giá (VNĐ)</th>
                            </tr>
                        </thead>
                        <tbody class="text-zinc-300 text-sm divide-y divide-zinc-800/50 bg-zinc-900/20">
                            <tr class="hover:bg-zinc-800/50 transition-colors">
                                <td class="p-4">Cài đặt Hệ điều hành (Windows) & Office cơ bản</td>
                                <td class="p-4">Máy</td>
                                <td class="p-4 text-right font-medium text-brand-green">150.000</td>
                            </tr>
                            <tr class="hover:bg-zinc-800/50 transition-colors">
                                <td class="p-4">Vệ sinh PC / Laptop thay keo tản nhiệt</td>
                                <td class="p-4">Máy</td>
                                <td class="p-4 text-right font-medium text-brand-green">150.000 - 250.000</td>
                            </tr>
                            <tr class="hover:bg-zinc-800/50 transition-colors">
                                <td class="p-4">Kiểm tra, khắc phục sự cố mạng (Không thay vật tư)</td>
                                <td class="p-4">Lần</td>
                                <td class="p-4 text-right font-medium text-brand-green">300.000</td>
                            </tr>
                            <tr class="hover:bg-zinc-800/50 transition-colors">
                                <td class="p-4">Cấu hình Router / Modem / Wifi Mesh</td>
                                <td class="p-4">Thiết bị</td>
                                <td class="p-4 text-right font-medium text-brand-green">Từ 200.000</td>
                            </tr>
                            <tr class="hover:bg-zinc-800/50 transition-colors">
                                <td class="p-4">Khôi phục dữ liệu ổ cứng bị format nhầm</td>
                                <td class="p-4">Ổ cứng</td>
                                <td class="p-4 text-right font-medium text-brand-green">Báo giá theo dung lượng</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- Hardware & Camera Combos -->
        <section id="combo-thiet-bi" class="py-24 border-t border-white/5 relative bg-gradient-to-b from-zinc-950 to-zinc-900">
            <div class="container mx-auto px-4 max-w-7xl reveal">
                <div class="text-center mb-16">
                    <h2 class="text-3xl font-bold text-white mb-4">Combo Lắp Đặt Thiết Bị / Camera</h2>
                    <p class="text-zinc-400">Trọn gói vật tư và công lắp đặt, không phát sinh chi phí ẩn.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <!-- Combo 1 -->
                    <div class="flex flex-col sm:flex-row bg-zinc-900 rounded-xl border border-zinc-800 overflow-hidden hover:border-zinc-600 transition-colors">
                        <div class="sm:w-1/3 bg-zinc-800 flex items-center justify-center p-6 text-brand-green">
                            <i class="ph-duotone ph-video-camera text-6xl"></i>
                        </div>
                        <div class="p-6 flex-1">
                            <h4 class="text-lg font-bold text-white mb-2">Trọn bộ 4 Camera Hikvision 2.0MP</h4>
                            <p class="text-sm text-zinc-400 mb-4 line-clamp-2">Bao gồm: 4 Mắt Camera 1080p, Đầu ghi 4 kênh, Ổ cứng 500GB, Nguồn, Jack BNC, 40m dây tín hiệu, Tên miền xem qua điện thoại, Công lắp đặt nội thành.</p>
                            <div class="flex items-center justify-between">
                                <span class="text-xs text-zinc-500 uppercase tracking-wider">Giá tham khảo</span>
                                <span class="text-xl font-black text-brand-green">4.200.000 đ</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Combo 2 -->
                    <div class="flex flex-col sm:flex-row bg-zinc-900 rounded-xl border border-zinc-800 overflow-hidden hover:border-zinc-600 transition-colors">
                        <div class="sm:w-1/3 bg-zinc-800 flex items-center justify-center p-6 text-brand-purple">
                            <i class="ph-duotone ph-wifi-high text-6xl"></i>
                        </div>
                        <div class="p-6 flex-1">
                            <h4 class="text-lg font-bold text-white mb-2">Hệ thống Wifi Mesh Văn Phòng (Dưới 30 User)</h4>
                            <p class="text-sm text-zinc-400 mb-4 line-clamp-2">Bao gồm: 1 Router cân bằng tải cơ bản, 2 Node Wifi Mesh băng tần kép, Cấu hình roaming, Công đi dây nổi/âm trần (cơ bản).</p>
                            <div class="flex items-center justify-between">
                                <span class="text-xs text-zinc-500 uppercase tracking-wider">Giá tham khảo</span>
                                <span class="text-xl font-black text-brand-purple">3.800.000 đ</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Combo 3 -->
                    <div class="flex flex-col sm:flex-row bg-zinc-900 rounded-xl border border-zinc-800 overflow-hidden hover:border-zinc-600 transition-colors">
                        <div class="sm:w-1/3 bg-zinc-800 flex items-center justify-center p-6 text-brand-orange">
                            <i class="ph-duotone ph-desktop text-6xl"></i>
                        </div>
                        <div class="p-6 flex-1">
                            <h4 class="text-lg font-bold text-white mb-2">Combo PC Văn Phòng Đồng Bộ Dell/HP</h4>
                            <p class="text-sm text-zinc-400 mb-4 line-clamp-2">Cấu hình: Core i3/i5, RAM 8GB, SSD 256GB, Màn hình 24 inch, Phím Chuột chính hãng. Bao gồm cài đặt sẵn HĐH và phần mềm cơ bản.</p>
                            <div class="flex items-center justify-between">
                                <span class="text-xs text-zinc-500 uppercase tracking-wider">Giá tham khảo</span>
                                <span class="text-xl font-black text-brand-orange">Từ 6.500.000 đ</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Combo 4 -->
                    <div class="flex flex-col sm:flex-row bg-zinc-900 rounded-xl border border-zinc-800 overflow-hidden hover:border-zinc-600 transition-colors">
                        <div class="sm:w-1/3 bg-zinc-800 flex items-center justify-center p-6 text-blue-500">
                            <i class="ph-duotone ph-fingerprint text-6xl"></i>
                        </div>
                        <div class="p-6 flex-1">
                            <h4 class="text-lg font-bold text-white mb-2">Trọn bộ Máy Chấm Công Vân Tay</h4>
                            <p class="text-sm text-zinc-400 mb-4 line-clamp-2">Máy chấm công vân tay chính hãng Hikvision/Ronald Jack, Hỗ trợ cài đặt phần mềm tính công trên 1 PC, Công lắp đặt treo tường nội thành.</p>
                            <div class="flex items-center justify-between">
                                <span class="text-xs text-zinc-500 uppercase tracking-wider">Giá tham khảo</span>
                                <span class="text-xl font-black text-blue-500">2.500.000 đ</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- CTA Form Section -->
        <section id="nhan-bao-gia" class="py-24 border-t border-white/5 relative bg-zinc-950 overflow-hidden">
            <!-- Decorative circle -->
            <div class="absolute bottom-0 right-0 w-[500px] h-[500px] bg-brand-purple/5 rounded-full blur-[100px] translate-x-1/2 translate-y-1/2 pointer-events-none"></div>
            
            <div class="container mx-auto px-4 max-w-3xl relative z-10 reveal">
                <div class="bg-zinc-900 border border-zinc-800 rounded-2xl p-8 md:p-12 shadow-2xl">
                    <div class="text-center mb-10">
                        <h2 class="text-3xl font-bold text-white mb-3">Yêu Cầu Báo Giá Riêng</h2>
                        <p class="text-zinc-400">Bạn không tìm thấy hạng mục cần thiết? Để lại thông tin, chuyên viên của chúng tôi sẽ gọi lại khảo sát và báo giá chi tiết trong 30 phút!</p>
                    </div>
                    
                    <form action="https://formsubmit.co/phongishop86@gmail.com" method="POST" class="space-y-5">
                        <input type="hidden" name="_subject" value="Yêu cầu Báo Giá Tùy Chỉnh từ Web">
                        <input type="hidden" name="_captcha" value="false">
                        
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                            <div>
                                <label class="block text-sm font-medium text-zinc-400 mb-2">Tên của bạn / Tên Công Ty *</label>
                                <input type="text" name="Tên" required class="w-full bg-zinc-950 border border-zinc-800 rounded-xl px-4 py-3 text-white focus:border-brand-purple focus:outline-none transition-colors">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-zinc-400 mb-2">Số điện thoại / Zalo *</label>
                                <input type="tel" name="Số điện thoại" required class="w-full bg-zinc-950 border border-zinc-800 rounded-xl px-4 py-3 text-white focus:border-brand-purple focus:outline-none transition-colors">
                            </div>
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-zinc-400 mb-2">Nhu cầu cụ thể (Lắp mới camera, Sửa máy in, Thuê IT...) *</label>
                            <textarea name="Yêu cầu chi tiết" required rows="4" class="w-full bg-zinc-950 border border-zinc-800 rounded-xl px-4 py-3 text-white focus:border-brand-purple focus:outline-none transition-colors resize-none"></textarea>
                        </div>
                        
                        <button type="submit" class="w-full py-4 bg-brand-purple hover:bg-brand-purple-dark text-white font-bold rounded-xl transition-all shadow-[0_4px_20px_rgba(139,92,246,0.3)] hover:shadow-[0_4px_25px_rgba(139,92,246,0.5)] mt-4">
                            Nhận Báo Giá Ngay
                        </button>
                    </form>
                </div>
            </div>
        </section>
"""

full_html = head_header + main_content + '\n    </main>' + footer_tail

with open('bao-gia.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
print("Created bao-gia.html")
