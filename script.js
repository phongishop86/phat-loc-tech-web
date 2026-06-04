// Chat Widget Toggle Logic
const chatToggleBtn = document.getElementById('chat-toggle');
const chatPanel = document.getElementById('chat-panel');
const btnTuVan = document.getElementById('btn-tu-van');

let isChatOpen = false;

function toggleChat() {
    isChatOpen = !isChatOpen;
    
    if (isChatOpen) {
        // Mở chat
        chatPanel.classList.remove('scale-90', 'opacity-0', 'pointer-events-none');
        chatPanel.classList.add('scale-100', 'opacity-100');
        // Đổi icon
        chatToggleBtn.innerHTML = '<i class="ph ph-x text-2xl"></i>';
    } else {
        // Đóng chat
        chatPanel.classList.remove('scale-100', 'opacity-100');
        chatPanel.classList.add('scale-90', 'opacity-0', 'pointer-events-none');
        // Đổi lại icon
        chatToggleBtn.innerHTML = `
            <i class="ph ph-chats text-2xl"></i>
            <span class="absolute top-0 right-0 w-3.5 h-3.5 bg-green-500 rounded-full border-2 border-zinc-950 animate-pulse-g"></span>
        `;
    }
}

chatToggleBtn.addEventListener('click', toggleChat);

if (btnTuVan) {
    btnTuVan.addEventListener('click', (e) => {
        e.preventDefault();
        // Bật/tắt khung chat
        toggleChat();
    });
}

// Smooth Scroll & Highlight for Service Links
const serviceIds = ['#thiet-bi', '#ha-tang', '#dich-vu', '#phan-mem'];

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        
        if (serviceIds.includes(targetId)) {
            e.preventDefault();
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                // Cuộn tới giữa màn hình một cách mượt mà
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
                
                // Xóa hiệu ứng highlight cũ của tất cả thẻ
                serviceIds.forEach(id => {
                    const el = document.querySelector(id);
                    if (el) {
                        el.classList.remove('scale-[1.05]', 'z-50', 'ring-2', 'ring-offset-4', 'ring-offset-zinc-950', 'ring-brand-green', 'ring-brand-orange', 'ring-blue-400', 'ring-brand-purple', 'shadow-[0_0_40px_rgba(16,185,129,0.4)]', 'shadow-[0_0_40px_rgba(249,115,22,0.4)]', 'shadow-[0_0_40px_rgba(96,165,250,0.4)]', 'shadow-[0_0_40px_rgba(139,92,246,0.4)]');
                    }
                });
                
                // Đợi cuộn hòm hòm rồi thêm hiệu ứng highlight (thời gian tuỳ độ dài trang)
                setTimeout(() => {
                    // Thêm class phát sáng cơ bản
                    targetElement.classList.add('transition-all', 'duration-500', 'scale-[1.05]', 'z-50', 'ring-2', 'ring-offset-4', 'ring-offset-zinc-950');
                    
                    // Thêm màu sắc tương ứng cho từng dịch vụ
                    if (targetId === '#thiet-bi') {
                        targetElement.classList.add('ring-brand-green', 'shadow-[0_0_40px_rgba(16,185,129,0.4)]');
                    } else if (targetId === '#ha-tang') {
                        targetElement.classList.add('ring-brand-orange', 'shadow-[0_0_40px_rgba(249,115,22,0.4)]');
                    } else if (targetId === '#dich-vu') {
                        targetElement.classList.add('ring-blue-400', 'shadow-[0_0_40px_rgba(96,165,250,0.4)]');
                    } else if (targetId === '#phan-mem') {
                        targetElement.classList.add('ring-brand-purple', 'shadow-[0_0_40px_rgba(139,92,246,0.4)]');
                    }
                    
                    // Tự động tắt phát sáng sau 3 giây
                    setTimeout(() => {
                        targetElement.classList.remove('scale-[1.05]', 'z-50', 'ring-2', 'ring-offset-4', 'ring-offset-zinc-950', 'ring-brand-green', 'ring-brand-orange', 'ring-blue-400', 'ring-brand-purple', 'shadow-[0_0_40px_rgba(16,185,129,0.4)]', 'shadow-[0_0_40px_rgba(249,115,22,0.4)]', 'shadow-[0_0_40px_rgba(96,165,250,0.4)]', 'shadow-[0_0_40px_rgba(139,92,246,0.4)]');
                    }, 3000);
                    
                }, 400); // delay 400ms để đợi cuộn xuống tới nơi
            }
        }
    });
});

// Header Auto-Hide on Scroll
const header = document.querySelector('header');
const floatingHome = document.getElementById('floating-home-btn');
if (header) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('-translate-y-full');
            if (floatingHome) {
                floatingHome.classList.remove('-translate-y-24', 'opacity-0', 'pointer-events-none');
            }
        } else {
            header.classList.remove('-translate-y-full');
            if (floatingHome) {
                floatingHome.classList.add('-translate-y-24', 'opacity-0', 'pointer-events-none');
            }
        }
    });
}

// Handle Contact Form Submission
const leadForm = document.getElementById('lead-form');
if (leadForm) {
    leadForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const btn = leadForm.querySelector('button[type="submit"]');
        const originalBtnHTML = btn.innerHTML;
        btn.innerHTML = 'Đang gửi... <i class="ph ph-spinner animate-spin text-lg"></i>';
        btn.disabled = true;

        fetch(leadForm.action, {
            method: 'POST',
            body: new FormData(leadForm),
            headers: {
                'Accept': 'application/json'
            }
        }).then(response => {
            if (response.ok) {
                const container = document.getElementById('contact-form-container');
                container.innerHTML = '<div class="text-center py-6 bg-[#27272a]/50 rounded-xl border border-zinc-800"><i class="ph-fill ph-check-circle text-5xl text-green-500 mb-3 drop-shadow-[0_0_15px_rgba(34,197,94,0.5)]"></i><p class="text-white font-bold text-base">Gửi thành công!</p><p class="text-zinc-400 text-xs mt-2 px-4 leading-relaxed">Thông tin của bạn đã được tiếp nhận. Phát Lộc Tech sẽ liên hệ lại qua số điện thoại này trong thời gian sớm nhất.</p></div>';
            } else {
                throw new Error('Network error');
            }
        }).catch(error => {
            btn.innerHTML = 'Lỗi mạng, thử lại <i class="ph ph-warning text-lg"></i>';
            btn.disabled = false;
            setTimeout(() => {
                btn.innerHTML = originalBtnHTML;
            }, 3000);
        });
    });
}

// Trigger chat open and prefill when clicking quote buttons
document.querySelectorAll('.request-quote-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        
        // Find the title of the service
        const card = e.target.closest('div.group');
        const title = card ? card.querySelector('h3').innerText : '';
        
        // Open the chat widget if closed
        if (!isChatOpen) {
            toggleChat();
        }
        
        // Fill the form's textarea
        const textarea = document.querySelector('textarea[name="Yêu cầu"]');
        if (textarea && title) {
            textarea.value = `Báo giá: ${title}`;
            textarea.focus();
        }
    });
});

// Custom Modal Alert Function
function showCustomAlert(title, message) {
    let modal = document.getElementById('custom-alert-modal');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'custom-alert-modal';
        modal.className = 'fixed inset-0 z-[10000] flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm opacity-0 pointer-events-none transition-opacity duration-300';
        
        modal.innerHTML = `
            <div class="bg-zinc-900 border border-zinc-700 rounded-2xl shadow-2xl w-full max-w-md overflow-hidden transform scale-95 transition-transform duration-300">
                <div class="p-6">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="w-10 h-10 rounded-full bg-brand-green/20 text-brand-green flex items-center justify-center shrink-0">
                            <i class="ph-fill ph-info text-2xl"></i>
                        </div>
                        <h3 class="text-lg font-bold text-white" id="custom-alert-title"></h3>
                    </div>
                    <p class="text-zinc-300 text-sm leading-relaxed" id="custom-alert-body" style="white-space: pre-wrap;"></p>
                </div>
                <div class="bg-zinc-950 px-6 py-4 flex justify-end border-t border-zinc-800">
                    <button id="custom-alert-close" class="bg-brand-green hover:bg-green-600 text-white font-bold py-2 px-6 rounded-lg transition-colors text-sm">
                        Đồng ý
                    </button>
                </div>
            </div>
        `;
        document.body.appendChild(modal);

        document.getElementById('custom-alert-close').addEventListener('click', () => {
            modal.classList.remove('opacity-100', 'pointer-events-auto');
            modal.classList.add('opacity-0', 'pointer-events-none');
            const innerDiv = modal.querySelector('div');
            innerDiv.classList.remove('scale-100');
            innerDiv.classList.add('scale-95');
        });
    }

    document.getElementById('custom-alert-title').innerText = title;
    document.getElementById('custom-alert-body').innerText = message;

    // Show modal
    modal.classList.remove('opacity-0', 'pointer-events-none');
    modal.classList.add('opacity-100', 'pointer-events-auto');
    const innerDiv = modal.querySelector('div');
    innerDiv.classList.remove('scale-95');
    innerDiv.classList.add('scale-100');
}

// Trigger alert when clicking view detail buttons
document.querySelectorAll('.view-detail-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const href = btn.getAttribute('href');
        if (href === '#pricing-table') {
            const table = document.getElementById('pricing-table') || document.getElementById('pricing-container');
            if (table) {
                e.preventDefault();
                table.scrollIntoView({ behavior: 'smooth' });
                return;
            }
        }
        
        e.preventDefault();
        showCustomAlert(
            "Thông báo từ Phát Lộc Tech",
            "Hệ thống báo giá tự động cho danh mục này hiện đang được tối ưu hóa nhằm mang lại trải nghiệm tốt nhất. Để không làm gián đoạn kế hoạch của Quý khách, xin vui lòng để lại thông tin sản phẩm cần báo giá kèm số điện thoại tại khung chat/form liên hệ, hoặc gọi số 0932 685 794. Chúng tôi xin chân thành cảm ơn sự thông cảm của Quý khách!"
        );
    });
});

// Trigger alert when clicking policy buttons
document.querySelectorAll('.policy-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        const policyType = btn.getAttribute('data-policy');
        let title = "Chính Sách";
        let content = "";
        
        if (policyType === 'baohanh') {
            title = "Chính Sách: Bảo hành 1 đổi 1";
            content = "Cam kết bảo hành 1 đổi 1 đối với tất cả thiết bị phần cứng do Phát Lộc Tech cung cấp trong vòng 30 ngày đầu tiên nếu phát sinh lỗi từ nhà sản xuất. Sau 30 ngày, sản phẩm sẽ được bảo hành theo đúng tiêu chuẩn và thời hạn của hãng (12-36 tháng).";
        } else if (policyType === 'hotro') {
            title = "Chính Sách: Hỗ trợ tận nơi (Ad-hoc)";
            content = "Cung cấp dịch vụ hỗ trợ kỹ thuật tận nơi (Ad-hoc) nhanh chóng trong vòng 2-4 giờ làm việc (giờ hành chính). Dịch vụ xử lý sự cố máy tính, cấu hình mạng, camera và máy chủ linh hoạt theo từng lần yêu cầu mà không cần ký hợp đồng bảo trì dài hạn.";
        } else if (policyType === 'thanhtoan') {
            title = "Chính Sách: Thanh toán & Vận chuyển";
            content = "Hỗ trợ đa dạng phương thức thanh toán: Tiền mặt, Chuyển khoản hoặc Thanh toán qua thẻ tín dụng. Đặc biệt, miễn phí giao hàng và lắp đặt tận nơi tại khu vực nội thành cho các đơn hàng thiết bị và máy bộ trị giá trên 2,000,000 VNĐ.";
        }
        
        showCustomAlert(title, content);
    });
});


// Scroll Reveal Animation
function reveal() {
    var reveals = document.querySelectorAll('.reveal');
    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 100;
        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add('active');
        }
    }
}
window.addEventListener('scroll', reveal);
reveal(); // Trigger on load

// Number Counter Animation
const counters = document.querySelectorAll('.counter');
const speed = 100; // The lower the slower

function animateCounters() {
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            const inc = target / speed;
            if (count < target) {
                counter.innerText = Math.ceil(count + inc);
                setTimeout(updateCount, 20);
            } else {
                counter.innerText = target;
            }
        };
        
        // Ensure animation only triggers once when in view
        const rect = counter.getBoundingClientRect();
        if(rect.top < window.innerHeight && !counter.classList.contains('counted')) {
            counter.classList.add('counted');
            updateCount();
        }
    });
}
window.addEventListener('scroll', animateCounters);
animateCounters(); // Trigger on load
