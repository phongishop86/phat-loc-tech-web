import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Google Maps in Hero Section with Enterprise IT Hero Illustration
map_pattern = r'<!-- Google Maps Location Right Side -->.*?</div>\s*</div>'

hero_illustration = """<!-- Enterprise Hero Illustration Right Side -->
                <div class="relative hidden lg:flex items-center justify-center z-20">
                    <div class="w-full max-w-[500px] aspect-square relative">
                        <!-- Abstract Enterprise Nodes -->
                        <div class="absolute inset-0 bg-blue-50/20 rounded-full animate-pulse blur-3xl"></div>
                        <svg viewBox="0 0 400 400" class="w-full h-full relative z-10 drop-shadow-xl" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <!-- Network lines -->
                            <path d="M200 200L100 100M200 200L300 100M200 200L100 300M200 200L300 300M200 200L200 60M200 200L60 200" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="6 6"/>
                            <!-- Center Node -->
                            <circle cx="200" cy="200" r="40" fill="white" stroke="#2563EB" stroke-width="8"/>
                            <text x="200" y="206" font-family="Inter, sans-serif" font-weight="900" font-size="20" fill="#0F172A" text-anchor="middle">PLT</text>
                            
                            <!-- Peripheral Nodes -->
                            <circle cx="100" cy="100" r="25" fill="#F8FAFC" stroke="#06B6D4" stroke-width="4"/>
                            <circle cx="300" cy="100" r="25" fill="#F8FAFC" stroke="#10B981" stroke-width="4"/>
                            <circle cx="100" cy="300" r="25" fill="#F8FAFC" stroke="#8B5CF6" stroke-width="4"/>
                            <circle cx="300" cy="300" r="25" fill="#F8FAFC" stroke="#F59E0B" stroke-width="4"/>
                            <circle cx="200" cy="60" r="20" fill="#F8FAFC" stroke="#3B82F6" stroke-width="4"/>
                            <circle cx="60" cy="200" r="20" fill="#F8FAFC" stroke="#EC4899" stroke-width="4"/>
                            
                            <!-- Decorative orbits -->
                            <circle cx="200" cy="200" r="140" stroke="#E2E8F0" stroke-width="1" fill="none" stroke-dasharray="10 10"/>
                        </svg>
                    </div>
                </div>"""

content = re.sub(map_pattern, hero_illustration, content, flags=re.DOTALL)

# 2. Replace Old "Hệ Sinh Thái Dịch Vụ" with New "Hệ Sinh Thái Giải Pháp"
old_services_pattern = r'<section id="services".*?<!-- Service 4 -->.*?</a>\s*</div>\s*</div>\s*</section>'

new_solutions_section = """<section id="services" class="w-full bg-slate-50 py-32 border-b border-slate-200 relative overflow-hidden">
        <!-- Background depth -->
        <div class="absolute top-0 inset-x-0 h-px bg-gradient-to-r from-transparent via-slate-300 to-transparent"></div>
        <div class="absolute -top-40 -right-40 w-96 h-96 bg-blue-100/50 rounded-full blur-[100px] pointer-events-none"></div>
        
        <div class="container mx-auto px-4 max-w-7xl relative z-10">
            <div class="text-center mb-16 reveal">
                <span class="text-sm font-bold text-secondary tracking-wider uppercase mb-3 block">Enterprise IT Solutions</span>
                <h2 class="text-3xl md:text-5xl font-black text-primary mb-6 leading-tight">
                    Hệ sinh thái giải pháp <br/><span class="text-secondary">công nghệ toàn diện</span>
                </h2>
                <p class="text-slate-600 leading-relaxed max-w-2xl mx-auto text-lg">
                    Đồng hành cùng doanh nghiệp trong mọi nhu cầu về hạ tầng CNTT, bảo mật, giám sát và chuyển đổi số.
                </p>
            </div>
            
            <!-- Center Infographic: The Topology -->
            <div class="mb-20 reveal flex justify-center">
                <div class="w-full max-w-4xl relative">
                    <!-- Lines connecting the ecosystem -->
                    <div class="hidden md:block absolute top-1/2 left-0 right-0 h-0.5 bg-slate-300 -translate-y-1/2 z-0 border-t-2 border-dashed border-slate-300"></div>
                    <div class="hidden md:block absolute top-0 bottom-0 left-1/2 w-0.5 bg-slate-300 -translate-x-1/2 z-0 border-l-2 border-dashed border-slate-300"></div>
                    
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-center relative z-10">
                        
                        <!-- Left Node: Camera -->
                        <div class="flex flex-col items-center gap-3">
                            <div class="w-20 h-20 bg-white rounded-2xl shadow-lg border border-slate-200 flex items-center justify-center text-3xl text-brand-orange z-10 relative">
                                <i class="ph-duotone ph-webcam"></i>
                            </div>
                            <span class="font-bold text-slate-700 bg-white px-4 py-1 rounded-full border border-slate-200 shadow-sm">Camera</span>
                        </div>
                        
                        <!-- Center Node: PLT Core -->
                        <div class="flex flex-col items-center gap-0">
                            <div class="text-slate-500 font-bold mb-4 bg-white px-4 py-1 rounded-full border border-slate-200 shadow-sm z-10">Máy tính</div>
                            <div class="w-32 h-32 bg-white rounded-full shadow-2xl border-4 border-secondary flex items-center justify-center z-10 relative overflow-hidden group">
                                <div class="absolute inset-0 bg-blue-50 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                                <img src="logo.png" alt="Phát Lộc Tech" class="w-16 h-16 object-contain relative z-10"/>
                            </div>
                            <div class="text-slate-500 font-bold mt-4 bg-white px-4 py-1 rounded-full border border-slate-200 shadow-sm z-10">Phần mềm số hóa</div>
                        </div>
                        
                        <!-- Right Node: Hạ tầng mạng -->
                        <div class="flex flex-col items-center gap-3">
                            <div class="w-20 h-20 bg-white rounded-2xl shadow-lg border border-slate-200 flex items-center justify-center text-3xl text-brand-green z-10 relative">
                                <i class="ph-duotone ph-hard-drives"></i>
                            </div>
                            <span class="font-bold text-slate-700 bg-white px-4 py-1 rounded-full border border-slate-200 shadow-sm">Hạ tầng mạng</span>
                        </div>
                        
                    </div>
                </div>
            </div>

            <!-- 4 Solution Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 reveal">
                
                <!-- Card 1: Máy tính doanh nghiệp -->
                <div class="bg-white rounded-[20px] p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-2 hover:border-secondary transition-all duration-300 group relative overflow-hidden">
                    <div class="w-14 h-14 bg-slate-50 rounded-xl flex items-center justify-center text-3xl text-secondary mb-6 group-hover:bg-blue-50 group-hover:scale-110 transition-all border border-slate-100">
                        <i class="ph-duotone ph-desktop"></i>
                    </div>
                    <h3 class="text-xl font-bold text-primary mb-3">Máy tính doanh nghiệp</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">
                        Cung cấp máy tính, workstation, laptop và thiết bị văn phòng cho doanh nghiệp.
                    </p>
                    <div class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-secondary to-accent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                </div>

                <!-- Card 2: Camera giám sát -->
                <div class="bg-white rounded-[20px] p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-2 hover:border-secondary transition-all duration-300 group relative overflow-hidden">
                    <div class="w-14 h-14 bg-slate-50 rounded-xl flex items-center justify-center text-3xl text-secondary mb-6 group-hover:bg-blue-50 group-hover:scale-110 transition-all border border-slate-100">
                        <i class="ph-duotone ph-webcam"></i>
                    </div>
                    <h3 class="text-xl font-bold text-primary mb-3">Camera giám sát</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">
                        Thi công và bảo trì hệ thống camera cho văn phòng, nhà xưởng và cửa hàng.
                    </p>
                    <div class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-secondary to-accent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                </div>

                <!-- Card 3: Hạ tầng mạng -->
                <div class="bg-white rounded-[20px] p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-2 hover:border-secondary transition-all duration-300 group relative overflow-hidden">
                    <div class="w-14 h-14 bg-slate-50 rounded-xl flex items-center justify-center text-3xl text-secondary mb-6 group-hover:bg-blue-50 group-hover:scale-110 transition-all border border-slate-100">
                        <i class="ph-duotone ph-hard-drives"></i>
                    </div>
                    <h3 class="text-xl font-bold text-primary mb-3">Hạ tầng mạng</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">
                        Thiết kế và triển khai hệ thống mạng LAN, WiFi, Firewall và Server.
                    </p>
                    <div class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-secondary to-accent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                </div>

                <!-- Card 4: Phần mềm & số hóa -->
                <div class="bg-white rounded-[20px] p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-2 hover:border-secondary transition-all duration-300 group relative overflow-hidden">
                    <div class="w-14 h-14 bg-slate-50 rounded-xl flex items-center justify-center text-3xl text-secondary mb-6 group-hover:bg-blue-50 group-hover:scale-110 transition-all border border-slate-100">
                        <i class="ph-duotone ph-cloud-arrow-up"></i>
                    </div>
                    <h3 class="text-xl font-bold text-primary mb-3">Phần mềm & số hóa</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">
                        Hóa đơn điện tử, chữ ký số, phần mềm quản lý và chuyển đổi số.
                    </p>
                    <div class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-secondary to-accent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                </div>

            </div>
        </div>
    </section>"""

content = re.sub(old_services_pattern, new_solutions_section, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully replaced map and old services section with Enterprise UI.")
