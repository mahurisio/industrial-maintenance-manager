# Roadmap del proyecto

Este documento organiza la ruta de trabajo del proyecto Industrial Maintenance Manager.

La idea es avanzar por fases pequeñas, defendibles y medibles. El proyecto no debe crecer de forma desordenada; cada etapa debe dejar evidencia clara en GitHub.

## Fase 1: Organización inicial del repositorio

Estado: en progreso.

Objetivo: dejar una base documental y técnica clara para que el proyecto pueda entenderse y ejecutarse.

Tareas:

- Crear README principal del proyecto.
- Crear documento de requisitos.
- Crear modelo inicial de base de datos.
- Crear estructura básica del backend.
- Agregar dependencias en `requirements.txt`.
- Agregar archivo `.gitignore`.
- Eliminar archivos de prueba que no pertenecen al proyecto.

## Fase 2: Backend inicial con FastAPI

Estado: en construcción.

Objetivo: crear una API funcional que permita registrar y consultar información básica.

Tareas:

- Crear punto de entrada con `main.py`.
- Configurar la aplicación en `app.py`.
- Definir modelos iniciales con Pydantic.
- Crear almacenamiento temporal en memoria.
- Crear rutas para activos.
- Crear rutas para órdenes de trabajo.
- Crear rutas para técnicos.
- Crear rutas para clientes.
- Crear rutas para repuestos.
- Probar la API desde `/docs`.

## Fase 3: Persistencia de datos

Estado: pendiente.

Objetivo: reemplazar el almacenamiento en memoria por una base de datos real.

Opciones iniciales:

- SQLite para pruebas locales.
- PostgreSQL para una versión más profesional.
- Amazon RDS para una etapa futura en AWS.

Tareas:

- Definir ORM o capa de acceso a datos.
- Crear migraciones.
- Conectar modelos con tablas reales.
- Probar operaciones CRUD.
- Documentar configuración local.

## Fase 4: Interfaz web

Estado: pendiente.

Objetivo: crear una interfaz visual sencilla para que el sistema pueda ser usado por personas no técnicas.

Tareas:

- Diseñar pantalla de inicio.
- Crear listado de activos.
- Crear formulario de activos.
- Crear listado de órdenes de trabajo.
- Crear formulario de órdenes de trabajo.
- Crear vista de historial técnico.
- Crear pantalla de reportes básicos.

Tecnologías posibles:

- HTML, CSS y JavaScript para una primera versión.
- React para una versión más profesional.

## Fase 5: Reportes e indicadores

Estado: pendiente.

Objetivo: transformar los datos registrados en información útil para tomar decisiones.

Tareas:

- Reporte de órdenes por estado.
- Reporte de costos por activo.
- Reporte de repuestos más usados.
- Reporte de fallas repetitivas.
- Reporte de trabajos por periodo.

## Fase 6: Integración con AWS

Estado: pendiente.

Objetivo: llevar el proyecto hacia una arquitectura más profesional en la nube.

Servicios previstos:

- Amazon RDS para base de datos.
- Amazon S3 para almacenamiento de evidencias técnicas.
- IAM para permisos y seguridad.
- VPC para aislamiento de recursos.
- CloudWatch para monitoreo.

Tareas:

- Preparar configuración de despliegue.
- Crear variables de entorno.
- Probar base de datos en Amazon RDS.
- Probar almacenamiento de evidencias en S3.
- Documentar arquitectura inicial en AWS.

## Fase 7: Evolución hacia analítica y mantenimiento predictivo

Estado: visión futura.

Objetivo: usar datos técnicos para anticipar fallas y mejorar decisiones de mantenimiento.

Tareas posibles:

- Registrar frecuencia de fallas.
- Analizar tiempos entre fallas.
- Medir costos acumulados por activo.
- Simular datos de sensores.
- Crear alertas básicas.
- Explorar modelos de análisis predictivo.

## Criterio de avance

Cada fase debe dejar evidencia clara en GitHub:

- Código organizado.
- Documentación entendible.
- Commits con mensajes claros.
- README actualizado.
- Capturas o ejemplos cuando sea necesario.

El objetivo final no es solo tener código, sino construir un portafolio profesional que muestre criterio técnico, pensamiento de software y conocimiento real del mundo industrial.
