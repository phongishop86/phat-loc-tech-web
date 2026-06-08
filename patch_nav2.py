import glob

old_nav = """<a href="bao-gia.html" class="flex items-center gap-1.5 text-[14px] font-bold text-yellow-400 hover:text-yellow-300 transition-colors uppercase tracking-wider drop-shadow-md"><i class="ph-bold ph-list-numbers text-lg"></i> Báo Giá</a>
                </div>
                <div class="relative flex items-center h-full group py-6">
                    <a href="may-tinh-linh-kien.html" class="flex items-center gap-1.5 text-[13px] font-bold text-gray-100 hover:text-yellow-400 transition-colors uppercase tracking-wider drop-shadow-sm">Máy Tính & Linh Kiện</a>"""

new_nav = """<a href="bao-gia.html" class="flex items-center gap-1.5 text-[14px] font-bold text-yellow-400 hover:text-yellow-300 transition-colors uppercase tracking-wider drop-shadow-md"><i class="ph-bold ph-list-numbers text-lg"></i> Báo Giá</a>
                </div>
                <div class="relative flex items-center h-full group py-6">
                    <a href="bao-gia-1.html" class="flex items-center gap-1.5 text-[14px] font-bold text-yellow-400 hover:text-yellow-300 transition-colors uppercase tracking-wider drop-shadow-md"><i class="ph-bold ph-table text-lg"></i> Báo Giá 1</a>
                </div>
                <div class="relative flex items-center h-full group py-6">
                    <a href="may-tinh-linh-kien.html" class="flex items-center gap-1.5 text-[13px] font-bold text-gray-100 hover:text-yellow-400 transition-colors uppercase tracking-wider drop-shadow-sm">Máy Tính & Linh Kiện</a>"""

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_nav in content:
        content = content.replace(old_nav, new_nav)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Skipped {file}")
