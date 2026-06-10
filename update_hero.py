import glob

for file in glob.glob("*.html"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        # Change body background
        new_content = new_content.replace(
            '<body class="min-h-full flex flex-col bg-slate-50 text-primary font-sans">',
            '<body class="min-h-full flex flex-col bg-white text-primary font-sans">'
        )
        new_content = new_content.replace(
            '<body class="min-h-full flex flex-col bg-slate-50 text-slate-900 font-sans">',
            '<body class="min-h-full flex flex-col bg-white text-slate-900 font-sans">'
        )
            
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated body in {file}")
    except Exception as e:
        print(f"Error {file}: {e}")

# Specifically update Hero section in index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

# Change Hero background
index_content = index_content.replace(
    '<section class="relative min-h-[90vh] flex items-center pt-24 pb-16 overflow-hidden bg-slate-50">',
    '<section class="relative min-h-[90vh] flex items-center pt-24 pb-16 overflow-hidden bg-gradient-to-br from-secondary to-accent">'
)
# The blobs inside Hero need to be white to glow, or removed. Let's just make them white/20
index_content = index_content.replace(
    '<div class="absolute top-[-10%] right-[-5%] w-[500px] h-[500px] rounded-full bg-secondary/20 blur-[100px]"></div>',
    '<div class="absolute top-[-10%] right-[-5%] w-[500px] h-[500px] rounded-full bg-white/20 blur-[100px]"></div>'
)
index_content = index_content.replace(
    '<div class="absolute bottom-[-10%] left-[-5%] w-[400px] h-[400px] rounded-full bg-accent/20 blur-[100px]"></div>',
    '<div class="absolute bottom-[-10%] left-[-5%] w-[400px] h-[400px] rounded-full bg-white/10 blur-[100px]"></div>'
)
index_content = index_content.replace(
    'style="background-image:radial-gradient(circle, #06b6d4 1.5px, transparent 1.5px);background-size:16px 16px"',
    'style="background-image:radial-gradient(circle, #ffffff 1.5px, transparent 1.5px);background-size:16px 16px"'
)

# Text colors inside Hero
# Replace specific text colors inside the hero text block to be white.
index_content = index_content.replace(
    '<h1 class="text-4xl md:text-5xl lg:text-7xl font-black mb-6 text-primary leading-tight font-serif">',
    '<h1 class="text-4xl md:text-5xl lg:text-7xl font-black mb-6 text-white leading-tight font-serif drop-shadow-md">'
)
index_content = index_content.replace(
    '<span class="text-transparent bg-clip-text bg-gradient-to-r from-secondary to-accent">',
    '<span class="text-transparent bg-clip-text bg-gradient-to-r from-white to-slate-200 drop-shadow-lg">'
)
index_content = index_content.replace(
    '<p class="text-lg md:text-xl text-slate-700 mb-8 max-w-2xl leading-relaxed">',
    '<p class="text-lg md:text-xl text-white/90 mb-8 max-w-2xl leading-relaxed font-medium">'
)
# Make the primary button white
index_content = index_content.replace(
    '<a href="dich-vu-it.html" class="px-8 py-4 bg-secondary text-white rounded-xl font-bold hover:bg-primary transition-colors flex items-center gap-2 group">',
    '<a href="dich-vu-it.html" class="px-8 py-4 bg-white text-secondary shadow-lg rounded-xl font-bold hover:bg-slate-50 transition-colors flex items-center gap-2 group">'
)
# Make the secondary button translucent white
index_content = index_content.replace(
    '<a href="bao-gia.html" class="px-8 py-4 bg-slate-100 text-primary hover:bg-slate-200 rounded-xl font-bold transition-colors flex items-center gap-2">',
    '<a href="bao-gia.html" class="px-8 py-4 bg-white/20 text-white backdrop-blur-sm border border-white/30 hover:bg-white/30 rounded-xl font-bold transition-colors flex items-center gap-2 shadow-lg">'
)
# Hero tag line text
index_content = index_content.replace(
    '<span class="text-sm font-semibold text-secondary tracking-wide uppercase">Dịch vụ IT Chuyên nghiệp</span>',
    '<span class="text-sm font-semibold text-white tracking-wide uppercase">Dịch vụ IT Chuyên nghiệp</span>'
)
index_content = index_content.replace(
    '<div class="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-brand-green/10 border border-brand-green/20 mb-8 fade-in-up">',
    '<div class="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-white/20 border border-white/30 mb-8 fade-in-up backdrop-blur-sm">'
)

# Features below hero button (if any) - leave them as is for now since they are below the hero gradient

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
    
print("Updated Hero section in index.html")
