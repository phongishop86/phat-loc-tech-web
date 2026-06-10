import glob
import re

replacements = {
    # Backgrounds
    r'\bbg-zinc-950/80\b': 'bg-white/80 backdrop-blur-md',
    r'\bbg-zinc-950/30\b': 'bg-slate-50/50',
    r'\bbg-zinc-900/50\b': 'bg-white/90 shadow-xl shadow-slate-200/50',
    r'\bbg-zinc-800/50\b': 'bg-slate-50',
    r'\bbg-zinc-950\b': 'bg-slate-50',
    r'\bbg-zinc-900\b': 'bg-white',
    r'\bbg-zinc-800\b': 'bg-slate-100',
    r'\bbg-\[\#0a0a0c\]\b': 'bg-slate-50',
    r'\bbg-\[\#121214\]\b': 'bg-white',
    r'\bbg-\[\#18181b\]\b': 'bg-white shadow-xl shadow-slate-200/50',
    r'\bbg-\[\#27272a\]\b': 'bg-slate-100',
    
    # Texts
    r'\btext-white\b': 'text-primary',
    r'\btext-zinc-50\b': 'text-primary',
    r'\btext-zinc-100\b': 'text-slate-800',
    r'\btext-zinc-200\b': 'text-slate-800',
    r'\btext-zinc-300\b': 'text-slate-700',
    r'\btext-zinc-400\b': 'text-slate-500',
    r'\btext-zinc-500\b': 'text-slate-400',
    r'\btext-gray-100\b': 'text-slate-800',
    r'\btext-gray-400\b': 'text-slate-500',
    
    # Borders
    r'\bborder-zinc-800/50\b': 'border-slate-200',
    r'\bborder-zinc-800/80\b': 'border-slate-200',
    r'\bborder-white/5\b': 'border-slate-200',
    r'\bborder-white/10\b': 'border-slate-200',
    r'\bborder-white/20\b': 'border-slate-300',
    r'\bborder-zinc-800\b': 'border-slate-200',
    r'\bborder-zinc-700\b': 'border-slate-300',
    
    # Hovers
    r'\bhover:bg-zinc-800\b': 'hover:bg-slate-100',
    r'\bhover:bg-zinc-700\b': 'hover:bg-slate-200',
    r'\bgroup-hover:text-white\b': 'group-hover:text-secondary',
    r'\bhover:text-white\b': 'hover:text-secondary',
    
    # Accents & Gradients
    r'\bfrom-brand-purple\b': 'from-secondary',
    r'\bto-pink-500\b': 'to-accent',
    r'\bto-brand-green\b': 'to-accent',
    r'\bfrom-purple-500\b': 'from-secondary',
    r'\bbg-brand-purple\b': 'bg-secondary',
    r'\btext-brand-purple\b': 'text-secondary',
    r'\bhover:bg-brand-purple-dark\b': 'hover:bg-primary',
    
    # Replace some specific card styling to look good in light theme
    r'\brounded-2xl p-5\b': 'rounded-2xl p-5 shadow-lg shadow-slate-200/50',
    r'\brounded-3xl p-6\b': 'rounded-3xl p-6 shadow-xl shadow-slate-200/50',
}

files_to_patch = glob.glob("*.html") + ["pricing.js", "script.js"]

for file in files_to_patch:
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        for old, new in replacements.items():
            new_content = re.sub(old, new, new_content)
            
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Patched theme in {file}")
    except Exception as e:
        print(f"Error patching {file}: {e}")
