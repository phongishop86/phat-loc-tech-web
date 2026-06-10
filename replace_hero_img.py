import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire <div class="w-full max-w-[500px] aspect-square relative">...</div> inside the right side
# The pattern should match from <!-- Enterprise Hero Illustration Right Side --> to the end of its container div
pattern = r'(<!-- Enterprise Hero Illustration Right Side -->\s*<div class="relative hidden lg:flex items-center justify-center z-20">\s*)<div class="w-full max-w-\[500px\] aspect-square relative">.*?</div>\s*(?=</div>\s*</section>)'

# Wait, let's just use a simpler regex that replaces the specific svg block.
pattern2 = r'<div class="w-full max-w-\[500px\] aspect-square relative">.*?</div>'

# The replacement should be an image tag
replacement = """<div class="w-full max-w-[600px] relative reveal-right">
                        <div class="absolute inset-0 bg-brand-green/20 rounded-full animate-pulse blur-3xl"></div>
                        <img src="kien-tao-ha-tang-so.png" alt="Kiến tạo hạ tầng số" class="w-full h-auto relative z-10 drop-shadow-2xl hover:scale-105 transition-transform duration-500 rounded-2xl" />
                    </div>"""

# Let's write a safer replace
if re.search(pattern2, content, flags=re.DOTALL):
    # Only replace the first occurrence after <!-- Enterprise Hero Illustration Right Side -->
    parts = content.split('<!-- Enterprise Hero Illustration Right Side -->')
    if len(parts) > 1:
        right_side = re.sub(pattern2, replacement, parts[1], count=1, flags=re.DOTALL)
        content = parts[0] + '<!-- Enterprise Hero Illustration Right Side -->' + right_side
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully replaced the SVG with the image.")
    else:
        print("Could not find the Enterprise Hero Illustration Right Side comment.")
else:
    print("Could not find the container div to replace.")
