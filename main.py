from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from config.settings import settings
from controllers import (
    menu_controller,
    order_controller,
    payment_controller,
    mvvm_order_controller,
)

app = FastAPI(
    title=settings.app_name,
    description="Backend para gestión de pedidos del food truck. Incluye endpoints MVC y MVVM para demo comparativa.",
    version="1.0.0",
    openapi_tags=[
        {"name": "MVC - Menú", "description": "Endpoints originales con patrón MVC."},
        {"name": "MVC - Pedidos", "description": "Pedidos usando controllers que coordinan models y views."},
        {"name": "MVC - Pagos", "description": "Pagos usando la estructura MVC original."},
        {"name": "MVVM - Tracking", "description": "Estado de pantalla mobile expuesto por un ViewModel."},
    ],
)

mvc_routers = [
    menu_controller.router,
    order_controller.router,
    payment_controller.router,
]

mvvm_routers = [
    mvvm_order_controller.router,
]

if settings.architecture_mode in ("mvc", "both"):
    for router in mvc_routers:
        app.include_router(router)

if settings.architecture_mode in ("mvvm", "both"):
    for router in mvvm_routers:
        app.include_router(router)

app.mount("/demo", StaticFiles(directory="frontend", html=True), name="demo")
