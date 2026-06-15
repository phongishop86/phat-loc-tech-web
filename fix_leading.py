with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('leading-[1.1]', 'leading-[1.25]')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated leading to 1.25")
