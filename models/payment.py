from models.json_db import read_json, write_json
from datetime import datetime

FILE = "orders.json"

def get_by_order_id(order_id: int) -> dict | None:
    orders = read_json(FILE)
    order = next((o for o in orders if o["id"] == order_id), None)
    if not order:
        return None
    return {
        "order_id":       order["id"],
        "payment_method": order["payment_method"],
        "total":          order["total"],
        "status":         "paid" if order["payment_method"] == "online" else "pending_cash"
    }