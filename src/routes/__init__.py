from src.routes.assets import router as assets_router
from src.routes.customers import router as customers_router
from src.routes.technicians import router as technicians_router
from src.routes.work_orders import router as work_orders_router

__all__ = [
    "assets_router",
    "customers_router",
    "technicians_router",
    "work_orders_router",
]
