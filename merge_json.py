import json

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

    # Merge them
    merged_data = {}
    
    import re
    # First add computer items
    for cat, items in data_mt.items():
        for item in items:
            item['name'] = re.sub(r'\[.*?\]', '', item['name']).strip()
        merged_data[cat] = items
        
    # Then add camera items
    for cat, items in data_cm.items():
        for item in items:
            item['name'] = re.sub(r'\[.*?\]', '', item['name']).strip()
        if cat in merged_data:
            merged_data[cat].extend(items)
        else:
            merged_data[cat] = items

    with open('data/all_prices.json', 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully merged {len(data_mt)} categories from may_tinh and {len(data_cm)} categories from camera.")
    print(f"Total categories in all_prices.json: {len(merged_data)}")

if __name__ == "__main__":
    merge_json_files()
