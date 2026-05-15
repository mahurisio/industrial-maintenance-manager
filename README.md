# Industrial Maintenance Manager

Sistema web en construccion para la gestion de mantenimiento industrial, ordenes de trabajo, activos, repuestos, costos y reportes tecnicos.

Este proyecto nace desde una necesidad real: muchas empresas pequenas, talleres y areas de mantenimiento todavia controlan sus intervenciones con cuadernos, hojas sueltas, archivos dispersos o conversaciones de WhatsApp. Esa forma de trabajo genera perdida de informacion, dificultad para calcular costos, poca trazabilidad y mala toma de decisiones.

La idea de este sistema es convertir la experiencia practica del mantenimiento industrial en una solucion de software organizada, medible y util.

## Objetivo del proyecto

Desarrollar una aplicacion que permita registrar, consultar y controlar informacion tecnica relacionada con mantenimiento industrial.

El sistema busca servir como una herramienta para:

- Registrar maquinas, equipos o activos.
- Crear ordenes de trabajo.
- Diferenciar mantenimientos preventivos, correctivos e inspecciones.
- Registrar repuestos, herramientas y consumibles utilizados.
- Calcular costos basicos de intervencion.
- Guardar observaciones tecnicas.
- Consultar historial de fallas.
- Generar reportes para analisis posterior.

## Contexto tecnico

Este proyecto esta construido desde mi experiencia como tecnologo en mecanica industrial, electronica industrial y soldadura, junto con mi formacion actual en Ingenieria de Software.

No es solamente un ejercicio academico. Es una forma de llevar problemas reales del mundo industrial al desarrollo de software: maquinas que fallan, mantenimientos que no quedan documentados, repuestos que se pierden, costos que no se calculan bien y decisiones que se toman sin datos.

## Tecnologias actuales

- Python
- FastAPI
- Pydantic
- Uvicorn
- Git y GitHub

## Tecnologias previstas

- Base de datos SQL
- PostgreSQL o MySQL
- HTML, CSS y JavaScript
- React en una etapa futura
- AWS para despliegue, almacenamiento, base de datos, seguridad y monitoreo

## Estructura actual del proyecto

```text
industrial-maintenance-manager/
|-- docs/
|   |-- requirements.md
|   |-- database-model.md
|   |-- project-roadmap.md
|-- src/
|   |-- main.py
|   |-- app.py
|   |-- database.py
|   |-- models.py
|   |-- readme.md
|   |-- routes/
|       |-- __init__.py
|       |-- assets.py
|       |-- work_orders.py
|-- .gitignore
|-- requirements.txt
|-- README.md
```

## Como ejecutar el proyecto en local

### 1. Clonar el repositorio

```bash
git clone https://github.com/mahurisio/industrial-maintenance-manager.git
cd industrial-maintenance-manager
```

### 2. Crear un entorno virtual

En Windows:

```bash
python -m venv .venv
.venv/Scripts/activate
```

En Linux o macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la API

```bash
uvicorn src.main:app --reload
```

Tambien se puede ejecutar desde la carpeta src con:

```bash
python main.py
```

### 5. Abrir la documentacion automatica

Despues de ejecutar el servidor, abrir en el navegador:

```text
http://localhost:8000/docs
```

Desde esa pantalla se pueden probar las rutas de la API.

## Rutas iniciales de la API

```text
GET  /
GET  /health
GET  /assets/
POST /assets/
GET  /assets/{asset_id}
GET  /work-orders/
POST /work-orders/
GET  /work-orders/{work_order_id}
```

## Relacion con AWS

A futuro, este proyecto buscara integrar servicios de AWS para darle una estructura mas profesional:

- Amazon RDS para base de datos.
- Amazon S3 para almacenamiento de evidencias tecnicas, fotos o documentos.
- IAM para control de accesos.
- VPC para una arquitectura mas segura.
- CloudWatch para monitoreo.

La intencion es que el proyecto no se quede solo en el codigo local, sino que pueda crecer hacia una solucion desplegada, segura y escalable.

## Documentacion del proyecto

- [Requisitos del proyecto](docs/requirements.md)
- [Modelo de base de datos](docs/database-model.md)
- [Roadmap del proyecto](docs/project-roadmap.md)

## Estado actual

Proyecto en fase inicial de diseno y construccion.

Ya cuenta con:

- Documentacion inicial.
- Estructura base del backend.
- Modelos principales del dominio.
- Rutas iniciales para activos y ordenes de trabajo.
- Dependencias declaradas.
- Preparacion para ejecucion local.

## Autor

Daniel Mauricio Padilla Gonzalez  
Tecnologo industrial y estudiante de Ingenieria de Software  
Manizales, Caldas, Colombia  
Sitio web: https://intecmzles.com
