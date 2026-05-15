from datetime import date
from enum import Enum
from pydantic import BaseModel, Field


class AssetStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    UNDER_MAINTENANCE = "under_maintenance"


class WorkOrderStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class MaintenanceType(str, Enum):
    PREVENTIVE = "preventive"
    CORRECTIVE = "corrective"
    INSPECTION = "inspection"


class Asset(BaseModel):
    id: int | None = None
    name: str = Field(..., min_length=2)
    code: str = Field(..., min_length=2)
    location: str
    equipment_type: str
    status: AssetStatus = AssetStatus.ACTIVE
    notes: str | None = None


class Technician(BaseModel):
    id: int | None = None
    full_name: str = Field(..., min_length=3)
    specialty: str | None = None
    phone: str | None = None
    email: str | None = None


class Client(BaseModel):
    id: int | None = None
    name: str = Field(..., min_length=2)
    contact_name: str | None = None
    phone: str | None = None
    email: str | None = None
    address: str | None = None


class SparePart(BaseModel):
    id: int | None = None
    name: str = Field(..., min_length=2)
    quantity: float = Field(..., ge=0)
    unit_cost: float = Field(..., ge=0)

    @property
    def total_cost(self) -> float:
        return self.quantity * self.unit_cost


class WorkOrder(BaseModel):
    id: int | None = None
    order_code: str = Field(..., min_length=2)
    asset_id: int
    client_id: int | None = None
    technician_id: int | None = None
    maintenance_type: MaintenanceType
    status: WorkOrderStatus = WorkOrderStatus.PENDING
    description: str
    created_at: date = Field(default_factory=date.today)
    closed_at: date | None = None
    final_notes: str | None = None
    spare_parts: list[SparePart] = Field(default_factory=list)

    @property
    def total_spare_parts_cost(self) -> float:
        return sum(part.total_cost for part in self.spare_parts)
