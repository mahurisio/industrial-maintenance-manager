from fastapi import APIRouter, HTTPException

from database import assets, get_next_id
from models import Asset

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/")
def list_assets() -> list[Asset]:
    return assets


@router.post("/")
def create_asset(asset: Asset) -> Asset:
    asset.id = get_next_id(assets)
    assets.append(asset)
    return asset


@router.get("/{asset_id}")
def get_asset(asset_id: int) -> Asset:
    for asset in assets:
        if asset.id == asset_id:
            return asset

    raise HTTPException(status_code=404, detail="Asset not found")
