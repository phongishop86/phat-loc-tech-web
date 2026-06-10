import glob
import re

for file in glob.glob("*.html"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content.replace('from-zinc-950 to-zinc-900', 'from-secondary to-primary')
        new_content = new_content.replace('from-zinc-950 to-transparent', 'from-white to-transparent')
        new_content = new_content.replace('via-zinc-700', 'via-slate-300')
            
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Cleaned up remaining dark gradients in {file}")
    except Exception as e:
        print(f"Error {file}: {e}")
