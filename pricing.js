const PricingWidget = {
    init() {
        const container = document.getElementById('pricing-container');
        if (!container) return;

        this.container = container;
        this.dataSource = container.getAttribute('data-source');
        this.data = null;
        this.activeCategory = null;
        this.searchQuery = '';
        this.isMobileCategoryOpen = false;

        this.renderSkeleton();
        this.fetchData();
    },

    renderSkeleton() {
        this.container.innerHTML = `
            <div class="py-4 bg-zinc-950/30" id="pricing-table">
                <div class="container mx-auto px-4 max-w-6xl">
                    <div class="text-center mb-6">
                        <p class="text-zinc-400">Đang tải dữ liệu từ máy chủ...</p>
                        <div class="flex justify-center mt-6">
                            <div class="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-brand-green"></div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    },

    async fetchData() {
        try {
            // Thêm tham số timestamp để tránh bị trình duyệt lưu cache file JSON cũ
            const cacheBuster = new Date().getTime();
            const response = await fetch(`${this.dataSource}?v=${cacheBuster}`);
            this.data = await response.json();
            
            // Get first category as default
            this.activeCategory = Object.keys(this.data)[0];
            this.render();
        } catch (error) {
            console.error('Error fetching pricing data:', error);
            this.container.innerHTML = `<div class="text-center text-red-500 py-10">Lỗi tải bảng giá. Vui lòng thử lại sau.</div>`;
        }
    },

    render() {
        if (!this.data) return;

        const categories = Object.keys(this.data);
        
        let filteredItems = this.data[this.activeCategory];
        if (this.searchQuery) {
            const q = this.searchQuery.toLowerCase();
            filteredItems = filteredItems.filter(item => item.name.toLowerCase().includes(q));
        }

        const sidebarTabs = categories.map(cat => `
            <button onclick="PricingWidget.setCategory('${cat}')" 
                class="w-full text-left px-4 py-3 rounded-xl text-sm font-semibold transition-all duration-300 flex items-center justify-between group
                ${this.activeCategory === cat ? 'bg-brand-green/10 text-brand-green border border-brand-green/30 shadow-sm' : 'bg-transparent text-zinc-400 hover:bg-zinc-800 hover:text-white border border-transparent'}">
                <span>${cat}</span>
                <span class="text-xs px-2 py-1 rounded-full ${this.activeCategory === cat ? 'bg-brand-green/20 text-brand-green' : 'bg-zinc-800 text-zinc-500 group-hover:bg-zinc-700 group-hover:text-zinc-300'}">${this.data[cat].length}</span>
            </button>
        `).join('');

        const tableRows = filteredItems.length > 0 ? filteredItems.map(item => `
            <tr class="hover:bg-zinc-800/50 transition-colors border-b border-zinc-800/50 last:border-0 group flex flex-col sm:table-row p-3 sm:p-0">
                <td class="p-2 sm:p-4 text-zinc-200 group-hover:text-white transition-colors block sm:table-cell font-semibold sm:font-normal text-base sm:text-sm">${item.name}</td>
                <td class="p-2 sm:p-4 text-left sm:text-center text-zinc-500 flex sm:table-cell justify-between items-center text-sm border-t border-zinc-800/50 sm:border-0 mt-2 sm:mt-0 pt-2 sm:pt-4">
                    <span class="sm:hidden font-semibold text-zinc-400 text-xs">Bảo hành:</span>
                    <span>${item.warranty}</span>
                </td>
                <td class="p-2 sm:p-4 text-left sm:text-right font-medium text-brand-green flex sm:table-cell justify-between items-center text-base sm:text-sm">
                    <span class="sm:hidden font-semibold text-zinc-400 text-xs">Đơn giá:</span>
                    <span class="font-bold sm:font-medium">${item.price.toLocaleString('vi-VN')} đ</span>
                </td>
                <td class="p-2 sm:p-4 text-right sm:text-center block sm:table-cell mt-3 sm:mt-0">
                    <button data-action="add-cart" data-name="${item.name.replace(/"/g, '&quot;')}" data-price="${item.price}" data-warranty="${item.warranty}" class="w-full sm:w-auto text-zinc-300 sm:text-zinc-500 hover:text-white sm:hover:text-brand-green bg-brand-green/20 hover:bg-brand-green/40 sm:bg-zinc-900 sm:hover:bg-zinc-800 p-2.5 sm:p-2 rounded-lg transition-colors border border-brand-green/30 sm:border-zinc-800 hover:border-brand-green sm:hover:border-brand-green/50 group-hover:shadow-[0_0_15px_rgba(16,185,129,0.2)] flex items-center justify-center gap-2" title="Thêm vào giỏ hàng">
                        <svg class="w-5 h-5 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                        <span class="sm:hidden text-sm font-bold pointer-events-none">Thêm vào giỏ</span>
                    </button>
                </td>
            </tr>
        `).join('') : `<tr><td colspan="4" class="p-8 text-center text-zinc-500">Không tìm thấy sản phẩm nào phù hợp.</td></tr>`;

        this.container.innerHTML = `
            <div class="py-4 bg-zinc-950/30" id="pricing-table">
                <div class="container mx-auto px-4 max-w-7xl">
                    <div class="flex flex-col lg:flex-row gap-8">
                        <!-- Sidebar Category -->
                        <div class="w-full lg:w-1/4">
                            <div class="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 sticky top-24 shadow-xl">
                                <div class="flex items-center justify-between gap-3 mb-2 lg:mb-6 pb-2 lg:pb-4 border-b border-zinc-800 cursor-pointer lg:cursor-default" onclick="if(window.innerWidth < 1024) PricingWidget.toggleMobileCategory()">
                                    <div class="flex items-center gap-3">
                                        <svg class="w-5 h-5 text-brand-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"></path></svg>
                                        <h4 class="text-lg font-bold text-white tracking-wide">DANH MỤC</h4>
                                    </div>
                                    <button class="lg:hidden text-zinc-400 hover:text-white transition-transform ${this.isMobileCategoryOpen ? 'rotate-180' : ''}">
                                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                                    </button>
                                </div>
                                
                                ${!this.isMobileCategoryOpen ? `
                                <div class="lg:hidden text-brand-green/80 font-medium text-sm mt-1 mb-2">
                                    Đang xem: ${this.activeCategory} (${this.data[this.activeCategory]?.length || 0} SP)
                                </div>
                                ` : ''}

                                <div class="${this.isMobileCategoryOpen ? 'flex' : 'hidden'} lg:flex flex-col gap-2 max-h-[60vh] overflow-y-auto pr-1 mt-4 lg:mt-0" style="scrollbar-width: thin; scrollbar-color: #10b981 transparent;">
                                    ${sidebarTabs}
                                </div>
                            </div>
                        </div>

                        <!-- Main Content -->
                        <div class="w-full lg:w-3/4">
                            <!-- Search Bar -->
                            <div class="mb-6 relative">
                                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                    <svg class="h-5 w-5 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                                    </svg>
                                </div>
                                <input type="text" id="pricing-search" placeholder="Tìm kiếm tên thiết bị, linh kiện trong danh mục '${this.activeCategory}'..." 
                                    value="${this.searchQuery}"
                                    onkeyup="PricingWidget.handleSearch(event)"
                                    class="w-full pl-11 pr-4 py-3.5 bg-zinc-900 border border-zinc-800 rounded-xl text-white placeholder-zinc-500 focus:outline-none focus:border-brand-green focus:ring-1 focus:ring-brand-green transition-all shadow-inner">
                            </div>

                            <!-- Data Table -->
                            <div class="bg-zinc-900 border border-zinc-800 rounded-2xl overflow-hidden shadow-2xl">
                                <div class="overflow-y-auto overflow-x-hidden max-h-[700px] custom-scrollbar w-full">
                                    <table class="w-full text-left border-collapse relative block sm:table">
                                        <thead class="sticky top-0 z-10 hidden sm:table-header-group">
                                            <tr class="bg-zinc-950/95 backdrop-blur-sm text-zinc-400 text-sm uppercase tracking-wider shadow-md">
                                                <th class="p-4 font-semibold">Tên Thiết Bị / Linh Kiện</th>
                                                <th class="p-4 font-semibold text-center w-32">Bảo Hành</th>
                                                <th class="p-4 font-semibold text-right w-40">Đơn Giá (VNĐ)</th>
                                                <th class="p-4 font-semibold text-center w-16">Mua</th>
                                            </tr>
                                        </thead>
                                        <tbody class="text-sm bg-zinc-900 block sm:table-row-group">
                                            ${tableRows}
                                        </tbody>
                                    </table>
                                </div>
                            </div>

                            <!-- Mobile Sticky Back to Top -->
                            <div class="sticky bottom-6 flex justify-center mt-8 lg:hidden pointer-events-none">
                                <button onclick="PricingWidget.openMobileCategory()" 
                                    class="pointer-events-auto bg-zinc-900 border border-brand-green text-brand-green px-5 py-3 rounded-full font-bold shadow-[0_4px_20px_rgba(0,0,0,0.5)] flex items-center gap-2 hover:bg-brand-green hover:text-zinc-950 transition-colors z-50">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
                                    Chọn danh mục khác
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        // Re-focus search if it was active
        if (this.searchQuery) {
            const input = document.getElementById('pricing-search');
            if (input) {
                input.focus();
                // Move cursor to end
                const len = input.value.length;
                input.setSelectionRange(len, len);
            }
        }
    },

    setCategory(cat) {
        this.activeCategory = cat;
        this.searchQuery = ''; // Reset search on tab change
        this.isMobileCategoryOpen = false; // Đóng menu mobile khi đã chọn xong
        this.render();
        // Cuộn xuống bảng giá nếu đang trên mobile
        if (window.innerWidth < 1024) {
            document.getElementById('pricing-search')?.scrollIntoView({behavior: 'smooth', block: 'start'});
        }
    },

    toggleMobileCategory() {
        this.isMobileCategoryOpen = !this.isMobileCategoryOpen;
        this.render();
    },

    openMobileCategory() {
        this.isMobileCategoryOpen = true;
        this.render();
        document.getElementById('pricing-table')?.scrollIntoView({behavior: 'smooth', block: 'start'});
    },

    handleSearch(e) {
        this.searchQuery = e.target.value;
        this.render();
    }
};

// Handle Add to Cart click globally to avoid inline onclick escaping issues
document.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-action="add-cart"]');
    if (btn && (window.CartManager || typeof CartManager !== 'undefined')) {
        const cm = window.CartManager || CartManager;
        cm.addToCart(btn.dataset.name, btn.dataset.price, btn.dataset.warranty);
    }
});

document.addEventListener('DOMContentLoaded', () => {
    PricingWidget.init();
});
