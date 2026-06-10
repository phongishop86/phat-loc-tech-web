import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix banner background blobs
content = content.replace('bg-secondary-/20', 'bg-secondary/20')
content = content.replace('bg-brand-green/10', 'bg-accent/20')
content = content.replace('#10b981 1.5px', '#06b6d4 1.5px')

# 2. Fix the bottom face of the cube
content = content.replace('text-zinc-700/50', 'text-slate-200')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero section and cube bottom face updated.")
