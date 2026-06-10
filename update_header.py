import glob

for file in glob.glob("*.html"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        # 1. Header Background
        new_content = new_content.replace(
            'bg-gradient-to-r from-purple-950 via-indigo-950 to-purple-900 z-50 shadow-xl sticky top-0 border-b border-slate-200',
            'bg-white/95 backdrop-blur-lg z-50 shadow-sm sticky top-0 border-b border-slate-200'
        )
        
        # 2. Mobile menu button hover
        new_content = new_content.replace('hover:bg-white/10 rounded-lg', 'hover:bg-slate-100 rounded-lg')
        
        # 3. Báo Giá link
        new_content = new_content.replace(
            'text-[14px] font-bold text-yellow-400 hover:text-yellow-300 transition-colors uppercase tracking-wider drop-shadow-md',
            'text-[14px] font-bold text-accent hover:text-secondary transition-colors uppercase tracking-wider'
        )
        
        # 4. Other menu links
        new_content = new_content.replace(
            'text-[13px] font-bold text-slate-800 hover:text-yellow-400 transition-colors uppercase tracking-wider drop-shadow-sm',
            'text-[13px] font-bold text-primary hover:text-secondary transition-colors uppercase tracking-wider'
        )
        
        # In case some variations exist
        new_content = new_content.replace('text-slate-800 hover:text-yellow-400', 'text-primary hover:text-secondary')
            
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated header in {file}")
    except Exception as e:
        print(f"Error {file}: {e}")
