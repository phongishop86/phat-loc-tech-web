import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

nav_pattern = r'<nav class="hidden lg:flex items-center gap-8 h-full flex-1 justify-center">.*?</nav>'

# Use a lambda function to wrap the matched string in HTML comments
if re.search(nav_pattern, content, flags=re.DOTALL):
    content = re.sub(nav_pattern, lambda m: f"<!--\n            {m.group(0)}\n            -->", content, flags=re.DOTALL)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully commented out the navigation menu.")
else:
    print("Could not find the navigation menu to comment out.")
