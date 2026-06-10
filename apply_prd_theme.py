import glob

replacements = {
    # Backgrounds
    'bg-zinc-950': 'bg-slate-50',
    'bg-zinc-900': 'bg-white',
    'bg-zinc-800': 'bg-slate-100',
    'bg-zinc-950/30': 'bg-slate-50/50',
    'bg-zinc-950/80': 'bg-white/80 backdrop-blur-md',
    'bg-zinc-900/50': 'bg-white/90 shadow-xl shadow-slate-200/50',
    'bg-zinc-800/50': 'bg-slate-50',
    'bg-[#0a0a0c]': 'bg-slate-50',
    'bg-[#121214]': 'bg-white',
    'bg-[#18181b]': 'bg-white shadow-xl shadow-slate-200/50',
    'bg-[#27272a]': 'bg-slate-100',
    
    # Texts
    'text-white': 'text-primary',
    'text-zinc-50': 'text-primary',
    'text-zinc-100': 'text-slate-800',
    'text-zinc-200': 'text-slate-800',
    'text-zinc-300': 'text-slate-700',
    'text-zinc-400': 'text-slate-500',
    'text-zinc-500': 'text-slate-400',
    'text-gray-100': 'text-slate-800',
    'text-gray-400': 'text-slate-500',
    
    # Borders
    'border-zinc-800': 'border-slate-200',
    'border-zinc-700': 'border-slate-300',
    'border-zinc-800/50': 'border-slate-200',
    'border-zinc-800/80': 'border-slate-200',
    'border-white/5': 'border-slate-200',
    'border-white/10': 'border-slate-200',
    'border-white/20': 'border-slate-300',
    
    # Hovers
    'hover:bg-zinc-800': 'hover:bg-slate-100',
    'hover:bg-zinc-700': 'hover:bg-slate-200',
    'group-hover:text-white': 'group-hover:text-secondary',
    'hover:text-white': 'hover:text-secondary',
    
    # Accents & Gradients
    'from-brand-purple': 'from-secondary',
    'to-pink-500': 'to-accent',
    'to-brand-green': 'to-accent',
    'from-purple-500': 'from-secondary',
    'bg-brand-purple': 'bg-secondary',
    'text-brand-purple': 'text-secondary',
    'hover:bg-brand-purple-dark': 'hover:bg-primary',
    
    # Replace some specific card styling to look good in light theme
    'rounded-2xl p-5': 'rounded-2xl p-5 shadow-lg shadow-slate-200/50',
    'rounded-3xl p-6': 'rounded-3xl p-6 shadow-xl shadow-slate-200/50',
}

files_to_patch = glob.glob("*.html") + ["pricing.js", "script.js"]

for file in files_to_patch:
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Patched theme in {file}")
    except Exception as e:
        print(f"Error patching {file}: {e}")
