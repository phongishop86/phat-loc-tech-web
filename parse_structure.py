from bs4 import BeautifulSoup
import re

with open('phatdat.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

output = []

# Find spans or divs that look exactly like prices
price_candidates = soup.find_all(string=re.compile(r'^\s*[\d\.,]{4,}\s*(?:đ|VNĐ|vnd|vnđ)?\s*$', re.I))

output.append(f"Found {len(price_candidates)} exact price candidates")

if price_candidates:
    for i in range(min(5, len(price_candidates))):
        el = price_candidates[i]
        parent = el.parent
        output.append(f"--- Price Candidate {i} ---")
        output.append(f"Tag: {parent.name}, class: {parent.get('class', [])}")
        output.append(f"Text: {el.strip()}")
        # Find the container to see the product name
        container = parent.find_parent(['li', 'div', 'tr', 'ul'])
        if container:
            output.append(f"Container tag: {container.name}, class: {container.get('class', [])}")
            # Try to get the whole text of container
            full_text = container.get_text(separator=' | ', strip=True)
            output.append(f"Full text: {full_text[:200]}")

with open('findings.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
