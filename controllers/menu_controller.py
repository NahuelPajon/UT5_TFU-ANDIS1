from fastapi import APIRouter, HTTPException
from views.menu_view import MenuItemResponse
from models import menu_item as menu_model

router = APIRouter(prefix="/menu", tags=["MVC - Menú"])

@router.get("/", response_model=list[MenuItemResponse], summary="Obtener menú completo")
def get_menu(category: str = None):
    return menu_model.get_all(category)

@router.get("/{item_id}", response_model=MenuItemResponse, summary="Obtener ítem del menú")
def get_menu_item(item_id: int):
    item = menu_model.get_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Ítem no encontrado")
    return item
