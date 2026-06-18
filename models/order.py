from models.json_db import read_json, write_json
from datetime import datetime

FILE = "orders.json"

def get_all(status: str = None) -> list:
    orders = read_json(FILE)
    if status:
        orders = [o for o in orders if o["status"] == status]
    return orders

def get_by_id(order_id: int) -> dict | None:
    orders = read_json(FILE)
    return next((o for o in orders if o["id"] == order_id), None)

def get_summary() -> dict:
    orders = read_json(FILE)
    return {
        "pending":   sum(1 for o in orders if o["status"] == "pending"),
        "preparing": sum(1 for o in orders if o["status"] == "preparing"),
        "ready":     sum(1 for o in orders if o["status"] == "ready"),
        "delivered": sum(1 for o in orders if o["status"] == "delivered"),
    }

def create(data: dict) -> dict:
    orders = read_json(FILE)
    new_id     = max((o["id"]     for o in orders), default=0) + 1
    new_number = max((o["number"] for o in orders), default=0) + 1
    order = {
        "id":                new_id,
        "number":            new_number,
        "status":            "pending",
        "items":             data["items"],
        "total":             data["total"],
        "payment_method":    data["payment_method"],
        "estimated_minutes": 12,
        "created_at":        datetime.now().isoformat()
    }
    orders.append(order)
    write_json(FILE, orders)
    return order

def update_status(order_id: int, new_status: str) -> dict | None:
    orders = read_json(FILE)
    for order in orders:
        if order["id"] == order_id:
            order["status"] = new_status
            write_json(FILE, orders)
            return order
    return None