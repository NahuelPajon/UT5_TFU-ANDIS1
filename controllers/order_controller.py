from fastapi import APIRouter, HTTPException
from views.order_view import (
    OrderCreateRequest, OrderResponse,
    OrderStatusResponse, OrderStatusUpdateRequest,
    OrderSummaryResponse
)
from models import order as order_model
from models import menu_item as menu_model

router = APIRouter(prefix="/orders", tags=["Pedidos"])

@router.get("/summary", response_model=OrderSummaryResponse, summary="Contadores por estado")
def get_summary():
    return order_model.get_summary()

@router.get("/", response_model=list[OrderResponse], summary="Listar pedidos")
def get_orders(status: str = None):
    return order_model.get_all(status)

@router.get("/{order_id}", response_model=OrderResponse, summary="Obtener pedido por ID")
def get_order(order_id: int):
    order = order_model.get_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return order

@router.get("/{order_id}/status", response_model=OrderStatusResponse, summary="Consultar estado")
def get_order_status(order_id: int):
    order = order_model.get_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return order

@router.post("/", response_model=OrderResponse, summary="Crear nuevo pedido")
def create_order(data: OrderCreateRequest):
    items_detail = []
    total = 0
    for item in data.items:
        menu_item = menu_model.get_by_id(item.menu_item_id)
        if not menu_item:
            raise HTTPException(status_code=404, detail=f"Ítem {item.menu_item_id} no encontrado")
        if not menu_item["available"]:
            raise HTTPException(status_code=400, detail=f"{menu_item['name']} no está disponible")
        subtotal = menu_item["price"] * item.quantity
        total += subtotal
        items_detail.append({
            "menu_item_id": item.menu_item_id,
            "name":         menu_item["name"],
            "quantity":     item.quantity,
            "unit_price":   menu_item["price"]
        })
    order = order_model.create({
        "items":          items_detail,
        "total":          total,
        "payment_method": data.payment_method
    })
    return order

@router.patch("/{order_id}/status", response_model=OrderResponse, summary="Actualizar estado del pedido")
def update_order_status(order_id: int, data: OrderStatusUpdateRequest):
    order = order_model.update_status(order_id, data.status)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return order