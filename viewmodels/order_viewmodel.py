from models import order as order_model
from viewmodels.exceptions import ResourceNotFoundError


def get_order_tracking_state(order_id: int) -> dict:
    order = order_model.get_by_id(order_id)
    if not order:
        raise ResourceNotFoundError("Pedido no encontrado")
    return {
        "orderStatus": order["status"],
        "estimatedTime": order["estimated_minutes"],
        "isLoading": False,
    }
