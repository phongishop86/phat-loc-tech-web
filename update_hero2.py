import glob
import re

for file in glob.glob("*.html"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = re.sub(r'<body([^>]*)bg-slate-50([^>]*)>', r'<body\1bg-white\2>', content)
            
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated body regex in {file}")
    except Exception as e:
        print(f"Error {file}: {e}")
