from fastapi import APIRouter, HTTPException
from views.order_view import OrderTrackingStateResponse
from viewmodels import order_viewmodel
from viewmodels.exceptions import ResourceNotFoundError

router = APIRouter(prefix="/mvvm/orders", tags=["MVVM - Tracking"])


@router.get(
    "/{order_id}/tracking",
    response_model=OrderTrackingStateResponse,
    summary="Estado para pantalla mobile del cliente",
)
def get_order_tracking(order_id: int):
    try:
        return order_viewmodel.get_order_tracking_state(order_id)
    except ResourceNotFoundError as exc:
        raise HTTPException(status_code=404, detail=exc.detail) from exc
