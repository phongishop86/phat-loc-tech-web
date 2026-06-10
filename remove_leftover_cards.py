import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to remove the remaining cards and fix the tags
# It starts at <!-- Card 2 and goes all the way to </section>
pattern = r'<!-- Card 2: Camera giám sát -->.*?</section>'

new_section_ending = """</div>
    </section>"""

if re.search(pattern, content, flags=re.DOTALL):
    content = re.sub(pattern, new_section_ending, content, flags=re.DOTALL)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully removed the remaining 3 HTML cards.")
else:
    print("Could not find the pattern to remove.")
