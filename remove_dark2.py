import glob
import re

for file in glob.glob("*.html"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = re.sub(r'class="([^"]*)\bdark\b([^"]*)"', r'class="\1\2"', content)
        new_content = new_content.replace('  "', '"').replace('class=" "', 'class=""')
            
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Removed dark mode in {file}")
    except Exception as e:
        print(f"Error {file}: {e}")
