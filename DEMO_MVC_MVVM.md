# Demo MVC vs MVVM

La API deja MVC como backend REST completo y agrega una demo MVVM enfocada en una pantalla mobile de tracking.

## MVC

Endpoints originales:

- `GET /menu/`
- `GET /menu/{item_id}`
- `GET /orders/`
- `GET /orders/summary`
- `GET /orders/{order_id}`
- `GET /orders/{order_id}/status`
- `POST /orders/`
- `PATCH /orders/{order_id}/status`
- `GET /payments/{order_id}`

Flujo:

`Controller -> Model -> View`

En esta version el controller recibe el request, consulta los models, aplica parte de la logica y devuelve schemas de `views/`.

## MVVM

Endpoint de demo:

- `GET /mvvm/orders/{order_id}/tracking`

Flujo:

`View -> Controller -> ViewModel -> Model`

En esta version el controller queda como capa HTTP fina. El ViewModel mantiene y expone el estado que necesita la pantalla mobile de seguimiento. En una app con interfaz grafica, la View se suscribe a ese estado mediante data binding. En esta API REST no hay una View viva ni binding automatico, por eso la idea se muestra de forma adaptada: el endpoint consulta el estado expuesto por el ViewModel y FastAPI lo presenta como JSON.

El ViewModel no importa `views/` ni conoce los schemas de respuesta. Solo devuelve estado simple (`dict` o `list`). Los schemas siguen declarados en el controller con `response_model`.

Para mostrar la pantalla mobile de la slide, usar:

```http
GET /mvvm/orders/{order_id}/tracking
```

Respuesta esperada:

```json
{
  "orderStatus": "ready",
  "estimatedTime": 12,
  "isLoading": false
}
```

Ese endpoint representa el estado que observaria la pantalla del cliente. En una app mobile real, la View se redibujaria cuando cambien esas propiedades.

## Comparacion clave

MVC devuelve datos del recurso:

```http
GET /orders/{order_id}
```

MVVM devuelve estado de pantalla:

```http
GET /mvvm/orders/{order_id}/tracking
```

La diferencia no es que un endpoint haga lo mismo con otro nombre. La diferencia es que MVC responde una operacion de backend, mientras que MVVM modela lo que necesita una View.

## Como mostrarlo en Swagger

1. Levantar la API.
2. Entrar a `http://localhost:8000/docs`.
3. Ejecutar:

```http
GET /orders/{order_id}
GET /mvvm/orders/{order_id}/tracking
```

La primera respuesta es la orden completa. La segunda respuesta es estado listo para la pantalla del cliente.
