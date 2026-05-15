from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    app = FastAPI(
        title="Industrial Maintenance Manager",
        description="API para gestionar activos, órdenes de trabajo, repuestos, técnicos y clientes en procesos de mantenimiento industrial.",
        version="0.1.0",
    )

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
