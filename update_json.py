import os
import json
import urllib.request
import re
from bs4 import BeautifulSoup
import math

def main():
    print("Fetching phatdat.html...")
    req = urllib.request.Request('https://phatdatcomputer.vn/bang-gia', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    product_rows = soup.find_all('div', class_='row_title2')
    items = []
    
    for row in product_rows:
        text_nodes = [t for t in row.stripped_strings]
        name = ""
        warranty = "12 tháng"
        price = 0
        
        for t in text_nodes:
            if t.startswith('[SP_'): continue
            if len(t) > 10 and 'Bảo hành' not in t and 'Tình trạng' not in t and 'MUA' not in t and 'Giá' not in t:
                name = t
                break
                
        for i, t in enumerate(text_nodes):
            if 'Bảo hành' in t:
                if ':' in t and t.split(':')[1].strip():
                    w_text = t.split(':')[1].strip()
                elif i + 1 < len(text_nodes) and 'Tình trạng' not in text_nodes[i+1]:
                    w_text = text_nodes[i+1].replace(':', '').strip()
                else:
                    w_text = "12 tháng"
                
                w_text = re.sub(r'(?i)(\d+)\s*T\b', r'\g<1> tháng', w_text)
                
                if w_text.strip().upper() == 'T':
                    w_text = '1 tháng'
                elif w_text.strip().upper() == 'BH':
                    w_text = '12 tháng'
                elif not re.search(r'\d', w_text) and 'test' not in w_text.lower():
                    # Nếu không có số nào và không phải bao test
                    if 'tháng' not in w_text.lower():
                        w_text = w_text + " tháng"
                        
                warranty = w_text
                
            if 'Giá' in t:
                price_text = ''
                if ':' in t and t.split(':')[1].strip():
                    price_text = t.split(':')[1].strip()
                elif i + 1 < len(text_nodes):
                    price_text = text_nodes[i+1].strip()
                
                price_digits = re.sub(r'[^\d]', '', price_text)
                if price_digits:
                    price = int(price_digits)
                
        c4 = row.find('div', class_='c4')
        c3 = row.find('div', class_='c3')
        price_str = None
        if c4: price_str = c4.get_text(strip=True)
        elif c3: price_str = c3.get_text(strip=True)
            
        if price_str and price == 0:
            price_clean = re.sub(r'[^\d]', '', price_str)
            if price_clean.isdigit(): price = int(price_clean)
                
        if name and price > 1000:
            retail_price = math.ceil((price * 1.15) / 1000) * 1000
            
            if not warranty or warranty == 'Tình trạng':
                warranty = '12 tháng'
                
            items.append({'name': name, 'warranty': warranty, 'price': retail_price})

    def is_camera_network(name):
        n = name.upper()
        
        if n.startswith('MÁY IN') or n.startswith('MÁY PHOTO') or 'UPS' in n or 'BỘ LƯU ĐIỆN' in n or 'MÁY CHẤM CÔNG' in n:
            return False 
            
        if n.startswith('LAPTOP') or n.startswith('BỘ MÁY') or n.startswith('MÁY TÍNH ĐỂ BÀN') or n.startswith('MAINBOARD') or n.startswith('MAIN') or n.startswith('VGA') or n.startswith('CPU') or n.startswith('LCD') or n.startswith('RAM') or n.startswith('DDR') or n.startswith('KIT DDR') or n.startswith('NGUỒN') or n.startswith('CASE') or n.startswith('MOUSE') or n.startswith('KEYBOARD') or n.startswith('CHUỘT') or n.startswith('BÀN PHÍM') or n.startswith('COMBO') or n.startswith('HDD') or n.startswith('SSD') or n.startswith('M.2') or n.startswith('M2') or n.startswith('NVME') or n.startswith('Ổ CỨNG DI ĐỘNG SSD') or n.startswith('TẢN NHIỆT') or n.startswith('FAN'):
            return False
            
        camera_network_keywords = ['CAMERA', 'ĐẦU GHI', 'HIKVISION', 'DAHUA', 'IMOU', 'EZVIZ', 'CÁP MẠNG', 'CABLE LAN', 'WIFI', 'ROUTER', 'SWITCH', 'TP-LINK', 'TPLINK', 'TENDA', 'RUIJIE', 'UNIFI', 'PHÁT WIFI', 'MESH WIFI', 'USB WIFI', 'USB THU WIFI', 'CARD THU WIFI', 'KÍCH SÓNG', 'ĐẦU BẤM', 'ĐẦU MẠNG', 'ĐẦU NỐI LAN', 'ĐẦU BỌC', 'CARD LAN', 'KỀM BẤM', 'WEBCAM', 'THẺ NHỚ', 'MICROSD']
        return any(k in n for k in camera_network_keywords)

    def categorize_camera(name):
        n = name.upper()
        
        if 'SWITCH' in n: return 'Switch (Bộ Chia Mạng)'
        if n.startswith('KỀM BẤM') or n.startswith('ĐẦU BẤM') or n.startswith('ĐẦU MẠNG') or n.startswith('ĐẦU NỐI LAN') or n.startswith('ĐẦU BỌC'): return 'Kềm / Đầu bấm mạng'
        if 'CÁP MẠNG' in n or 'CABLE' in n or 'DÂY' in n: return 'Cáp Mạng & Dây Điện'
        
        if n.startswith('PHÁT WIFI') or n.startswith('ROUTER WIFI') or n.startswith('MESH WIFI') or 'USB WIFI' in n or 'USB THU WIFI' in n or 'CARD THU WIFI' in n or n.startswith('KÍCH SÓNG') or n.startswith('CARD LAN') or any(k in n for k in ['ROUTER', 'TPLINK', 'TP-LINK', 'TENDA', 'RUIJIE', 'UNIFI', 'MERCUSYS']): return 'Thiết Bị Mạng'
        
        if n.startswith('BỘ KIT CAMERA') or n.startswith('KIT CAMERA'): return 'Camera IP / Wifi'
        
        if 'THẺ NHỚ' in n or 'MICROSD' in n: return 'Thẻ Nhớ'
        
        if n.startswith('ĐẦU GHI'): return 'Đầu Ghi Hình'
        if 'CAMERA IP' in n or ('WIFI' in n and ('CAMERA' in n or 'EZVIZ' in n or 'IMOU' in n)) or 'EZVIZ' in n or 'IMOU' in n: return 'Camera IP / Wifi'
        if n.startswith('CAMERA') or 'TVI' in n or 'CVI' in n or 'HIK' in n or 'DAHUA' in n: return 'Camera Đồng Trục'
        
        if 'WEBCAM' in n: return 'Webcam'
        
        if 'WIFI' in n: return 'Thiết Bị Mạng'
        
        return 'Phụ Kiện Khác'
        
    def categorize_pc(name):
        n = name.upper()
        
        if n.startswith('MÁY IN') or n.startswith('MÁY PHOTO'): return 'Máy in/ Máy photocopy'
        if 'UPS' in n or 'BỘ LƯU ĐIỆN' in n: return 'UPS (Bộ Lưu Điện)'
        if 'MÁY CHẤM CÔNG' in n: return 'Máy Chấm Công'
        
        if n.startswith('CPU'): return 'CPU (Vi Xử Lý)'
        if n.startswith('VGA'): return 'Card Màn Hình (VGA)'
        if n.startswith('MAINBOARD') or n.startswith('MAIN'): return 'Mainboard (Bo Mạch Chủ)'
        if n.startswith('LCD'): return 'Màn Hình (LCD)'
        if n.startswith('NGUỒN'): return 'Nguồn Máy Tính'
        if n.startswith('MOUSE') or n.startswith('KEYBOARD') or n.startswith('CHUỘT') or n.startswith('BÀN PHÍM') or n.startswith('COMBO KBM') or n.startswith('COMBO KEYBOARD') or n.startswith('COMBO CÓ DÂY KEYBOARD') or n.startswith('COMBO KO DÂY KEYBOARD'): return 'Phím / Chuột'
        if n.startswith('CASE'): return 'Vỏ Case'
        
        if n.startswith('HDD'): return 'Ổ Cứng HDD'
        if n.startswith('SSD') or n.startswith('M.2') or n.startswith('M2') or n.startswith('NVME') or n.startswith('Ổ CỨNG DI ĐỘNG SSD'): return 'Ổ Cứng SSD/M.2'
        
        if n.startswith('RAM') or n.startswith('DDR') or n.startswith('KIT DDR'): return 'RAM (Bộ Nhớ Trong)'
        if n.startswith('LAPTOP') or 'WIN11' in n or 'WIN10' in n or '14FHD' in n or '15.6FHD' in n or 'MACBOOK' in n or 'SURFACE' in n: return 'Laptop'
        if n.startswith('BỘ MÁY') or n.startswith('MÁY TÍNH ĐỂ BÀN'): return 'Máy Bộ (PC)'
        
        if n.startswith('TẢN NHIỆT') or n.startswith('FAN') or n.startswith('ĐẾ TẢN NHIỆT'): return 'Tản Nhiệt (Cooler)'
        
        return 'Phụ Kiện Khác'

    camera_categories = {}
    pc_categories = {}
    
    for item in items:
        if is_camera_network(item['name']):
            cat = categorize_camera(item['name'])
            if cat not in camera_categories: camera_categories[cat] = []
            camera_categories[cat].append(item)
        else:
            cat = categorize_pc(item['name'])
            if cat not in pc_categories: pc_categories[cat] = []
            pc_categories[cat].append(item)
            
    # Sort keys
    camera_categories = dict(sorted(camera_categories.items()))
    pc_categories = dict(sorted(pc_categories.items()))
    
    # Move "Phụ Kiện Khác" to bottom if exists
    if 'Phụ Kiện Khác' in camera_categories:
        v = camera_categories.pop('Phụ Kiện Khác')
        camera_categories['Phụ Kiện Khác'] = v
        
    if 'Phụ Kiện Khác' in pc_categories:
        v = pc_categories.pop('Phụ Kiện Khác')
        pc_categories['Phụ Kiện Khác'] = v
            
    os.makedirs('data', exist_ok=True)
    with open('data/camera_prices.json', 'w', encoding='utf-8') as f:
        json.dump(camera_categories, f, ensure_ascii=False, indent=2)
    with open('data/may_tinh_prices.json', 'w', encoding='utf-8') as f:
        json.dump(pc_categories, f, ensure_ascii=False, indent=2)
        
    print(f"Dumped Camera: {sum(len(v) for v in camera_categories.values())} items")
    print(f"Dumped PC: {sum(len(v) for v in pc_categories.values())} items")

if __name__ == "__main__":
    main()
