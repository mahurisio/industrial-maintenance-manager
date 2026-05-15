# Requisitos del proyecto

Este documento define los requisitos iniciales del sistema Industrial Maintenance Manager. La intención es construir una aplicación web que permita controlar información técnica relacionada con mantenimiento industrial, órdenes de trabajo, activos, repuestos, costos e historial de intervenciones.

## Problema que se busca resolver

En muchos talleres, empresas pequeñas y áreas de mantenimiento, la información técnica se maneja de forma dispersa: cuadernos, hojas de cálculo, mensajes de WhatsApp, fotografías sueltas y recuerdos del técnico que atendió la falla.

Ese método puede funcionar de manera informal, pero genera problemas serios cuando se necesita consultar el historial de una máquina, calcular costos, identificar fallas repetitivas, justificar una intervención o tomar decisiones con datos.

El sistema busca organizar esa información en una plataforma sencilla, útil y orientada a la realidad del mantenimiento.

## Usuarios principales

### Administrador

Usuario encargado de gestionar el sistema, crear activos, registrar técnicos, revisar reportes y controlar la información general.

### Técnico de mantenimiento

Usuario encargado de registrar intervenciones, describir fallas, agregar repuestos utilizados, reportar observaciones y cerrar órdenes de trabajo.

### Cliente o responsable del equipo

Usuario que puede consultar el estado de una intervención, revisar historial básico y acceder a reportes cuando sea necesario.

## Requisitos funcionales iniciales

### Gestión de activos

El sistema debe permitir registrar activos técnicos como máquinas, equipos, herramientas críticas o sistemas industriales.

Cada activo debe tener como mínimo:

- Nombre del activo.
- Código o identificación interna.
- Ubicación.
- Tipo de equipo.
- Estado actual.
- Observaciones generales.

### Gestión de órdenes de trabajo

El sistema debe permitir crear órdenes de trabajo asociadas a un activo.

Cada orden debe incluir:

- Número o código de orden.
- Activo relacionado.
- Tipo de mantenimiento: preventivo, correctivo o inspección.
- Descripción del problema o actividad.
- Fecha de creación.
- Técnico responsable.
- Estado de la orden: pendiente, en proceso, finalizada o cancelada.
- Observaciones finales.

### Registro de repuestos y consumibles

El sistema debe permitir registrar repuestos, herramientas o consumibles utilizados durante una intervención.

Cada registro debe incluir:

- Nombre del repuesto o consumible.
- Cantidad usada.
- Costo unitario estimado.
- Costo total.
- Orden de trabajo asociada.

### Historial técnico

El sistema debe permitir consultar el historial de intervenciones de cada activo.

La consulta debe mostrar:

- Fechas de mantenimiento.
- Tipo de intervención.
- Fallas reportadas.
- Repuestos utilizados.
- Técnico responsable.
- Observaciones.

### Reportes básicos

El sistema debe permitir generar reportes iniciales sobre:

- Cantidad de órdenes por estado.
- Costos acumulados por activo.
- Fallas repetitivas.
- Mantenimientos realizados por periodo.
- Repuestos más utilizados.

## Requisitos no funcionales

### Usabilidad

La aplicación debe ser sencilla de usar para personas técnicas que no necesariamente tienen experiencia avanzada con software.

### Seguridad

El sistema debe manejar usuarios y roles para evitar que cualquier persona modifique información crítica.

### Trazabilidad

Cada intervención debe quedar registrada de forma clara para que pueda consultarse posteriormente.

### Escalabilidad

El proyecto debe diseñarse pensando en un crecimiento futuro, incluyendo despliegue en la nube con AWS.

### Mantenibilidad

El código debe organizarse de forma clara para facilitar mejoras, correcciones y nuevas funcionalidades.

## Alcance inicial

La primera versión del sistema se enfocará en:

- Registro de activos.
- Registro de órdenes de trabajo.
- Registro básico de repuestos y costos.
- Consulta de historial técnico.
- Documentación del proyecto.

## Alcance futuro

En versiones posteriores se podrá incluir:

- Autenticación de usuarios.
- Panel de indicadores.
- Exportación de reportes en PDF.
- Carga de fotografías como evidencia técnica.
- Integración con AWS S3 para almacenamiento.
- Uso de Amazon RDS como base de datos.
- Monitoreo con CloudWatch.
- Notificaciones por correo o WhatsApp.
- Análisis predictivo de fallas.

## Criterio de éxito

El proyecto será exitoso si logra demostrar que un problema real del mantenimiento industrial puede transformarse en una solución de software clara, documentada y técnicamente defendible.
