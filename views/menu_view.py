from pydantic import BaseModel

class MenuItemResponse(BaseModel):
    id:          int
    name:        str
    category:    str
    price:       float
    available:   bool
    description: str