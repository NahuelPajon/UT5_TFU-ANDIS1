from pydantic import BaseModel
from typing import Literal

class OrderItemRequest(BaseModel):
    menu_item_id: int
    quantity:     int

class OrderCreateRequest(BaseModel):
    items:          list[OrderItemRequest]
    payment_method: Literal["online", "cash"]

class OrderItemDetail(BaseModel):
    menu_item_id: int
    name:         str
    quantity:     int
    unit_price:   float

class OrderResponse(BaseModel):
    id:                int
    number:            int
    status:            str
    items:             list[OrderItemDetail]
    total:             float
    payment_method:    str
    estimated_minutes: int
    created_at:        str

class OrderStatusResponse(BaseModel):
    id:     int
    number: int
    status: str

class OrderStatusUpdateRequest(BaseModel):
    status: Literal["preparing", "ready", "delivered"]

class OrderSummaryResponse(BaseModel):
    pending:   int
    preparing: int
    ready:     int
    delivered: int

class OrderTrackingStateResponse(BaseModel):
    orderStatus:   str
    estimatedTime: int
    isLoading:     bool
