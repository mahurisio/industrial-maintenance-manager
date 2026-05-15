from fastapi import APIRouter

from src.database import technicians, get_next_id
from src.models import Technician

router = APIRouter(prefix="/technicians", tags=["technicians"])


@router.get("/")
def list_technicians() -> list[Technician]:
    return technicians


@router.post("/")
def create_technician(technician: Technician) -> Technician:
    technician.id = get_next_id(technicians)
    technicians.append(technician)
    return technician
