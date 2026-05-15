from fastapi import APIRouter, HTTPException

from database import assets, get_next_id, work_orders
from models import WorkOrder

router = APIRouter(prefix="/work-orders", tags=["work-orders"])


@router.get("/")
def list_work_orders() -> list[WorkOrder]:
    return work_orders


@router.post("/")
def create_work_order(work_order: WorkOrder) -> WorkOrder:
    asset_exists = any(asset.id == work_order.asset_id for asset in assets)

    if not asset_exists:
        raise HTTPException(status_code=400, detail="Asset does not exist")

    work_order.id = get_next_id(work_orders)
    work_orders.append(work_order)
    return work_order


@router.get("/{work_order_id}")
def get_work_order(work_order_id: int) -> WorkOrder:
    for work_order in work_orders:
        if work_order.id == work_order_id:
            return work_order

    raise HTTPException(status_code=404, detail="Work order not found")
