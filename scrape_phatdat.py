import urllib.request
import re
import json
import math
import io
import sys
from bs4 import BeautifulSoup

# Fix windows console encoding issue if any prints are used
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = "https://phatdatcomputer.vn/bang-gia"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114.0.0.0 Safari/537.36'})

print("Fetching URL...")
try:
    html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8')
except Exception as e:
    print("Error fetching:", e)
    exit(1)

print("Parsing HTML...")
soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all('div', class_=re.compile('item|row', re.I))
print(f"Found {len(items)} rows/items.")

categories = {
    "Màn hình (LCD)": [],
    "Ổ cứng (SSD/HDD)": [],
    "RAM": [],
    "Camera": [],
    "Bàn phím & Chuột": [],
    "Thiết bị mạng (Wifi, Switch, Cable)": [],
    "Phần Mềm & Số Hóa": [],
    "Linh kiện khác": []
}

def get_category(name):
    n = name.upper()
    if 'ANTIVIRUS' in n or 'KASPERSKY' in n or 'BKAV' in n or 'WINDOWS' in n or 'OFFICE' in n or 'MICROSOFT' in n or 'PHẦN MỀM' in n or 'ESET' in n:
        return "Phần Mềm & Số Hóa"
    if 'LCD' in n or 'MÀN HÌNH' in n or 'MONITOR' in n:
        return "Màn hình (LCD)"
    if 'SSD' in n or 'HDD' in n or 'Ổ CỨNG' in n or 'USB' in n or 'THẺ NHỚ' in n:
        return "Ổ cứng (SSD/HDD)"
    if 'RAM' in n or 'BỘ NHỚ' in n:
        return "RAM"
    if 'CAMERA' in n or 'WEBCAM' in n or 'HIKVISION' in n or 'DAHUA' in n or 'EZVIZ' in n or 'KBVISION' in n:
        return "Camera"
    if 'PHÍM' in n or 'CHUỘT' in n or 'KEYBOARD' in n or 'MOUSE' in n or 'BỘ COMBO' in n:
        return "Bàn phím & Chuột"
    if 'CABLE' in n or 'CÁP' in n or 'WIFI' in n or 'SWITCH' in n or 'ROUTER' in n or 'MẠNG' in n or 'ĐẦU ĐỌC' in n or 'HUB' in n or 'LAN' in n:
        return "Thiết bị mạng (Wifi, Switch, Cable)"
    return "Linh kiện khác"

parsed_count = 0

for item in items:
    # A typical row has columns in divs or spans. 
    # Let's extract all text with a separator
    text_content = item.get_text(separator='|', strip=True)
    parts = [p.strip() for p in text_content.split('|') if p.strip()]
    
    # We expect some format like:
    # ["[SP_29997]LCD 23.8' MSI...", "Bảo hành: 36T", "Tình trạng:Liên Hệ", "(Giá đã bao gồm VAT)", "MUA HÀNG", "2.007.000đ", "2.028.000đ", "2.041.000đ"]
    
    name = ""
    warranty = ""
    price1 = price2 = price3 = 0
    prices = []
    
    for i, part in enumerate(parts):
        if part.startswith('Bảo hành:'):
            # The previous parts are likely the name
            name = " ".join(parts[:i])
            warranty = part.replace('Bảo hành:', '').strip()
            # If name has [SP_...], clean it
            name = re.sub(r'\[SP_\d+\]', '', name)
            name = re.sub(r'\[\]', '', name).strip()
            
        elif part.endswith('đ') and '.' in part:
            num_str = part.replace('đ', '').replace('.', '')
            if num_str.isdigit():
                prices.append(int(num_str))
                
    if name and len(prices) > 0:
        # Price 3 is usually the last price (consumer price)
        price_base = prices[-1]
        
        # Rule: PLT Price = Price 3 + 10%, rounded to nearest 1000
        plt_price = round((price_base * 1.1) / 1000) * 1000
        
        cat = get_category(name)
        categories[cat].append({
            "name": name,
            "price": plt_price,
            "warranty": warranty
        })
        parsed_count += 1

print(f"Successfully parsed and categorized {parsed_count} products.")

# Save to data/may_tinh_prices.json
output_file = "data/may_tinh_prices.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(categories, f, ensure_ascii=False, indent=4)

print(f"Data saved to {output_file}")
