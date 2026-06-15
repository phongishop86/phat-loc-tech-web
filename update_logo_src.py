with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('src="PLT-Logo-final.png"', 'src="PLT-Logo-final-transparent.png"')
content = content.replace('object-contain"', 'object-contain mix-blend-multiply"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML updated.")
