import glob
import re

def process_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        # 1. Global Readability: text-slate-500 to text-slate-600
        new_content = new_content.replace('text-slate-500', 'text-slate-600')
        
        # 2. Fix Card Shadows and Borders to be more "Corporate Modern"
        new_content = new_content.replace(
            'bg-white/90 shadow-xl shadow-slate-200/50 p-8 rounded-2xl border border-slate-200',
            'bg-white shadow-xl shadow-secondary/10 p-8 rounded-2xl border border-slate-100 border-t-4 border-t-secondary'
        )
        new_content = new_content.replace(
            'hover:shadow-[0_0_30px_rgba(16,185,129,0.2)]',
            'hover:shadow-2xl hover:shadow-secondary/20'
        )
        new_content = new_content.replace(
            'border-zinc-900',
            'border-slate-200'
        )
        
        # If it's index.html, apply specific section background fixes
        if filename == "index.html":
            # Fix Achievements text
            ach_start = new_content.find('id="achievements"')
            if ach_start != -1:
                ach_end = new_content.find('</section>', ach_start)
                if ach_end != -1:
                    ach_block = new_content[ach_start:ach_end]
                    # Make numbers white
                    ach_block = ach_block.replace('text-primary', 'text-white')
                    # Make labels light blue instead of slate-600
                    ach_block = ach_block.replace('text-slate-600', 'text-blue-100')
                    new_content = new_content[:ach_start] + ach_block + new_content[ach_end:]

            # Inject colorful mesh backgrounds to specific sections
            # "Tại Sao Chọn"
            new_content = new_content.replace(
                '<section class="py-20 relative reveal">',
                '<section class="py-20 relative reveal bg-gradient-to-br from-white via-blue-50/50 to-white">'
            )
            
            # "Hệ Sinh Thái Dịch Vụ"
            new_content = new_content.replace(
                '<section id="services" class="w-full bg-slate-50 py-32 border-b border-slate-200 relative overflow-hidden">',
                '<section id="services" class="w-full bg-white py-32 border-b border-slate-200 relative overflow-hidden">'
            )
            
            # "Quy Trình Triển Khai"
            new_content = new_content.replace(
                '<section class="py-24 relative overflow-hidden reveal">',
                '<section class="py-24 relative overflow-hidden reveal bg-gradient-to-b from-blue-50/30 to-white">'
            )
            
        if new_content != content:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filename}")
            
    except Exception as e:
        print(f"Error {filename}: {e}")

for file in glob.glob("*.html"):
    process_file(file)

