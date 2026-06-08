import json
import re

def merge_json_files():
    try:
        with open('data/may_tinh_prices.json', 'r', encoding='utf-8') as f:
            data_mt = json.load(f)
    except Exception as e:
        print("Error reading may_tinh_prices.json:", e)
        data_mt = {}

    try:
        with open('data/camera_prices.json', 'r', encoding='utf-8') as f:
            data_cm = json.load(f)
    except Exception as e:
        print("Error reading camera_prices.json:", e)
        data_cm = {}

    merged_data = {}
    
    # Process computer items
    for cat, items in data_mt.items():
        if cat not in merged_data:
            merged_data[cat] = []
        for item in items:
            item['name'] = re.sub(r'\[.*?\]', '', item['name']).strip()
            # Fix miscategorized Wi-Fi items from Software category
            if cat == "Phần Mềm & Bản quyền" and ("Wifi" in item['name'] or "Card" in item['name']):
                if "Thiết bị mạng (Wifi, Switch, Cable)" not in merged_data:
                    merged_data["Thiết bị mạng (Wifi, Switch, Cable)"] = []
                merged_data["Thiết bị mạng (Wifi, Switch, Cable)"].append(item)
            else:
                if cat == "Phần Mềm & Bản quyền":
                    item['price'] = "Liên hệ"
                merged_data[cat].append(item)
        
    # Process camera items
    for cat, items in data_cm.items():
        if cat not in merged_data:
            merged_data[cat] = []
        for item in items:
            item['name'] = re.sub(r'\[.*?\]', '', item['name']).strip()
            merged_data[cat].append(item)

    # Add custom software products
    software_cat = "Phần Mềm & Bản quyền"
    if software_cat not in merged_data:
        merged_data[software_cat] = []
    
    custom_software = [
        {"name": "Kaspersky Internet Security (1 thiết bị/1 năm)", "price": "Liên hệ", "warranty": "Theo thời hạn bản quyền"},
        {"name": "Kaspersky Total Security (1 thiết bị/1 năm)", "price": "Liên hệ", "warranty": "Theo thời hạn bản quyền"},
        {"name": "Kaspersky Anti-Virus (1 thiết bị/1 năm)", "price": "Liên hệ", "warranty": "Theo thời hạn bản quyền"},
        {"name": "BKAV Pro Internet Security (1 thiết bị/1 năm)", "price": "Liên hệ", "warranty": "Theo thời hạn bản quyền"},
        {"name": "Microsoft Windows 11 Home FPP Bản Quyền (USB/Key)", "price": "Liên hệ", "warranty": "Trọn đời máy"},
        {"name": "Microsoft Windows 11 Pro OEM Bản Quyền (Theo máy)", "price": "Liên hệ", "warranty": "Trọn đời máy"},
        {"name": "Microsoft Office 365 Personal (1 thiết bị/1 năm)", "price": "Liên hệ", "warranty": "12 Tháng"},
        {"name": "Microsoft Office Home & Business 2021 FPP", "price": "Liên hệ", "warranty": "Trọn đời máy"},
        {"name": "ESET Internet Security (1 thiết bị/1 năm)", "price": "Liên hệ", "warranty": "Theo thời hạn bản quyền"}
    ]
    
    # Prepend custom software to the top of the category
    merged_data[software_cat] = custom_software + merged_data[software_cat]

    with open('data/all_prices.json', 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully merged data.")
    print(f"Total categories in all_prices.json: {len(merged_data)}")

if __name__ == "__main__":
    merge_json_files()
