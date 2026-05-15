# Industrial Maintenance Manager

Sistema web en construcción para la gestión de mantenimiento industrial, órdenes de trabajo, activos, repuestos, costos y reportes técnicos.

Este proyecto nace desde una necesidad real: muchas empresas pequeñas, talleres y áreas de mantenimiento todavía controlan sus intervenciones con cuadernos, hojas sueltas, archivos dispersos o conversaciones de WhatsApp. Esa forma de trabajar puede servir por un tiempo, pero termina generando pérdida de información, dificultad para calcular costos, poca trazabilidad y mala toma de decisiones.

La idea de este sistema es convertir la experiencia práctica del mantenimiento industrial en una solución de software organizada, medible y útil.

## Objetivo del proyecto

Desarrollar una aplicación que permita registrar, consultar y controlar información técnica relacionada con mantenimiento industrial.

El sistema busca servir como una herramienta para:

- Registrar máquinas, equipos o activos.
- Crear órdenes de trabajo.
- Diferenciar mantenimientos preventivos y correctivos.
- Registrar repuestos, herramientas y consumibles utilizados.
- Calcular costos básicos de intervención.
- Guardar observaciones técnicas.
- Consultar historial de fallas.
- Generar reportes para análisis posterior.

## Contexto técnico

Este proyecto está construido desde mi experiencia como tecnólogo en mecánica industrial, electrónica industrial y soldadura, junto con mi formación actual en Ingeniería de Software.

No es solamente un ejercicio académico. Es una forma de llevar problemas reales del mundo industrial al desarrollo de software: máquinas que fallan, mantenimientos que no quedan documentados, repuestos que se pierden, costos que no se calculan bien y decisiones que se toman sin datos.

## Tecnologías previstas

El proyecto se desarrollará progresivamente con tecnologías como:

- Python
- FastAPI o Django
- HTML, CSS y JavaScript
- Base de datos SQL
- Git y GitHub
- AWS para futuras pruebas de despliegue, almacenamiento, base de datos y monitoreo

## Módulos iniciales

### Gestión de activos

Registro de máquinas, equipos o elementos técnicos con información básica como nombre, código, ubicación, estado y observaciones.

### Órdenes de trabajo

Creación y seguimiento de trabajos de mantenimiento, incluyendo tipo de intervención, descripción del problema, técnico responsable, fecha, estado y resultado.

### Repuestos y costos

Registro de repuestos utilizados, cantidades, valor estimado y costo total de la intervención.

### Historial técnico

Consulta de intervenciones anteriores para identificar fallas repetitivas, equipos críticos y patrones de mantenimiento.

### Reportes

Generación de reportes básicos para analizar trabajos realizados, costos acumulados y frecuencia de fallas.

## Relación con AWS

A futuro, este proyecto buscará integrar servicios de AWS para darle una estructura más profesional:

- Amazon RDS para base de datos.
- Amazon S3 para almacenamiento de evidencias técnicas, fotos o documentos.
- IAM para control de accesos.
- VPC para una arquitectura más segura.
- CloudWatch para monitoreo.

La intención es que el proyecto no se quede solo en el código local, sino que pueda crecer hacia una solución desplegada, segura y escalable.

## Estado actual

Proyecto en fase inicial de diseño y construcción.

Próximos pasos:

- Definir estructura de carpetas.
- Diseñar modelo de base de datos.
- Crear primeras pantallas.
- Implementar registro de activos.
- Implementar órdenes de trabajo.
- Documentar instalación y uso.

## Autor

Daniel Mauricio Padilla González  
Tecnólogo industrial y estudiante de Ingeniería de Software  
Manizales, Caldas, Colombia  
Sitio web: https://intecmzles.com
