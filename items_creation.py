import sqlite3
import json

def export_items_to_json():



    conn = sqlite3.connect('Archandia_db.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT itemId, itemTypeKindId, name, image_source, itemRarityTypeId, colorId, description
        FROM items_database
    """)
    items = []
    for row in cursor.fetchall():
        itemId, itemTypeKindId, name, image_source, itemRarityTypeId, colorId, description = row
        item = {
            "itemId": itemId,
            "itemTypeKindId": itemTypeKindId,
            "obrazek": image_source,
            "nazwa": name,
            "rodzaj": itemTypeKindId,
            "unikalnosc": itemRarityTypeId,
            "opis": description,
            "color": colorId
        }
        items.append(item)
    conn.close()

    with open("items.JSON", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=4)

# Wywołanie funkcji
export_items_to_json()