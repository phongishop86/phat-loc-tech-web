const PricingFlatWidget = {
    init() {
        const container = document.getElementById('pricing-container-flat');
        if (!container) return;

        this.container = container;
        this.dataSource = container.getAttribute('data-source');
        this.data = null;
        this.flatItems = [];
        this.searchQuery = '';

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
            const cacheBuster = new Date().getTime();
            const response = await fetch(`${this.dataSource}?v=${cacheBuster}`);
            this.data = await response.json();
            
            // Flatten all items
            this.flatItems = [];
            for (const cat in this.data) {
                for (const item of this.data[cat]) {
                    this.flatItems.push({...item, category: cat});
                }
            }
            
            this.render();
        } catch (error) {
            console.error('Error fetching pricing data:', error);
            this.container.innerHTML = `<div class="text-center text-red-500 py-10">Lỗi tải bảng giá. Vui lòng thử lại sau.</div>`;
        }
    },

    render() {
        if (!this.flatItems) return;

        let filteredItems = this.flatItems;
        if (this.searchQuery) {
            const q = this.searchQuery.toLowerCase();
            filteredItems = filteredItems.filter(item => item.name.toLowerCase().includes(q) || item.category.toLowerCase().includes(q));
        }

        const displayItems = filteredItems;
        const showingText = this.searchQuery 
            ? `Tìm thấy ${filteredItems.length} kết quả` 
            : `Đang hiển thị toàn bộ ${this.flatItems.length} sản phẩm`;

        const tableRows = displayItems.length > 0 ? displayItems.map(item => `
            <tr class="hover:bg-zinc-800/50 transition-colors border-b border-zinc-800/50 last:border-0 group flex flex-col sm:table-row p-3 sm:p-0">
                <td class="p-2 sm:p-4 text-zinc-200 group-hover:text-white transition-colors block sm:table-cell font-semibold sm:font-normal text-base sm:text-sm">
                    ${item.name}
                    <div class="text-xs text-zinc-500 mt-1 sm:hidden">${item.category}</div>
                </td>
                <td class="hidden lg:table-cell p-2 sm:p-4 text-left sm:text-center text-zinc-500 text-xs">
                    <span class="bg-zinc-800 px-2 py-1 rounded-md">${item.category}</span>
                </td>
                <td class="p-2 sm:p-4 text-left sm:text-center text-zinc-500 flex sm:table-cell justify-between items-center text-sm border-t border-zinc-800/50 sm:border-0 mt-2 sm:mt-0 pt-2 sm:pt-4">
                    <span class="sm:hidden font-semibold text-zinc-400 text-xs">Bảo hành:</span>
                    <span>${item.warranty}</span>
                </td>
                <td class="p-2 sm:p-4 text-left sm:text-right font-medium text-brand-green flex sm:table-cell justify-between items-center text-base sm:text-sm">
                    <span class="sm:hidden font-semibold text-zinc-400 text-xs">Đơn giá:</span>
                    <span class="font-bold sm:font-medium">${typeof item.price === 'number' && item.price > 0 ? item.price.toLocaleString('vi-VN') + ' đ' : (item.price || 'Liên hệ')}</span>
                </td>
                <td class="p-2 sm:p-4 text-right sm:text-center block sm:table-cell mt-3 sm:mt-0">
                    <button data-action="add-cart" data-name="${item.name.replace(/"/g, '&quot;')}" data-price="${item.price}" data-warranty="${item.warranty}" class="w-full sm:w-auto text-zinc-300 sm:text-zinc-500 hover:text-white sm:hover:text-brand-green bg-brand-green/20 hover:bg-brand-green/40 sm:bg-zinc-900 sm:hover:bg-zinc-800 p-2.5 sm:p-2 rounded-lg transition-colors border border-brand-green/30 sm:border-zinc-800 hover:border-brand-green sm:hover:border-brand-green/50 group-hover:shadow-[0_0_15px_rgba(16,185,129,0.2)] flex items-center justify-center gap-2" title="Thêm vào giỏ hàng">
                        <svg class="w-5 h-5 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                        <span class="sm:hidden text-sm font-bold pointer-events-none">Thêm vào giỏ</span>
                    </button>
                </td>
            </tr>
        `).join('') : `<tr><td colspan="5" class="p-8 text-center text-zinc-500">Không tìm thấy sản phẩm nào phù hợp.</td></tr>`;

        this.container.innerHTML = `
            <div class="py-4 bg-zinc-950/30" id="pricing-table">
                <div class="container mx-auto px-4 max-w-7xl">
                    <div class="w-full">
                        <div class="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 mb-6 lg:mb-8 shadow-xl relative overflow-hidden">
                            <div class="absolute top-0 right-0 w-32 h-32 bg-brand-green/10 blur-[50px] rounded-full pointer-events-none"></div>
                            
                            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 relative z-10">
                                <div>
                                    <h2 class="text-2xl font-bold text-white mb-2 flex items-center gap-2">
                                        <svg class="w-6 h-6 text-brand-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                                        Báo Giá Tất Cả Sản Phẩm
                                    </h2>
                                    <p class="text-sm text-zinc-400">${showingText}</p>
                                </div>
                                <div class="relative w-full md:w-80 shrink-0">
                                    <input type="text" 
                                        placeholder="Tìm kiếm ${this.flatItems.length} sản phẩm..." 
                                        class="w-full bg-zinc-950 border border-zinc-700 text-white text-sm rounded-xl pl-10 pr-4 py-3 focus:outline-none focus:border-brand-green focus:ring-1 focus:ring-brand-green transition-all"
                                        value="${this.searchQuery}"
                                        onkeyup="PricingFlatWidget.setSearch(this.value)"
                                    >
                                    <svg class="w-4 h-4 text-zinc-500 absolute left-3.5 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                                </div>
                            </div>
                        </div>

                        <div class="bg-zinc-900/50 border border-zinc-800/80 rounded-2xl overflow-hidden shadow-2xl backdrop-blur-sm">
                            <div class="overflow-x-auto">
                                <table class="w-full text-left border-collapse min-w-[300px]">
                                    <thead>
                                        <tr class="bg-zinc-950/80 text-zinc-400 text-xs uppercase tracking-wider hidden sm:table-row border-b border-zinc-800">
                                            <th class="p-4 font-semibold">Tên sản phẩm</th>
                                            <th class="hidden lg:table-cell p-4 font-semibold text-center">Danh mục</th>
                                            <th class="p-4 font-semibold text-center w-24">Bảo hành</th>
                                            <th class="p-4 font-semibold text-right w-32">Đơn giá</th>
                                            <th class="p-4 font-semibold text-center w-20">Đặt hàng</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-zinc-800/30">
                                        ${tableRows}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    },

    setSearch(query) {
        this.searchQuery = query;
        this.render();
    }
};

document.addEventListener('DOMContentLoaded', () => {
    PricingFlatWidget.init();
});
