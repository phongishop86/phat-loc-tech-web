import json
from bs4 import BeautifulSoup
import re

html_path = 'phatdat.html'
try:
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
except FileNotFoundError:
    print("phatdat.html not found.")
    exit()

soup = BeautifulSoup(html, 'html.parser')

items = []

# Phat Dat table usually has rows. Let's find all tr elements
rows = soup.find_all('tr')
current_category = "Khác"

for row in rows:
    # A category row might just have one th or td with colspan
    th_cells = row.find_all('th')
    if th_cells and len(th_cells) == 1:
        current_category = th_cells[0].get_text(strip=True)
        continue
    
    tds = row.find_all('td')
    if len(tds) >= 4:
        # Assuming format: Code, Name, Price1, Price2, Warranty, etc.
        # Or Code, Name, Warranty, Price1, Price2
        # Let's extract the text of all columns to inspect.
        cols = [td.get_text(strip=True) for td in tds]
        
        # We need the product name and the "column 3" price.
        # Often: [0]=Code, [1]=Name, [2]=Warranty, [3]=Price 1, [4]=Price 2
        # Let's assume the user meant the last column or the highest price column if it's wholesale/retail.
        # We'll just grab the 3rd index column (which is the 4th column visually: Code, Name, BH, Gia1).
        # We will parse the prices from all columns to find the highest number to be safe or just take col 3.
        
        name = cols[1] if len(cols) > 1 else ""
        price_str = cols[3] if len(cols) > 3 else "0"
        
        # Clean price string
        price_clean = re.sub(r'[^\d]', '', price_str)
        if price_clean.isdigit() and int(price_clean) > 1000:
            price = int(price_clean)
            items.append({
                'category': current_category,
                'name': name,
                'raw_price': price,
                'new_price': int(price * 1.3)
            })

# Categorize items into Phat Loc Tech categories
# Target categories:
# - may-tinh: RAM, SSD, HDD, CPU, Mainboard, Phím Chuột, Màn hình...
# - camera: Camera, Đầu ghi, Cáp mạng, Router, Wifi...

may_tinh_keywords = ['RAM', 'SSD', 'HDD', 'CPU', 'MAIN', 'PHÍM', 'CHUỘT', 'MOUSE', 'KEYBOARD', 'MÀN HÌNH', 'LCD', 'VGA', 'NGUỒN', 'CASE', 'LAPTOP']
camera_keywords = ['CAMERA', 'ĐẦU GHI', 'WIFI', 'ROUTER', 'SWITCH', 'CÁP MẠNG', 'HIKVISION', 'DAHUA', 'IMOU', 'EZVIZ', 'TP-LINK', 'TPLINK', 'TENDA', 'RUIJIE', 'UNIFI']

may_tinh_items = []
camera_items = []

for item in items:
    # Filter out empty names
    if not item['name']: continue
    
    name_upper = item['name'].upper()
    cat_upper = item['category'].upper()
    
    is_camera = any(k in name_upper or k in cat_upper for k in camera_keywords)
    is_may_tinh = any(k in name_upper or k in cat_upper for k in may_tinh_keywords)
    
    if is_camera:
        camera_items.append(item)
    elif is_may_tinh:
        may_tinh_items.append(item)
    else:
        # If ambiguous, put in may_tinh by default if it looks like an electronic part
        may_tinh_items.append(item)

print(f"Total items parsed: {len(items)}")
print(f"Máy tính items: {len(may_tinh_items)}")
print(f"Camera items: {len(camera_items)}")

# We just want a representative 90%? We will just pick up to 50 items for each to not overload the page
# Or pick random 90%. We'll just output them to JSON so we can generate HTML.
with open('parsed_items.json', 'w', encoding='utf-8') as f:
    json.dump({
        'may_tinh': may_tinh_items,
        'camera': camera_items
    }, f, ensure_ascii=False, indent=2)

print("Saved to parsed_items.json")
