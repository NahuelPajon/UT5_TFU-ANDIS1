from models.json_db import read_json

FILE = "menu.json"

def get_all(category: str = None) -> list:
    items = read_json(FILE)
    if category:
        items = [i for i in items if i["category"] == category]
    return items

def get_by_id(item_id: int) -> dict | None:
    items = read_json(FILE)
    return next((i for i in items if i["id"] == item_id), None)
