import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the inner custom logos with the real image
custom_logo_pattern = r'<div class="flex flex-col items-center leading-none">\s*<span class="[^"]*">PL</span>\s*<span class="[^"]*">T</span>\s*</div>'
real_logo_img = '<img src="PLT-Logo-final.png" alt="PLT Logo" class="w-full h-full object-contain p-1" />'
content = re.sub(custom_logo_pattern, real_logo_img, content)

# 2. Replace the #services section
# The current #services section looks like:
# <!-- Services Section (4 Cards) -->
# <section id="services" ...>
# ...
# </section>
services_pattern = r'<!-- Services Section \(4 Cards\) -->.*?</section>'

new_services_html = """<!-- Ecosystem Section -->
        <section id="services" class="w-full bg-slate-50 py-24 border-b border-slate-200 relative overflow-hidden">
            <!-- Background depth -->
            <div class="absolute top-0 inset-x-0 h-px bg-gradient-to-r from-transparent via-slate-300 to-transparent"></div>
            <div class="absolute -top-40 -right-40 w-96 h-96 bg-blue-100/50 rounded-full blur-[100px] pointer-events-none"></div>

            <div class="container mx-auto px-4 max-w-7xl relative z-10">
                <!-- Main Title -->
                <div class="text-center mb-16">
                    <h2 class="text-3xl md:text-4xl lg:text-5xl font-[var(--font-oswald)] font-bold text-slate-900 mb-4 tracking-tight uppercase">
                        HỆ SINH THÁI GIẢI PHÁP <span class="text-[#1d4ed8]">CÔNG NGHỆ TOÀN DIỆN</span>
                    </h2>
                    <p class="text-slate-600 max-w-3xl mx-auto text-lg">Đồng hành cùng doanh nghiệp trong mọi nhu cầu về hạ tầng CNTT, bảo mật, giám sát và chuyển đổi số.</p>
                </div>

                <!-- Ecosystem Grid -->
                <div class="flex flex-col lg:flex-row items-center justify-between gap-12 lg:gap-4 relative">
                    
                    <!-- Left Column (3 Nodes) -->
                    <div class="flex flex-col gap-6 w-full lg:w-[35%] relative z-20">
                        <!-- Node 1 -->
                        <div class="flex items-center gap-4 bg-white p-4 rounded-full shadow-lg shadow-rose-900/5 border border-slate-100 hover:shadow-xl hover:border-rose-200 transition transform hover:-translate-y-1 group">
                            <div class="w-14 h-14 shrink-0 rounded-full bg-gradient-to-br from-rose-500 to-pink-500 flex items-center justify-center text-white shadow-inner group-hover:scale-110 transition">
                                <i class="ph-duotone ph-laptop text-3xl"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-rose-600 uppercase text-sm mb-0.5">MÁY TÍNH & LAPTOP</h3>
                                <p class="text-[11px] text-slate-600 leading-tight pr-4">Cung cấp máy tính, laptop, workstation và thiết bị chính hãng cho doanh nghiệp.</p>
                            </div>
                        </div>
                        <!-- Node 2 -->
                        <div class="flex items-center gap-4 bg-white p-4 rounded-full shadow-lg shadow-purple-900/5 border border-slate-100 hover:shadow-xl hover:border-purple-200 transition transform hover:-translate-y-1 group">
                            <div class="w-14 h-14 shrink-0 rounded-full bg-gradient-to-br from-purple-600 to-violet-600 flex items-center justify-center text-white shadow-inner group-hover:scale-110 transition">
                                <i class="ph-duotone ph-video-camera text-3xl"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-purple-700 uppercase text-sm mb-0.5">CAMERA GIÁM SÁT</h3>
                                <p class="text-[11px] text-slate-600 leading-tight pr-4">Thi công và lắp đặt hệ thống camera giám sát chất lượng cao cho mọi mô hình.</p>
                            </div>
                        </div>
                        <!-- Node 3 -->
                        <div class="flex items-center gap-4 bg-white p-4 rounded-full shadow-lg shadow-cyan-900/5 border border-slate-100 hover:shadow-xl hover:border-cyan-200 transition transform hover:-translate-y-1 group">
                            <div class="w-14 h-14 shrink-0 rounded-full bg-gradient-to-br from-cyan-500 to-blue-500 flex items-center justify-center text-white shadow-inner group-hover:scale-110 transition">
                                <i class="ph-duotone ph-printer text-3xl"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-cyan-700 uppercase text-sm mb-0.5">THIẾT BỊ VĂN PHÒNG</h3>
                                <p class="text-[11px] text-slate-600 leading-tight pr-4">Cung cấp máy in, máy chiếu, thiết bị văn phòng, UPS và vật tư chính hãng.</p>
                            </div>
                        </div>
                    </div>

                    <!-- Center Column (Logo) -->
                    <div class="flex flex-col items-center justify-center w-full lg:w-[30%] relative z-10 order-first lg:order-none mb-12 lg:mb-0">
                        <!-- Connecting Lines on PC -->
                        <div class="hidden lg:block absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[150%] h-0.5 bg-slate-200 z-0"></div>
                        <div class="hidden lg:block absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%] h-0.5 bg-slate-200 z-0 rotate-45"></div>
                        <div class="hidden lg:block absolute top-3/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%] h-0.5 bg-slate-200 z-0 -rotate-45"></div>

                        <!-- Outer Rainbow Circle -->
                        <div class="w-56 h-56 lg:w-64 lg:h-64 rounded-full p-2 bg-gradient-to-tr from-cyan-400 via-blue-500 to-rose-500 shadow-2xl shadow-blue-500/20 relative z-20">
                            <div class="w-full h-full bg-white rounded-full p-6 lg:p-10 flex items-center justify-center shadow-inner">
                                <img src="PLT-Logo-final.png" alt="PLT Logo" class="w-full h-full object-contain" />
                            </div>
                            <!-- Small decorative dots -->
                            <div class="absolute top-0 left-1/2 w-4 h-4 bg-rose-500 rounded-full -translate-x-1/2 -translate-y-1/2 border-2 border-white shadow-sm"></div>
                            <div class="absolute bottom-0 left-1/2 w-4 h-4 bg-emerald-500 rounded-full -translate-x-1/2 translate-y-1/2 border-2 border-white shadow-sm"></div>
                            <div class="absolute top-1/2 left-0 w-4 h-4 bg-purple-500 rounded-full -translate-x-1/2 -translate-y-1/2 border-2 border-white shadow-sm"></div>
                            <div class="absolute top-1/2 right-0 w-4 h-4 bg-orange-500 rounded-full translate-x-1/2 -translate-y-1/2 border-2 border-white shadow-sm"></div>
                        </div>
                        <div class="mt-8 text-center relative z-20 bg-slate-50/80 backdrop-blur-sm px-6 py-2 rounded-2xl">
                            <h3 class="text-2xl font-black text-slate-900 tracking-wider">PHÁT LỘC TECH</h3>
                            <p class="text-[13px] font-bold text-slate-500 mt-1 uppercase">Đối tác công nghệ toàn diện<br/>cho doanh nghiệp</p>
                        </div>
                    </div>

                    <!-- Right Column (3 Nodes) -->
                    <div class="flex flex-col gap-6 w-full lg:w-[35%] relative z-20">
                        <!-- Node 4 -->
                        <div class="flex items-center gap-4 bg-white p-4 rounded-full shadow-lg shadow-blue-900/5 border border-slate-100 hover:shadow-xl hover:border-blue-200 transition transform hover:-translate-y-1 flex-row-reverse lg:flex-row text-left group">
                            <div class="w-14 h-14 shrink-0 rounded-full bg-gradient-to-br from-blue-600 to-indigo-600 flex items-center justify-center text-white shadow-inner group-hover:scale-110 transition">
                                <i class="ph-duotone ph-tree-structure text-3xl"></i>
                            </div>
                            <div class="lg:text-right pl-4 lg:pl-0">
                                <h3 class="font-bold text-blue-700 uppercase text-sm mb-0.5">HẠ TẦNG MẠNG</h3>
                                <p class="text-[11px] text-slate-600 leading-tight">Thiết kế và triển khai hệ thống mạng LAN, WiFi, Firewall, Server chuyên nghiệp.</p>
                            </div>
                        </div>
                        <!-- Node 5 -->
                        <div class="flex items-center gap-4 bg-white p-4 rounded-full shadow-lg shadow-emerald-900/5 border border-slate-100 hover:shadow-xl hover:border-emerald-200 transition transform hover:-translate-y-1 flex-row-reverse lg:flex-row text-left group">
                            <div class="w-14 h-14 shrink-0 rounded-full bg-gradient-to-br from-emerald-500 to-green-600 flex items-center justify-center text-white shadow-inner group-hover:scale-110 transition">
                                <i class="ph-duotone ph-headset text-3xl"></i>
                            </div>
                            <div class="lg:text-right pl-4 lg:pl-0">
                                <h3 class="font-bold text-emerald-700 uppercase text-sm mb-0.5">DỊCH VỤ IT</h3>
                                <p class="text-[11px] text-slate-600 leading-tight">IT Helpdesk, bảo trì hệ thống, quản trị mạng và hỗ trợ kỹ thuật 24/7.</p>
                            </div>
                        </div>
                        <!-- Node 6 -->
                        <div class="flex items-center gap-4 bg-white p-4 rounded-full shadow-lg shadow-orange-900/5 border border-slate-100 hover:shadow-xl hover:border-orange-200 transition transform hover:-translate-y-1 flex-row-reverse lg:flex-row text-left group">
                            <div class="w-14 h-14 shrink-0 rounded-full bg-gradient-to-br from-orange-400 to-amber-500 flex items-center justify-center text-white shadow-inner group-hover:scale-110 transition">
                                <i class="ph-duotone ph-cloud-arrow-up text-3xl"></i>
                            </div>
                            <div class="lg:text-right pl-4 lg:pl-0">
                                <h3 class="font-bold text-orange-600 uppercase text-sm mb-0.5">PHẦN MỀM & SỐ HÓA</h3>
                                <p class="text-[11px] text-slate-600 leading-tight">Hóa đơn điện tử, chữ ký số, phần mềm quản lý và giải pháp chuyển đổi số.</p>
                            </div>
                        </div>
                    </div>

                </div>

                <!-- Bottom Criteria Banner -->
                <div class="mt-20 bg-white rounded-[2rem] p-6 lg:p-8 flex flex-col md:flex-row flex-wrap lg:flex-nowrap justify-between gap-6 shadow-xl shadow-slate-200/50 border border-slate-100">
                    <!-- Item 1 -->
                    <div class="flex items-start gap-3 w-full sm:w-[45%] lg:w-1/4 group">
                        <i class="ph-duotone ph-shield-check text-4xl text-[#1d4ed8] group-hover:scale-110 transition-transform"></i>
                        <div class="mt-1">
                            <h4 class="text-xs font-bold text-slate-900 uppercase">SẢN PHẨM CHÍNH HÃNG</h4>
                            <p class="text-[11px] text-slate-500 mt-1">Đa dạng thương hiệu uy tín toàn cầu</p>
                        </div>
                    </div>
                    <!-- Item 2 -->
                    <div class="flex items-start gap-3 w-full sm:w-[45%] lg:w-1/4 lg:border-l lg:border-slate-200 lg:pl-6 group">
                        <i class="ph-duotone ph-gear text-4xl text-[#1d4ed8] group-hover:scale-110 transition-transform"></i>
                        <div class="mt-1">
                            <h4 class="text-xs font-bold text-slate-900 uppercase">GIẢI PHÁP TOÀN DIỆN</h4>
                            <p class="text-[11px] text-slate-500 mt-1">Tư vấn – Thiết kế – Triển khai – Bảo trì trọn gói</p>
                        </div>
                    </div>
                    <!-- Item 3 -->
                    <div class="flex items-start gap-3 w-full sm:w-[45%] lg:w-1/4 lg:border-l lg:border-slate-200 lg:pl-6 group">
                        <i class="ph-duotone ph-lock-key text-4xl text-[#1d4ed8] group-hover:scale-110 transition-transform"></i>
                        <div class="mt-1">
                            <h4 class="text-xs font-bold text-slate-900 uppercase">BẢO MẬT & AN TOÀN</h4>
                            <p class="text-[11px] text-slate-500 mt-1">Giải pháp bảo mật nhiều lớp, an toàn dữ liệu</p>
                        </div>
                    </div>
                    <!-- Item 4 -->
                    <div class="flex items-start gap-3 w-full sm:w-[45%] lg:w-1/4 lg:border-l lg:border-slate-200 lg:pl-6 group">
                        <i class="ph-duotone ph-phone-call text-4xl text-[#1d4ed8] group-hover:scale-110 transition-transform"></i>
                        <div class="mt-1">
                            <h4 class="text-xs font-bold text-slate-900 uppercase">HỖ TRỢ 24/7</h4>
                            <p class="text-[11px] text-slate-500 mt-1">Đội ngũ kỹ thuật chuyên nghiệp, sẵn sàng hỗ trợ</p>
                        </div>
                    </div>
                </div>

            </div>
        </section>"""

if re.search(services_pattern, content, flags=re.DOTALL):
    content = re.sub(services_pattern, new_services_html, content, flags=re.DOTALL)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Ecosystem section updated successfully.")
else:
    print("Could not find the services section.")
