from fastapi import APIRouter, HTTPException
from views.payment_view import PaymentResponse
from models import payment as payment_model

router = APIRouter(prefix="/payments", tags=["Pagos"])

@router.get("/{order_id}", response_model=PaymentResponse, summary="Consultar pago de un pedido")
def get_payment(order_id: int):
    payment = payment_model.get_by_order_id(order_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return payment