# Modelo de base de datos

Este documento describe el modelo de datos inicial del proyecto Industrial Maintenance Manager.

La primera versión del sistema trabajará con una estructura sencilla, pensada para registrar activos, clientes, técnicos, órdenes de trabajo, repuestos y el historial de mantenimiento.

## Objetivo del modelo

El modelo de base de datos busca organizar la información crítica del mantenimiento industrial para que pueda consultarse, analizarse y escalarse en el futuro.

La intención no es crear una base de datos compleja desde el primer día, sino diseñar una estructura clara que pueda crecer hacia PostgreSQL, MySQL o Amazon RDS cuando el proyecto llegue a una etapa de despliegue en AWS.

## Entidades principales

### clients

Representa a los clientes o empresas que solicitan trabajos de mantenimiento.

Campos iniciales:

| Campo | Tipo | Descripción |
|---|---|---|
| id | integer | Identificador único del cliente. |
| name | string | Nombre del cliente o empresa. |
| contact_name | string | Persona de contacto. |
| phone | string | Teléfono de contacto. |
| email | string | Correo electrónico. |
| address | string | Dirección del cliente. |

Relación principal:

Un cliente puede tener varios activos y varias órdenes de trabajo.

### assets

Representa máquinas, equipos, herramientas críticas o sistemas técnicos que requieren mantenimiento.

Campos iniciales:

| Campo | Tipo | Descripción |
|---|---|---|
| id | integer | Identificador único del activo. |
| name | string | Nombre del activo. |
| code | string | Código interno o placa del equipo. |
| location | string | Ubicación física del activo. |
| equipment_type | string | Tipo de equipo o máquina. |
| status | string | Estado: activo, inactivo o en mantenimiento. |
| notes | text | Observaciones generales. |
| client_id | integer | Cliente asociado al activo. |

Relación principal:

Un activo puede tener muchas órdenes de trabajo.

### technicians

Representa los técnicos encargados de realizar las intervenciones.

Campos iniciales:

| Campo | Tipo | Descripción |
|---|---|---|
| id | integer | Identificador único del técnico. |
| full_name | string | Nombre completo del técnico. |
| specialty | string | Especialidad técnica. |
| phone | string | Teléfono. |
| email | string | Correo electrónico. |

Relación principal:

Un técnico puede estar asociado a muchas órdenes de trabajo.

### work_orders

Representa las órdenes de trabajo de mantenimiento.

Campos iniciales:

| Campo | Tipo | Descripción |
|---|---|---|
| id | integer | Identificador único de la orden. |
| order_code | string | Código de la orden de trabajo. |
| asset_id | integer | Activo relacionado. |
| client_id | integer | Cliente relacionado. |
| technician_id | integer | Técnico responsable. |
| maintenance_type | string | Preventivo, correctivo o inspección. |
| status | string | Pendiente, en curso, terminada o cancelada. |
| description | text | Descripción de la falla o actividad. |
| created_at | date | Fecha de creación. |
| closed_at | date | Fecha de cierre. |
| final_notes | text | Observaciones finales. |

Relación principal:

Una orden de trabajo pertenece a un activo, puede estar asociada a un cliente y puede tener un técnico responsable.

### spare_parts

Representa repuestos, herramientas o consumibles utilizados en una orden de trabajo.

Campos iniciales:

| Campo | Tipo | Descripción |
|---|---|---|
| id | integer | Identificador único del repuesto. |
| work_order_id | integer | Orden de trabajo asociada. |
| name | string | Nombre del repuesto o consumible. |
| quantity | decimal | Cantidad utilizada. |
| unit_cost | decimal | Costo unitario estimado. |
| total_cost | decimal | Costo total calculado. |

Relación principal:

Una orden de trabajo puede tener varios repuestos asociados.

## Relaciones generales

```text
clients 1 ──── * assets
clients 1 ──── * work_orders
assets 1 ──── * work_orders
technicians 1 ──── * work_orders
work_orders 1 ──── * spare_parts
```

## Reglas iniciales de negocio

- Una orden de trabajo debe estar asociada a un activo existente.
- Un activo puede existir sin órdenes de trabajo previas.
- Un técnico puede existir aunque todavía no tenga órdenes asignadas.
- Una orden puede no tener repuestos si la intervención fue solo inspección o diagnóstico.
- El costo total de repuestos se calcula con cantidad por costo unitario.
- El historial técnico de un activo se construye a partir de sus órdenes de trabajo.

## Estados propuestos

### Estado del activo

- active
- inactive
- under_maintenance

### Estado de la orden de trabajo

- pending
- in_progress
- completed
- cancelled

### Tipo de mantenimiento

- preventive
- corrective
- inspection

## Evolución futura

Cuando el proyecto avance, este modelo podrá crecer con nuevas tablas como:

- users
- roles
- permissions
- maintenance_plans
- maintenance_evidence
- attachments
- notifications
- audit_logs

También se podrá migrar el almacenamiento inicial hacia una base de datos real, primero local y luego en AWS mediante Amazon RDS.
