import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Heading
# We'll match "Quy Trình Triển Khai" handling any potential weird encoding by just matching the English/HTML parts around it.
# Actually, if I just use the exact string it might fail due to utf-8 vs whatever PS printed. Let's use a regex.
heading_pattern = r'<h2 class="text-3xl md:text-5xl font-serif font-bold text-primary mb-4">(Quy Tr[^\<]*Tri[^\<]*Khai)</h2>'
heading_repl = r'<h2 class="text-4xl md:text-5xl font-[var(--font-oswald)] font-bold text-slate-900 mb-4 tracking-tight uppercase">Quy Trình <span class="text-[#1d4ed8]">Triển Khai</span></h2>'
content = re.sub(heading_pattern, heading_repl, content)

# 2. Update the Step Numbers and hover colors
# Step 1
content = content.replace('group-hover:border-brand-green group-hover:text-brand-green', 'group-hover:border-[#1d4ed8] group-hover:text-[#1d4ed8]')
content = content.replace('bg-brand-green text-primary text-sm font-black rounded-full flex items-center justify-center border-4 border-zinc-950', 'bg-[#1d4ed8] text-white text-sm font-black rounded-full flex items-center justify-center border-4 border-white')

# Step 2
content = content.replace('group-hover:border-brand-purple group-hover:text-secondary', 'group-hover:border-[#1d4ed8] group-hover:text-[#1d4ed8]')
content = content.replace('bg-secondary text-primary text-sm font-black rounded-full flex items-center justify-center border-4 border-zinc-950', 'bg-[#1d4ed8] text-white text-sm font-black rounded-full flex items-center justify-center border-4 border-white')

# Step 3
content = content.replace('group-hover:border-brand-orange group-hover:text-brand-orange', 'group-hover:border-[#1d4ed8] group-hover:text-[#1d4ed8]')
content = content.replace('bg-brand-orange text-primary text-sm font-black rounded-full flex items-center justify-center border-4 border-zinc-950', 'bg-[#1d4ed8] text-white text-sm font-black rounded-full flex items-center justify-center border-4 border-white')

# Step 4
content = content.replace('group-hover:border-blue-500 group-hover:text-blue-500', 'group-hover:border-[#1d4ed8] group-hover:text-[#1d4ed8]')
content = content.replace('bg-blue-500 text-primary text-sm font-black rounded-full flex items-center justify-center border-4 border-zinc-950', 'bg-[#1d4ed8] text-white text-sm font-black rounded-full flex items-center justify-center border-4 border-white')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Process typography and colors updated successfully.")
