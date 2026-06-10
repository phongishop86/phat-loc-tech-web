import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<div class="relative z-10 w-full max-w-7xl mx-auto px-6 grid lg:grid-cols-\[1\.1fr_1fr\] gap-16 items-center">.*?</section>'

replacement = """<div class="relative z-10 w-full max-w-[1400px] mx-auto px-6 flex justify-center items-center">
                  <div class="w-full relative reveal-up flex justify-center">
                      <div class="absolute inset-0 bg-secondary/10 rounded-full animate-pulse blur-3xl"></div>
                      <img src="kien-tao-ha-tang-so.png" alt="Kiến tạo hạ tầng số" class="w-full h-auto max-w-[1200px] relative z-10 drop-shadow-2xl hover:scale-[1.01] transition-transform duration-500 rounded-2xl" />
                  </div>
              </div>
          </section>"""

if re.search(pattern, content, flags=re.DOTALL):
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced Hero content with the full-width image.")
else:
    print("Could not find the target pattern.")
