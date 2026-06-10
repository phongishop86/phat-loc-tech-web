import glob

for file in glob.glob("*.html"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content.replace('class="h-full antialiased dark"', 'class="h-full antialiased"')
            
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Removed dark mode in {file}")
    except Exception as e:
        print(f"Error {file}: {e}")
