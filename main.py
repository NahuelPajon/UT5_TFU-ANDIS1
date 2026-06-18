from fastapi import FastAPI
from config.settings import settings
from controllers import order_controller, menu_controller, payment_controller

app = FastAPI(
    title=settings.app_name,
    description="Backend para gestión de pedidos del food truck",
    version="1.0.0"
)

app.include_router(menu_controller.router)
app.include_router(order_controller.router)
app.include_router(payment_controller.router)