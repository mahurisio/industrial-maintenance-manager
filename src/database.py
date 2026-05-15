from src.models import Asset, Client, Technician, WorkOrder


# Almacenamiento temporal en memoria.
# Mas adelante este modulo se reemplazara por una conexion real a base de datos.
assets: list[Asset] = []
clients: list[Client] = []
technicians: list[Technician] = []
work_orders: list[WorkOrder] = []


def get_next_id(collection: list) -> int:
    """Calcula el siguiente identificador entero para una coleccion en memoria."""

    if not collection:
        return 1

    return max(item.id or 0 for item in collection) + 1
