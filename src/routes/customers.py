from fastapi import APIRouter

from src.database import clients, get_next_id
from src.models import Client

router = APIRouter(prefix="/customers", tags=["customers"])


@router.get("/")
def list_customers() -> list[Client]:
    return clients


@router.post("/")
def create_customer(customer: Client) -> Client:
    customer.id = get_next_id(clients)
    clients.append(customer)
    return customer
