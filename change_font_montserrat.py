import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Google Fonts Link
old_fonts = 'family=Oswald:wght@500;600;700&display=swap'
new_fonts = 'family=Oswald:wght@500;600;700&family=Montserrat:wght@800;900&display=swap'
content = content.replace(old_fonts, new_fonts)

# 2. Add to @theme
if '--font-montserrat' not in content:
    content = content.replace("--font-oswald: 'Oswald', sans-serif;", "--font-oswald: 'Oswald', sans-serif;\n            --font-montserrat: 'Montserrat', sans-serif;")

# 3. Apply to headings
old_class = 'font-black uppercase leading-[1.25]'
new_class = 'font-montserrat font-black uppercase leading-[1.25]'
content = content.replace(old_class, new_class)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Font Montserrat applied successfully.")
