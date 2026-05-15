from fastapi import FastAPI

from src.routes import assets_router, work_orders_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    app = FastAPI(
        title="Industrial Maintenance Manager",
        description="API para gestionar activos, ordenes de trabajo, repuestos, tecnicos y clientes en procesos de mantenimiento industrial.",
        version="0.1.0",
    )

    app.include_router(assets_router)
    app.include_router(work_orders_router)

    @app.get("/")
    def root() -> dict[str, str]:
        return {
            "message": "Industrial Maintenance Manager API",
            "status": "running",
        }

    @app.get("/health")
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return app
