from pydantic import BaseModel

class PaymentResponse(BaseModel):
    order_id:       int
    payment_method: str
    total:          float
    status:         str