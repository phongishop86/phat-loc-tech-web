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
    "Máy tính bộ & Laptop": [],
    "Linh kiện PC (Main, CPU, VGA, Nguồn)": [],
    "Màn hình (LCD)": [],
    "Ổ cứng (SSD/HDD)": [],
    "RAM (Bộ nhớ trong)": [],
    "Bàn phím & Chuột": [],
    "Thiết bị mạng (Wifi, Switch, Cable)": [],
    "Camera & Thiết bị an ninh": [],
    "Máy in, Mã vạch & POS": [],
    "Thiết bị Âm thanh & Loa": [],
    "Thiết bị Gia dụng": [],
    "Phần Mềm & Bản quyền": [],
    "Phụ kiện & Linh kiện khác": []
}

def get_category(name):
    n = name.upper()
    
    # 1. Nhóm Phần Mềm (Antivirus, Windows, Office...)
    if n.startswith('ANTIVIRUS') or n.startswith('KASPERSKY') or n.startswith('BKAV') or n.startswith('WINDOWS') or n.startswith('OFFICE') or n.startswith('MICROSOFT') or n.startswith('PHẦN MỀM') or 'ESET' in n:
        return "Phần Mềm & Bản quyền"
        
    # 2. Nhóm Máy tính bộ & Laptop
    if n.startswith('LAPTOP') or n.startswith('PC') or n.startswith('BỘ MÁY') or n.startswith('MÁY BỘ'):
        return "Máy tính bộ & Laptop"
        
    # 3. Nhóm RAM (Từ khóa bắt đầu: DDR, RAM, BỘ NHỚ)
    if n.startswith('DDR') or n.startswith('RAM') or n.startswith('BỘ NHỚ TRONG') or n.startswith('THANH RAM'):
        return "RAM (Bộ nhớ trong)"
        
    # 4. Nhóm Linh kiện PC (Mainboard, CPU, VGA, Nguồn, Case, Tản)
    if n.startswith('MAIN') or n.startswith('BO MẠCH') or n.startswith('CPU') or n.startswith('VGA') or n.startswith('NGUỒN') or n.startswith('PSU') or n.startswith('CASE') or n.startswith('VỎ CASE') or n.startswith('TẢN') or n.startswith('FAN') or n.startswith('QUẠT') or n.startswith('CARD MÀN HÌNH'):
        return "Linh kiện PC (Main, CPU, VGA, Nguồn)"
        
    # 5. Nhóm Ổ Cứng (Từ khóa bắt đầu: HDD, SSD, USB, THẺ NHỚ)
    if n.startswith('SSD') or n.startswith('HDD') or n.startswith('Ổ CỨNG') or n.startswith('USB') or n.startswith('THẺ NHỚ') or n.startswith('BOX Ổ CỨNG'):
        return "Ổ cứng (SSD/HDD)"
        
    # 6. Nhóm Màn hình
    if n.startswith('LCD') or n.startswith('MÀN HÌNH') or n.startswith('MONITOR'):
        return "Màn hình (LCD)"
        
    # 7. Nhóm Phím Chuột
    if n.startswith('KEYBOARD') or n.startswith('MOUSE') or n.startswith('PHÍM') or n.startswith('CHUỘT') or n.startswith('COMBO') or n.startswith('BỘ PHÍM') or n.startswith('LÓT CHUỘT') or n.startswith('PAD'):
        return "Bàn phím & Chuột"
        
    # 8. Nhóm Mạng (Cable, Switch, Router, Wifi...)
    if n.startswith('CABLE') or n.startswith('CÁP') or n.startswith('SWITCH') or n.startswith('ROUTER') or n.startswith('WIFI') or n.startswith('BỘ PHÁT') or n.startswith('BỘ CHIA') or n.startswith('HUB') or n.startswith('CARD MẠNG'):
        return "Thiết bị mạng (Wifi, Switch, Cable)"
        
    # 9. Nhóm Camera & An ninh
    if n.startswith('CAMERA') or n.startswith('WEBCAM') or n.startswith('ĐẦU GHI') or n.startswith('BALUN'):
        return "Camera & Thiết bị an ninh"
        
    # 10. Nhóm Máy in, Mã vạch
    if n.startswith('MÁY IN') or n.startswith('MÁY QUÉT') or n.startswith('MÁY ĐỌC') or n.startswith('MÃ VẠCH') or n.startswith('PRINTER') or n.startswith('CARTRIDGE') or n.startswith('MỰC IN'):
        return "Máy in, Mã vạch & POS"
        
    # 11. Nhóm Âm thanh
    if n.startswith('LOA') or n.startswith('TAI NGHE') or n.startswith('HEADPHONE') or n.startswith('MICRO'):
        return "Thiết bị Âm thanh & Loa"
        
    # 12. Nhóm Gia dụng
    if n.startswith('MÁY LÀM SỮA') or n.startswith('MÁY XAY') or n.startswith('MÁY PHA') or n.startswith('NỒI') or n.startswith('QUẠT TÍCH ĐIỆN'):
        return "Thiết bị Gia dụng"
        
    # FALLBACK cho các từ khóa ngẫu nhiên nằm ở giữa tên (nếu không theo chuẩn)
    if 'ANTIVIRUS' in n or 'KASPERSKY' in n or 'BKAV' in n: return "Phần Mềm & Bản quyền"
    if 'CAMERA' in n or 'HIKVISION' in n or 'DAHUA' in n: return "Camera & Thiết bị an ninh"
    if re.search(r'\bSSD\b', n) or re.search(r'\bHDD\b', n): return "Ổ cứng (SSD/HDD)"
    if re.search(r'\bLCD\b', n): return "Màn hình (LCD)"
    
    return "Phụ kiện & Linh kiện khác"

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
            # If name has [SP_...], [MH...] etc, clean it
            name = re.sub(r'\[.*?\]', '', name)
            name = name.strip()
            
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
