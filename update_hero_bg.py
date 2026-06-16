with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the Unsplash image and adjust opacity
old_img = '<img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=2034&auto=format&fit=crop" \n              alt="Server Data Center" class="w-full h-full object-cover opacity-40 mix-blend-luminosity" />'
# Wait, the string in the file might have newlines differently. Let's just use string replace for parts.
content = content.replace('https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=2034&auto=format&fit=crop', 'hero-bg-tech.png')
content = content.replace('alt="Server Data Center"', 'alt="Digital Transformation Technology"')
content = content.replace('opacity-40 mix-blend-luminosity', 'opacity-60 mix-blend-lighten')
content = content.replace('from-[#03132e] via-[#041a3f]/90', 'from-[#03132e] via-[#041a3f]/70')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero background updated.")
