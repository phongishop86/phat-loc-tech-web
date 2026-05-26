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
