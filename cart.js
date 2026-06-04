window.CartManager = {
    items: [],
    zaloNumber: '0932685794',
    
    init() {
        this.loadCart();
        this.renderFloatingButton();
        this.renderCartModal();
        this.updateUI();
    },

    loadCart() {
        const saved = localStorage.getItem('phatloc_cart');
        if (saved) {
            this.items = JSON.parse(saved);
        }
    },

    saveCart() {
        localStorage.setItem('phatloc_cart', JSON.stringify(this.items));
        this.updateUI();
    },

    addToCart(name, priceStr, warranty) {
        let price = 0;
        if (typeof priceStr === 'string') {
            price = parseInt(priceStr.replace(/[^\d]/g, '')) || 0;
        } else {
            price = priceStr || 0;
        }

        const existingItem = this.items.find(item => item.name === name);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            this.items.push({ name, price, warranty, quantity: 1 });
        }
        this.saveCart();
        this.showToast('Đã thêm vào giỏ hàng!');
    },

    updateQuantity(index, delta) {
        if (this.items[index]) {
            this.items[index].quantity += delta;
            if (this.items[index].quantity <= 0) {
                this.items.splice(index, 1);
            }
            this.saveCart();
        }
    },

    removeItem(index) {
        this.items.splice(index, 1);
        this.saveCart();
    },

    clearCart() {
        this.showConfirmModal(
            'Quý khách chắc chắn xoá đơn hàng rồi chứ?',
            'Toàn bộ sản phẩm trong giỏ hàng sẽ bị xóa. Thao tác này không thể hoàn tác.',
            () => {
                this.items = [];
                this.saveCart();
            }
        );
    },

    getTotal() {
        return this.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    },

    getCartCount() {
        return this.items.reduce((sum, item) => sum + item.quantity, 0);
    },

    updateUI() {
        const count = this.getCartCount();
        const countEl = document.getElementById('cart-count');
        if (countEl) {
            countEl.innerText = count;
            countEl.classList.toggle('hidden', count === 0);
        }
        this.renderCartItems();
    },

    toggleModal() {
        const modal = document.getElementById('cart-modal');
        if (modal) {
            modal.classList.toggle('translate-x-full');
            document.getElementById('cart-overlay')?.classList.toggle('hidden');
        }
    },

    renderFloatingButton() {
        if (document.getElementById('cart-floating-btn')) return;
        const btn = document.createElement('div');
        btn.innerHTML = `
            <div id="cart-overlay" class="fixed inset-0 bg-black/50 backdrop-blur-sm z-40 hidden transition-opacity" onclick="CartManager.toggleModal()"></div>
            <button id="cart-floating-btn" onclick="CartManager.toggleModal()" class="fixed bottom-6 right-6 lg:bottom-10 lg:right-10 bg-brand-green text-zinc-950 p-4 rounded-full shadow-[0_4px_20px_rgba(16,185,129,0.4)] hover:scale-110 transition-transform z-30 group">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                <span id="cart-count" class="absolute -top-2 -right-2 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded-full hidden border-2 border-zinc-900 shadow-md">0</span>
            </button>
        `;
        document.body.appendChild(btn);
    },

    renderCartModal() {
        if (document.getElementById('cart-modal')) return;
        const modal = document.createElement('div');
        modal.id = 'cart-modal';
        modal.className = 'fixed top-0 right-0 h-full w-[85vw] sm:w-[400px] bg-zinc-900 shadow-2xl z-50 transform translate-x-full transition-transform duration-300 flex flex-col border-l border-zinc-800';
        modal.innerHTML = `
            <div class="p-4 border-b border-zinc-800 flex justify-between items-center bg-zinc-950">
                <h3 class="text-lg font-bold text-white flex items-center gap-2">
                    <svg class="w-5 h-5 text-brand-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                    Giỏ Hàng
                </h3>
                <button onclick="CartManager.toggleModal()" class="text-zinc-400 hover:text-white p-2 bg-zinc-800 rounded-full hover:bg-zinc-700 transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
            </div>
            <div id="cart-items" class="flex-1 overflow-y-auto p-4 space-y-3 custom-scrollbar">
                <!-- Items go here -->
            </div>
            <div class="p-4 border-t border-zinc-800 bg-zinc-950">
                <div id="cart-customer-info" class="mb-4">
                    <p class="text-xs text-brand-green mb-2 font-medium"><i class="ph-fill ph-info"></i> Vui lòng để lại thông tin để chốt đơn</p>
                    <input type="text" id="cart-customer-name" placeholder="Tên của bạn *" class="w-full bg-zinc-900 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm text-white mb-2 outline-none focus:border-brand-green focus:ring-1 focus:ring-brand-green transition-all placeholder-zinc-500">
                    <input type="tel" id="cart-customer-phone" placeholder="Số điện thoại *" class="w-full bg-zinc-900 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm text-white outline-none focus:border-brand-green focus:ring-1 focus:ring-brand-green transition-all placeholder-zinc-500">
                </div>
                <div class="flex justify-between items-center mb-4 bg-zinc-900 p-3 rounded-xl border border-zinc-800">
                    <span class="text-zinc-400 font-medium">Tổng thanh toán:</span>
                    <span id="cart-total" class="text-xl font-bold text-brand-green">0 đ</span>
                </div>
                <div class="flex gap-2">
                    <button onclick="window.CartManager.clearCart()" class="px-4 py-3 rounded-xl border border-zinc-700 text-zinc-400 hover:text-white hover:bg-zinc-800 transition-colors text-sm font-medium">
                        Xóa hết
                    </button>
                    <button onclick="window.CartManager.checkoutViaZalo()" class="flex-1 bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 rounded-xl transition-colors flex justify-center items-center gap-2 shadow-lg">
                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M21.2 13.9c.7-.6 1.1-1.4 1.1-2.4 0-2.3-2.6-4.2-5.7-4.2s-5.7 1.9-5.7 4.2c0 2.3 2.6 4.2 5.7 4.2.3 0 .7 0 1-.1 1.2 1.1 2.8 1.5 4.3 1.5-.2-.9-.4-2-.7-3.2zm-12.7.3h-4.3v-5.6h4.3v1h-3.1v1.3h2.8v1h-2.8v1.3h3.1v1zM2.8 8.6h2.8l-1.9 4.3v1.3H1v-1.3l1.8-4.3H1V7.6h4.5v1l-2.7 5.6zm7.2-1h-1.2v5.6h-1.2V7.6h2.4zm-1.8 0h-2.6v5.6h2.6c1.6 0 2.5-1.1 2.5-2.8 0-1.7-.9-2.8-2.5-2.8zm-.2 4.6h-1.2v-3.6h1.2c.9 0 1.4.6 1.4 1.8 0 1.2-.5 1.8-1.4 1.8z"></path></svg>
                        Gửi Đơn Zalo
                    </button>
                </div>
            </div>
        `;
        document.body.appendChild(modal);
    },

    renderCartItems() {
        const container = document.getElementById('cart-items');
        const totalEl = document.getElementById('cart-total');
        if (!container || !totalEl) return;

        if (this.items.length === 0) {
            container.innerHTML = `
                <div class="text-center py-10 flex flex-col items-center justify-center h-full">
                    <div class="bg-zinc-800 p-4 rounded-full mb-4">
                        <svg class="w-12 h-12 text-zinc-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
                    </div>
                    <p class="text-zinc-400 font-medium">Giỏ hàng đang trống</p>
                    <p class="text-sm text-zinc-500 mt-1">Hãy thêm vài món đồ công nghệ nhé!</p>
                    <button onclick="CartManager.toggleModal()" class="mt-6 px-6 py-2 bg-zinc-800 hover:bg-zinc-700 text-white rounded-full transition-colors text-sm font-medium">Tiếp tục xem hàng</button>
                </div>`;
            totalEl.innerText = '0 đ';
            return;
        }

        const customerInfo = document.getElementById('cart-customer-info');
        if (customerInfo) {
            customerInfo.style.display = this.items.length === 0 ? 'none' : 'block';
        }

        container.innerHTML = this.items.map((item, index) => `
            <div class="bg-zinc-950 border border-zinc-800 p-3 rounded-xl relative group hover:border-zinc-700 transition-colors">
                <button onclick="window.CartManager.removeItem(${index})" class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full p-1.5 opacity-0 group-hover:opacity-100 transition-opacity shadow-md hover:bg-red-600 focus:opacity-100 lg:group-hover:opacity-100 opacity-100 lg:opacity-0">
                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                <div class="text-sm font-medium text-white mb-2 leading-snug pr-4 line-clamp-2" title="${item.name}">${item.name}</div>
                <div class="flex justify-between items-end mt-2">
                    <div>
                        <div class="text-brand-green font-bold text-sm lg:text-base">${item.price.toLocaleString('vi-VN')} đ</div>
                        <div class="text-[10px] text-zinc-500 mt-0.5">BH: ${item.warranty || 'Không có'}</div>
                    </div>
                    <div class="flex items-center bg-zinc-900 rounded-lg border border-zinc-800 shadow-inner">
                        <button onclick="window.CartManager.updateQuantity(${index}, -1)" class="w-7 h-7 flex items-center justify-center text-zinc-400 hover:text-brand-green hover:bg-zinc-800 rounded-l-lg transition-colors">-</button>
                        <span class="text-xs font-bold w-6 text-center text-white">${item.quantity}</span>
                        <button onclick="window.CartManager.updateQuantity(${index}, 1)" class="w-7 h-7 flex items-center justify-center text-zinc-400 hover:text-brand-green hover:bg-zinc-800 rounded-r-lg transition-colors">+</button>
                    </div>
                </div>
            </div>
        `).join('');

        totalEl.innerText = this.getTotal().toLocaleString('vi-VN') + ' đ';
    },

    showToast(msg) {
        let toast = document.getElementById('cart-toast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'cart-toast';
            toast.className = 'fixed top-24 right-4 bg-brand-green text-zinc-950 font-bold px-4 py-3 rounded-xl shadow-[0_10px_40px_rgba(16,185,129,0.3)] transform transition-all duration-300 translate-x-full opacity-0 z-[60] flex items-center gap-3 border border-brand-green/50';
            toast.innerHTML = `<svg class="w-5 h-5 bg-zinc-950 text-brand-green rounded-full p-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg> <span id="cart-toast-msg" class="text-sm"></span>`;
            document.body.appendChild(toast);
        }
        document.getElementById('cart-toast-msg').innerText = msg;
        
        // Show
        requestAnimationFrame(() => {
            toast.classList.remove('translate-x-full', 'opacity-0');
        });
        
        // Hide after 3s
        setTimeout(() => {
            toast.classList.add('translate-x-full', 'opacity-0');
        }, 3000);
    },

    showConfirmModal(title, message, onConfirm) {
        let modal = document.getElementById('cart-confirm-modal');
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'cart-confirm-modal';
            modal.className = 'fixed inset-0 z-[10000] flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm opacity-0 pointer-events-none transition-opacity duration-300';
            modal.innerHTML = `
                <div class="bg-zinc-900 border border-zinc-700 rounded-2xl shadow-2xl w-full max-w-sm overflow-hidden transform scale-95 transition-transform duration-300">
                    <div class="p-5">
                        <div class="flex items-center gap-3 mb-2">
                            <div class="w-10 h-10 rounded-full bg-red-500/20 text-red-500 flex items-center justify-center shrink-0">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                            </div>
                            <h3 class="text-base sm:text-lg font-bold text-white" id="cart-confirm-title"></h3>
                        </div>
                        <p class="text-zinc-400 text-sm leading-relaxed ml-14" id="cart-confirm-body"></p>
                    </div>
                    <div class="bg-zinc-950 px-5 py-4 flex gap-3 justify-end border-t border-zinc-800">
                        <button id="cart-confirm-no" class="px-5 py-2 rounded-lg font-medium text-zinc-400 hover:text-white hover:bg-zinc-800 transition-colors text-sm">
                            Không
                        </button>
                        <button id="cart-confirm-yes" class="px-5 py-2 rounded-lg font-bold text-white bg-red-500 hover:bg-red-600 transition-colors text-sm shadow-lg shadow-red-500/20">
                            Có
                        </button>
                    </div>
                </div>
            `;
            document.body.appendChild(modal);

            document.getElementById('cart-confirm-no').addEventListener('click', () => {
                this.closeConfirmModal();
            });
        }

        document.getElementById('cart-confirm-title').innerText = title;
        document.getElementById('cart-confirm-body').innerText = message;
        
        const yesBtn = document.getElementById('cart-confirm-yes');
        const newYesBtn = yesBtn.cloneNode(true);
        yesBtn.parentNode.replaceChild(newYesBtn, yesBtn);
        
        newYesBtn.addEventListener('click', () => {
            if (typeof onConfirm === 'function') onConfirm();
            this.closeConfirmModal();
        });

        requestAnimationFrame(() => {
            modal.classList.remove('opacity-0', 'pointer-events-none');
            modal.classList.add('opacity-100', 'pointer-events-auto');
            modal.querySelector('div').classList.remove('scale-95');
            modal.querySelector('div').classList.add('scale-100');
        });
    },

    closeConfirmModal() {
        const modal = document.getElementById('cart-confirm-modal');
        if (modal) {
            modal.classList.remove('opacity-100', 'pointer-events-auto');
            modal.classList.add('opacity-0', 'pointer-events-none');
            modal.querySelector('div').classList.remove('scale-100');
            modal.querySelector('div').classList.add('scale-95');
        }
    },

    checkoutViaZalo() {
        if (this.items.length === 0) return;
        
        const nameInput = document.getElementById('cart-customer-name');
        const phoneInput = document.getElementById('cart-customer-phone');
        
        const name = nameInput ? nameInput.value.trim() : '';
        const phone = phoneInput ? phoneInput.value.trim() : '';
        
        if (!name || !phone) {
            this.showToast('Vui lòng nhập Tên và Số điện thoại!');
            if (!name && nameInput) nameInput.focus();
            else if (!phone && phoneInput) phoneInput.focus();
            return;
        }
        
        let message = `🛒 ĐƠN HÀNG TỪ WEB PHÁT LỘC TECH 🛒\n\n`;
        message += `👤 Khách hàng: ${name}\n`;
        message += `📞 SĐT: ${phone}\n`;
        message += `-------------------------\n`;
        this.items.forEach((item, i) => {
            message += `${i+1}. ${item.name}\n   ▪ SL: ${item.quantity} x ${item.price.toLocaleString('vi-VN')} đ = ${(item.price * item.quantity).toLocaleString('vi-VN')} đ\n`;
        });
        message += `-------------------------\n`;
        message += `💰 Tổng dự kiến: ${this.getTotal().toLocaleString('vi-VN')} đ\n\n`;
        message += `Vui lòng kiểm tra và báo giá lại giúp mình nhé. Cảm ơn!`;

        // Copy to clipboard fallback to ensure Zalo doesn't drop the message
        navigator.clipboard.writeText(message).then(() => {
            this.showToast('Đã copy đơn hàng! Hãy DÁN (Paste) vào Zalo nhé.');
            setTimeout(() => {
                const encodedMsg = encodeURIComponent(message);
                const zaloUrl = `https://zalo.me/${this.zaloNumber}?text=${encodedMsg}`;
                window.open(zaloUrl, '_blank');
                this.toggleModal();
            }, 1500);
        }).catch(err => {
            // Fallback if clipboard fails
            const encodedMsg = encodeURIComponent(message);
            const zaloUrl = `https://zalo.me/${this.zaloNumber}?text=${encodedMsg}`;
            window.open(zaloUrl, '_blank');
            this.toggleModal();
        });
    }
};

document.addEventListener('DOMContentLoaded', () => {
    CartManager.init();
});
