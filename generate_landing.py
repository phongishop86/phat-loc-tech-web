import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The hero section starts with <!-- Hero Section --> and ends before <!-- Partner Brands Section -->
pattern = r'<!-- Hero Section -->.*?<!-- Partner Brands Section -->'

new_hero = """<!-- Hero Section -->
        <section class="relative min-h-screen flex flex-col pt-8 pb-16 overflow-hidden bg-gradient-to-b from-[#e0f2fe] via-[#bae6fd] to-white font-sans">
            <!-- Background Glows -->
            <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
                <div class="absolute top-0 right-1/4 w-[600px] h-[600px] rounded-full bg-white/40 blur-[120px]"></div>
                <div class="absolute bottom-1/4 left-1/4 w-[500px] h-[500px] rounded-full bg-blue-300/20 blur-[100px]"></div>
            </div>
            
            <div class="container mx-auto px-6 relative z-10 max-w-[1400px]">
                
                <!-- Header (Logo) -->
                <div class="flex items-center gap-4 mb-16 fade-in-up">
                    <div class="relative flex items-center justify-center w-16 h-16 bg-white rounded-full shadow-[0_8px_30px_rgba(29,78,216,0.2)] border border-blue-50">
                        <div class="flex flex-col items-center leading-none">
                            <span class="text-xl font-black text-[#f97316] -mb-1">PL</span>
                            <span class="text-xl font-black text-[#1d4ed8]">T</span>
                        </div>
                    </div>
                    <div>
                        <h1 class="text-2xl md:text-3xl font-black text-[#0f172a] tracking-wider leading-none">PHÁT LỘC TECH</h1>
                        <p class="text-xs md:text-sm font-bold text-slate-500 mt-1 uppercase tracking-widest">GIẢI PHÁP CÔNG NGHỆ TOÀN DIỆN</p>
                    </div>
                </div>

                <!-- Main Content Grid -->
                <div class="grid lg:grid-cols-2 gap-12 items-center mb-16">
                    <!-- Left Side (Text & Features) -->
                    <div class="flex flex-col items-start text-left z-20">
                        <h2 class="font-[var(--font-oswald)] text-5xl md:text-6xl lg:text-[72px] font-bold text-[#0f172a] leading-[1.1] tracking-tight uppercase mb-6 drop-shadow-sm fade-in-up delay-100">
                            KIẾN TẠO <span class="text-[#1d4ed8]">HẠ TẦNG SỐ,</span><br/>
                            NÂNG TẦM <span class="text-[#1d4ed8]">DOANH NGHIỆP</span>
                        </h2>
                        <p class="text-lg md:text-xl text-slate-700 max-w-xl mb-12 font-medium leading-relaxed fade-in-up delay-200">
                            Hệ sinh thái công nghệ toàn diện: từ máy tính chuyên dụng, hệ thống giám sát an ninh đến quản trị mạng và phần mềm bản quyền, đáp ứng khắt khe mọi quy mô.
                        </p>

                        <!-- 4 Features Grid -->
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 w-full fade-in-up delay-300">
                            <!-- Feature 1 -->
                            <div class="flex flex-col items-center text-center bg-white/70 backdrop-blur-md p-5 rounded-2xl shadow-lg border border-white hover:-translate-y-1 transition duration-300">
                                <i class="ph-duotone ph-shield-check text-4xl text-[#1d4ed8] mb-3"></i>
                                <h3 class="text-[13px] font-bold text-slate-900 mb-2 uppercase leading-tight">GIẢI PHÁP<br/>TOÀN DIỆN</h3>
                                <p class="text-[11px] text-slate-600 leading-snug">Đáp ứng mọi nhu cầu công nghệ doanh nghiệp</p>
                            </div>
                            <!-- Feature 2 -->
                            <div class="flex flex-col items-center text-center bg-white/70 backdrop-blur-md p-5 rounded-2xl shadow-lg border border-white hover:-translate-y-1 transition duration-300">
                                <i class="ph-duotone ph-medal text-4xl text-[#1d4ed8] mb-3"></i>
                                <h3 class="text-[13px] font-bold text-slate-900 mb-2 uppercase leading-tight">SẢN PHẨM<br/>CHÍNH HÃNG</h3>
                                <p class="text-[11px] text-slate-600 leading-snug">Chất lượng đảm bảo, xuất xứ rõ ràng</p>
                            </div>
                            <!-- Feature 3 -->
                            <div class="flex flex-col items-center text-center bg-white/70 backdrop-blur-md p-5 rounded-2xl shadow-lg border border-white hover:-translate-y-1 transition duration-300">
                                <i class="ph-duotone ph-headset text-4xl text-[#1d4ed8] mb-3"></i>
                                <h3 class="text-[13px] font-bold text-slate-900 mb-2 uppercase leading-tight">HỖ TRỢ<br/>24/7</h3>
                                <p class="text-[11px] text-slate-600 leading-snug">Đội ngũ kỹ thuật chuyên nghiệp, sẵn sàng đồng hành</p>
                            </div>
                            <!-- Feature 4 -->
                            <div class="flex flex-col items-center text-center bg-white/70 backdrop-blur-md p-5 rounded-2xl shadow-lg border border-white hover:-translate-y-1 transition duration-300">
                                <i class="ph-duotone ph-trend-up text-4xl text-[#1d4ed8] mb-3"></i>
                                <h3 class="text-[13px] font-bold text-slate-900 mb-2 uppercase leading-tight">TỐI ƯU<br/>HIỆU QUẢ</h3>
                                <p class="text-[11px] text-slate-600 leading-snug">Giải pháp tối ưu chi phí, hiệu suất vượt trội</p>
                            </div>
                        </div>
                    </div>

                    <!-- Right Side Diagram (CSS based) -->
                    <div class="relative w-full h-[600px] hidden lg:flex items-center justify-center z-10 fade-in-up delay-400">
                        <!-- Connecting Lines (SVG) -->
                        <svg class="absolute inset-0 w-full h-full" style="z-index: 1;">
                            <path d="M300 400 Q 150 400 150 250" fill="none" stroke="#60a5fa" stroke-width="3" stroke-dasharray="6 6" class="animate-pulse"/>
                            <path d="M300 400 Q 150 400 150 550" fill="none" stroke="#60a5fa" stroke-width="3" stroke-dasharray="6 6" class="animate-pulse"/>
                            <path d="M300 400 Q 500 400 500 250" fill="none" stroke="#60a5fa" stroke-width="3" stroke-dasharray="6 6" class="animate-pulse"/>
                            <path d="M300 400 Q 500 400 500 550" fill="none" stroke="#60a5fa" stroke-width="3" stroke-dasharray="6 6" class="animate-pulse"/>
                        </svg>

                        <!-- Center Logo -->
                        <div class="absolute top-[400px] left-[300px] -translate-x-1/2 -translate-y-1/2 z-20 w-32 h-32 bg-white rounded-full shadow-[0_0_50px_rgba(29,78,216,0.5)] border-8 border-blue-500 flex items-center justify-center">
                            <div class="flex flex-col items-center leading-none">
                                <span class="text-4xl font-black text-[#f97316] -mb-2">PL</span>
                                <span class="text-4xl font-black text-[#1d4ed8]">T</span>
                            </div>
                        </div>

                        <!-- Main Cloud/Server Illustration -->
                        <div class="absolute top-[200px] left-[300px] -translate-x-1/2 -translate-y-1/2 z-10 flex flex-col items-center">
                            <i class="ph-fill ph-cloud text-[160px] text-blue-500 drop-shadow-[0_20px_50px_rgba(59,130,246,0.6)] relative -mb-10 z-20"></i>
                            <div class="flex gap-2 relative z-10">
                                <div class="w-16 h-40 bg-slate-800 rounded-lg shadow-2xl border-t border-slate-600 flex flex-col justify-around p-2">
                                    <div class="w-full h-2 bg-blue-500 rounded animate-pulse"></div>
                                    <div class="w-full h-2 bg-slate-700 rounded"></div>
                                    <div class="w-full h-2 bg-blue-500 rounded animate-pulse"></div>
                                </div>
                                <div class="w-20 h-48 bg-slate-900 rounded-lg shadow-2xl border-t border-slate-700 flex flex-col justify-around p-2 -mt-4 relative z-20">
                                    <div class="w-full h-3 bg-blue-400 rounded animate-pulse"></div>
                                    <div class="w-full h-3 bg-blue-500 rounded"></div>
                                    <div class="w-full h-3 bg-blue-400 rounded animate-pulse"></div>
                                    <div class="w-full h-3 bg-slate-800 rounded"></div>
                                </div>
                                <div class="w-16 h-40 bg-slate-800 rounded-lg shadow-2xl border-t border-slate-600 flex flex-col justify-around p-2">
                                    <div class="w-full h-2 bg-blue-500 rounded animate-pulse"></div>
                                    <div class="w-full h-2 bg-slate-700 rounded"></div>
                                    <div class="w-full h-2 bg-blue-500 rounded animate-pulse"></div>
                                </div>
                            </div>
                        </div>

                        <!-- Node 1: MÁY TÍNH -->
                        <div class="absolute top-[250px] left-[150px] -translate-x-1/2 -translate-y-1/2 z-30 bg-white/90 backdrop-blur-xl p-5 rounded-2xl shadow-xl border border-blue-100 w-64 hover:scale-105 transition">
                            <div class="absolute -top-6 left-1/2 -translate-x-1/2 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center border border-blue-50">
                                <i class="ph-duotone ph-desktop text-2xl text-[#1d4ed8]"></i>
                            </div>
                            <h4 class="text-[13px] font-bold text-[#1d4ed8] mb-1 uppercase mt-4 text-center">MÁY TÍNH CHUYÊN DỤNG</h4>
                            <p class="text-[11px] text-slate-600 text-center leading-relaxed">Cung cấp máy tính, laptop, workstation và thiết bị chính hãng cho doanh nghiệp.</p>
                        </div>

                        <!-- Node 2: QUẢN TRỊ MẠNG -->
                        <div class="absolute top-[550px] left-[150px] -translate-x-1/2 -translate-y-1/2 z-30 bg-white/90 backdrop-blur-xl p-5 rounded-2xl shadow-xl border border-blue-100 w-64 hover:scale-105 transition">
                            <div class="absolute -top-6 left-1/2 -translate-x-1/2 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center border border-blue-50">
                                <i class="ph-duotone ph-router text-2xl text-[#1d4ed8]"></i>
                            </div>
                            <h4 class="text-[13px] font-bold text-[#1d4ed8] mb-1 uppercase mt-4 text-center">QUẢN TRỊ MẠNG</h4>
                            <p class="text-[11px] text-slate-600 text-center leading-relaxed">Thiết kế và triển khai hệ thống mạng LAN, WiFi, Firewall, Server chuyên nghiệp.</p>
                        </div>

                        <!-- Node 3: CAMERA GIÁM SÁT -->
                        <div class="absolute top-[250px] left-[500px] -translate-x-1/2 -translate-y-1/2 z-30 bg-white/90 backdrop-blur-xl p-5 rounded-2xl shadow-xl border border-blue-100 w-64 hover:scale-105 transition">
                            <div class="absolute -top-6 left-1/2 -translate-x-1/2 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center border border-blue-50">
                                <i class="ph-duotone ph-video-camera text-2xl text-[#1d4ed8]"></i>
                            </div>
                            <h4 class="text-[13px] font-bold text-[#1d4ed8] mb-1 uppercase mt-4 text-center">CAMERA GIÁM SÁT</h4>
                            <p class="text-[11px] text-slate-600 text-center leading-relaxed">Thi công và lắp đặt hệ thống camera giám sát chất lượng cao cho mọi mô hình.</p>
                        </div>

                        <!-- Node 4: PHẦN MỀM -->
                        <div class="absolute top-[550px] left-[500px] -translate-x-1/2 -translate-y-1/2 z-30 bg-white/90 backdrop-blur-xl p-5 rounded-2xl shadow-xl border border-blue-100 w-64 hover:scale-105 transition">
                            <div class="absolute -top-6 left-1/2 -translate-x-1/2 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center border border-blue-50">
                                <i class="ph-duotone ph-app-window text-2xl text-[#1d4ed8]"></i>
                            </div>
                            <h4 class="text-[13px] font-bold text-[#1d4ed8] mb-1 uppercase mt-4 text-center">PHẦN MỀM BẢN QUYỀN</h4>
                            <p class="text-[11px] text-slate-600 text-center leading-relaxed">Cung cấp phần mềm bản quyền, giải pháp quản lý và chuyển đổi số cho doanh nghiệp.</p>
                        </div>
                    </div>
                </div>
                
                <!-- Bottom Dark Section (TRANG THIẾT BỊ) -->
                <div class="w-full bg-[#0a192f] rounded-[40px] mt-24 p-8 md:p-12 shadow-2xl relative">
                    <!-- Title Badge -->
                    <div class="absolute -top-6 left-1/2 -translate-x-1/2 bg-gradient-to-r from-blue-600 to-blue-500 px-10 py-3 rounded-full shadow-lg border-4 border-white">
                        <h3 class="text-lg md:text-xl font-[var(--font-oswald)] font-bold text-white uppercase tracking-widest">TRANG THIẾT BỊ</h3>
                    </div>

                    <!-- 5 Equipment Cards Grid -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6 mt-8">
                        <!-- Card 1 -->
                        <div class="bg-white rounded-2xl p-6 shadow-lg flex flex-col hover:-translate-y-2 transition duration-300">
                            <h4 class="text-sm font-bold text-[#1d4ed8] uppercase mb-2 text-center border-b border-blue-100 pb-2">THIẾT BỊ MẠNG</h4>
                            <p class="text-[11px] text-slate-600 text-center mb-6 leading-relaxed flex-1">Switch, Router, WiFi, Firewall, Access Point...</p>
                            <div class="w-full h-24 bg-blue-50 rounded-xl flex items-center justify-center">
                                <i class="ph-duotone ph-plugs-connected text-5xl text-[#1d4ed8]"></i>
                            </div>
                        </div>
                        <!-- Card 2 -->
                        <div class="bg-white rounded-2xl p-6 shadow-lg flex flex-col hover:-translate-y-2 transition duration-300">
                            <h4 class="text-sm font-bold text-[#1d4ed8] uppercase mb-2 text-center border-b border-blue-100 pb-2">THIẾT BỊ LƯU TRỮ</h4>
                            <p class="text-[11px] text-slate-600 text-center mb-6 leading-relaxed flex-1">NAS, Server, HDD, SSD, Thiết bị backup...</p>
                            <div class="w-full h-24 bg-blue-50 rounded-xl flex items-center justify-center">
                                <i class="ph-duotone ph-hard-drives text-5xl text-[#1d4ed8]"></i>
                            </div>
                        </div>
                        <!-- Card 3 -->
                        <div class="bg-white rounded-2xl p-6 shadow-lg flex flex-col hover:-translate-y-2 transition duration-300">
                            <h4 class="text-sm font-bold text-[#1d4ed8] uppercase mb-2 text-center border-b border-blue-100 pb-2">THIẾT BỊ AN NINH</h4>
                            <p class="text-[11px] text-slate-600 text-center mb-6 leading-relaxed flex-1">Camera, Đầu ghi, Chuông cửa, Báo động...</p>
                            <div class="w-full h-24 bg-blue-50 rounded-xl flex items-center justify-center">
                                <i class="ph-duotone ph-cctv text-5xl text-[#1d4ed8]"></i>
                            </div>
                        </div>
                        <!-- Card 4 -->
                        <div class="bg-white rounded-2xl p-6 shadow-lg flex flex-col hover:-translate-y-2 transition duration-300">
                            <h4 class="text-sm font-bold text-[#1d4ed8] uppercase mb-2 text-center border-b border-blue-100 pb-2">THIẾT BỊ VĂN PHÒNG</h4>
                            <p class="text-[11px] text-slate-600 text-center mb-6 leading-relaxed flex-1">Máy in, Máy chiếu, Máy scan, UPS...</p>
                            <div class="w-full h-24 bg-blue-50 rounded-xl flex items-center justify-center">
                                <i class="ph-duotone ph-printer text-5xl text-[#1d4ed8]"></i>
                            </div>
                        </div>
                        <!-- Card 5 -->
                        <div class="bg-white rounded-2xl p-6 shadow-lg flex flex-col hover:-translate-y-2 transition duration-300">
                            <h4 class="text-sm font-bold text-[#1d4ed8] uppercase mb-2 text-center border-b border-blue-100 pb-2">LINH KIỆN & PHỤ KIỆN</h4>
                            <p class="text-[11px] text-slate-600 text-center mb-6 leading-relaxed flex-1">CPU, RAM, SSD, Mainboard, Nguồn, Case, Phụ kiện...</p>
                            <div class="w-full h-24 bg-blue-50 rounded-xl flex items-center justify-center">
                                <i class="ph-duotone ph-cpu text-5xl text-[#1d4ed8]"></i>
                            </div>
                        </div>
                    </div>

                    <!-- 4 Footer Features -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 mt-12 pt-12 border-t border-slate-700/50">
                        <!-- Feature 1 -->
                        <div class="flex items-start gap-4">
                            <i class="ph-duotone ph-shield-check text-4xl text-[#3b82f6]"></i>
                            <div>
                                <h4 class="text-sm font-bold text-white uppercase mb-1">ĐA DẠNG THƯƠNG HIỆU</h4>
                                <p class="text-[11px] text-slate-400 leading-relaxed">Phân phối chính hãng từ các thương hiệu uy tín.</p>
                            </div>
                        </div>
                        <!-- Feature 2 -->
                        <div class="flex items-start gap-4">
                            <i class="ph-duotone ph-currency-circle-dollar text-4xl text-[#3b82f6]"></i>
                            <div>
                                <h4 class="text-sm font-bold text-white uppercase mb-1">GIÁ CẢ CẠNH TRANH</h4>
                                <p class="text-[11px] text-slate-400 leading-relaxed">Tối ưu chi phí, hiệu quả đầu tư cao.</p>
                            </div>
                        </div>
                        <!-- Feature 3 -->
                        <div class="flex items-start gap-4">
                            <i class="ph-duotone ph-shield-plus text-4xl text-[#3b82f6]"></i>
                            <div>
                                <h4 class="text-sm font-bold text-white uppercase mb-1">BẢO HÀNH CHUYÊN NGHIỆP</h4>
                                <p class="text-[11px] text-slate-400 leading-relaxed">Bảo hành tận nơi, hỗ trợ nhanh chóng.</p>
                            </div>
                        </div>
                        <!-- Feature 4 -->
                        <div class="flex items-start gap-4">
                            <i class="ph-duotone ph-handshake text-4xl text-[#3b82f6]"></i>
                            <div>
                                <h4 class="text-sm font-bold text-white uppercase mb-1">ĐỒNG HÀNH LÂU DÀI</h4>
                                <p class="text-[11px] text-slate-400 leading-relaxed">Cam kết chất lượng, hợp tác bền vững.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Partner Brands Section -->"""

if re.search(pattern, content, flags=re.DOTALL):
    content = re.sub(pattern, new_hero, content, flags=re.DOTALL)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced Hero section with the new HTML structure.")
else:
    print("Could not find the target pattern.")
