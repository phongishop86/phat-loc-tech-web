import glob

def revert_hero_and_widget():
    # 1. Update all HTML files to fix the dark Chat Widget
    for file in glob.glob("*.html"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = content
            # Fix widget backgrounds
            new_content = new_content.replace('bg-[#18181b]', 'bg-white shadow-xl')
            new_content = new_content.replace('bg-[#09090b]', 'bg-slate-50')
            new_content = new_content.replace('bg-[#27272a]', 'bg-white')
            # Text contrast in widget if any (text-slate-300 to text-slate-600)
            new_content = new_content.replace('text-slate-300', 'text-slate-600')
            new_content = new_content.replace('text-slate-400', 'text-slate-500')
            
            if new_content != content:
                with open(file, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Fixed widget in {file}")
        except Exception as e:
            print(f"Error {file}: {e}")

    # 2. Revert index.html Hero background to white
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            index_content = f.read()
            
        # Revert hero gradient to white
        index_content = index_content.replace(
            'bg-gradient-to-br from-secondary to-accent',
            'bg-white'
        )
        # Revert hero text colors
        index_content = index_content.replace(
            '<h1 class="text-4xl md:text-5xl lg:text-7xl font-black mb-6 text-white leading-tight font-serif drop-shadow-md">',
            '<h1 class="text-4xl md:text-5xl lg:text-7xl font-black mb-6 text-primary leading-tight font-serif">'
        )
        index_content = index_content.replace(
            '<p class="text-lg md:text-xl text-white/90 mb-8 max-w-2xl leading-relaxed font-medium">',
            '<p class="text-lg md:text-xl text-slate-600 mb-8 max-w-2xl leading-relaxed">'
        )
        index_content = index_content.replace(
            '<span class="text-transparent bg-clip-text bg-gradient-to-r from-white to-slate-200 drop-shadow-lg">',
            '<span class="text-transparent bg-clip-text bg-gradient-to-r from-secondary to-accent">'
        )
        index_content = index_content.replace(
            '<span class="text-sm font-semibold text-white tracking-wide uppercase">',
            '<span class="text-sm font-semibold text-secondary tracking-wide uppercase">'
        )
        
        # Revert hero buttons
        index_content = index_content.replace(
            '<a href="dich-vu-it.html" class="px-8 py-4 bg-white text-secondary shadow-lg rounded-xl font-bold hover:bg-slate-50 transition-colors flex items-center gap-2 group">',
            '<a href="dich-vu-it.html" class="px-8 py-4 bg-secondary text-white rounded-xl font-bold hover:bg-primary transition-colors flex items-center gap-2 group shadow-lg shadow-secondary/30">'
        )
        index_content = index_content.replace(
            '<a href="bao-gia.html" class="px-8 py-4 bg-white/20 text-white backdrop-blur-sm border border-white/30 hover:bg-white/30 rounded-xl font-bold transition-colors flex items-center gap-2 shadow-lg">',
            '<a href="bao-gia.html" class="px-8 py-4 bg-slate-50 text-primary border border-slate-200 hover:bg-slate-100 rounded-xl font-bold transition-colors flex items-center gap-2">'
        )
        
        # Revert blur orbs
        index_content = index_content.replace(
            '<div class="absolute top-[-10%] right-[-5%] w-[500px] h-[500px] rounded-full bg-white/20 blur-[100px]"></div>',
            '<div class="absolute top-[-10%] right-[-5%] w-[500px] h-[500px] rounded-full bg-secondary/10 blur-[100px]"></div>'
        )
        index_content = index_content.replace(
            '<div class="absolute bottom-[-10%] left-[-5%] w-[400px] h-[400px] rounded-full bg-white/10 blur-[100px]"></div>',
            '<div class="absolute bottom-[-10%] left-[-5%] w-[400px] h-[400px] rounded-full bg-accent/10 blur-[100px]"></div>'
        )
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(index_content)
        print("Reverted index.html hero background to white.")
    except Exception as e:
        print(f"Error index.html: {e}")

if __name__ == "__main__":
    revert_hero_and_widget()
