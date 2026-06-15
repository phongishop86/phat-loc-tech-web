import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find everything from <!-- Hero Section --> to just before <!-- Partner Brands Section -->
pattern = r'(<!-- Hero Section -->.*?)(?=<!-- Partner Brands Section -->)'

new_hero_and_nav = """<!-- Top Navigation Bar -->
    <nav class="w-full bg-white border-b border-slate-200 z-50 relative">
        <div class="max-w-[1400px] mx-auto px-6 h-20 flex items-center justify-between">
            <!-- Left: Logo -->
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center">
                    <img src="PLT-Logo-final-transparent.png" alt="Phát Lộc Tech" class="w-full h-full object-contain mix-blend-multiply" />
                </div>
                <span class="text-[#0f172a] font-bold text-xl tracking-tight">Phát Lộc Tech</span>
            </div>

            <!-- Center: Links (Hidden on Mobile) -->
            <div class="hidden lg:flex items-center gap-8">
                <a href="#" class="text-slate-800 font-medium text-sm hover:text-blue-600 transition">Trang chủ</a>
                <a href="#services" class="text-slate-600 font-medium text-sm hover:text-blue-600 transition">Giải pháp CNTT</a>
                <a href="#" class="text-slate-600 font-medium text-sm hover:text-blue-600 transition">Tra cứu báo giá</a>
                <a href="#" class="text-slate-600 font-medium text-sm hover:text-blue-600 transition">Dự án</a>
                <a href="#" class="text-slate-600 font-medium text-sm hover:text-blue-600 transition">Tin tức</a>
            </div>

            <!-- Right: Contact -->
            <div class="hidden lg:flex items-center gap-6">
                <div class="text-right">
                    <p class="text-xs text-slate-500 mb-0.5">Hotline 24/7</p>
                    <p class="text-sm font-bold text-blue-900">0932 685 794</p>
                </div>
                <a href="tel:0932685794" class="bg-blue-800 hover:bg-blue-700 text-white font-semibold text-sm px-6 py-2.5 rounded shadow-lg transition">Nhận tư vấn</a>
            </div>
            
            <!-- Mobile Menu Button -->
            <button class="lg:hidden text-slate-800 text-2xl">
                <i class="ph ph-list"></i>
            </button>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative w-full h-[600px] lg:h-[750px] flex items-center justify-start overflow-hidden bg-slate-900">
        <!-- Background Image with Overlay -->
        <div class="absolute inset-0 z-0">
            <!-- Server rack image from Unsplash -->
            <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=2034&auto=format&fit=crop" alt="Server Data Center" class="w-full h-full object-cover opacity-40 mix-blend-luminosity" />
            <div class="absolute inset-0 bg-gradient-to-r from-[#03132e] via-[#041a3f]/90 to-transparent"></div>
        </div>

        <!-- Content -->
        <div class="max-w-[1400px] mx-auto px-6 relative z-10 w-full pt-10">
            <div class="max-w-3xl">
                <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-white font-[var(--font-oswald)] uppercase leading-[1.1] tracking-wide mb-2">
                    KIẾN TẠO HẠ TẦNG SỐ,
                </h1>
                <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-[#0ea5e9] font-[var(--font-oswald)] uppercase leading-[1.1] tracking-wide mb-8">
                    NÂNG TẦM DOANH NGHIỆP
                </h1>
                
                <p class="text-slate-300 text-sm md:text-base lg:text-lg leading-relaxed mb-10 max-w-2xl font-medium">
                    Hệ sinh thái công nghệ toàn diện: từ máy tính chuyên dụng, hệ thống giám sát an ninh đến quản trị mạng và phần mềm bản quyền, đáp ứng khắt khe mọi quy mô.
                </p>

                <div class="flex flex-wrap items-center gap-4 mb-20">
                    <a href="#services" class="bg-[#ea580c] hover:bg-[#c2410c] text-white font-bold text-sm lg:text-base px-8 py-3.5 rounded shadow-[0_0_20px_rgba(234,88,12,0.4)] transition">
                        Nhận tư vấn ngay
                    </a>
                    <a href="#about" class="bg-transparent border border-slate-500 hover:border-slate-300 text-white font-semibold text-sm lg:text-base px-8 py-3.5 rounded transition">
                        Tìm hiểu thêm
                    </a>
                </div>

                <!-- 4 Bottom Features -->
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 pt-8 border-t border-slate-700/50">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-blue-900/50 border border-blue-700 flex items-center justify-center shrink-0">
                            <i class="ph-duotone ph-shield-check text-[#38bdf8] text-xl"></i>
                        </div>
                        <span class="text-white text-xs lg:text-sm font-bold">Giải Pháp Toàn Diện</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-blue-900/50 border border-blue-700 flex items-center justify-center shrink-0">
                            <i class="ph-duotone ph-check-circle text-[#38bdf8] text-xl"></i>
                        </div>
                        <span class="text-white text-xs lg:text-sm font-bold">Sản Phẩm Chính Hãng</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-blue-900/50 border border-blue-700 flex items-center justify-center shrink-0">
                            <i class="ph-duotone ph-headset text-[#38bdf8] text-xl"></i>
                        </div>
                        <span class="text-white text-xs lg:text-sm font-bold">Hỗ Trợ 24/7</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-blue-900/50 border border-blue-700 flex items-center justify-center shrink-0">
                            <i class="ph-duotone ph-trend-up text-[#38bdf8] text-xl"></i>
                        </div>
                        <span class="text-white text-xs lg:text-sm font-bold">Tối Ưu Hiệu Quả</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

if re.search(pattern, content, flags=re.DOTALL):
    content = re.sub(pattern, new_hero_and_nav, content, flags=re.DOTALL)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Hero section updated successfully.")
else:
    print("Could not find the target Hero section.")
