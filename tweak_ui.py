import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove cart.js
content = content.replace('<script src="cart.js"></script>', '')

# 2. Move Chat Widget Button to bottom right
# <button id="chat-toggle" class="fixed bottom-6 left-6 ...">
content = content.replace(
    '<button id="chat-toggle" class="fixed bottom-6 left-6', 
    '<button id="chat-toggle" class="fixed bottom-6 right-6'
)

# 3. Move Chat Widget Panel to bottom right
# <div id="chat-panel" class="fixed bottom-24 left-6 z-[9998] ... origin-bottom-left ...">
content = content.replace(
    '<div id="chat-panel" class="fixed bottom-24 left-6',
    '<div id="chat-panel" class="fixed bottom-24 right-6'
)
content = content.replace('origin-bottom-left', 'origin-bottom-right')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully disabled cart and moved chatbot.")
