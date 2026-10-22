ESTIMATION_EXAMPLES: list[dict] = [
    {
        "meeting_summary": (
            "El cliente opera una clínica ambulatoria con varios profesionales y necesita una "
            "plataforma web que sustituya las reservas por teléfono y hojas de cálculo. Quiere "
            "gestionar profesionales, salas y tipos de servicio con horarios semanales, un "
            "calendario que evite dobles reservas, reprogramaciones y cancelaciones con motivo, "
            "y un perfil ligero de paciente (datos de contacto y notas de visita — sin historial "
            "clínico ni facturación). Los roles son administrador, recepción y profesional. "
            "Los pacientes no inician sesión; recepción reserva en su nombre. Los recordatorios "
            "salen por correo y SMS 24 horas antes de la visita. Necesitan un informe sencillo "
            "de ocupación de salas y tasa de inasistencias. El hosting será en su cuenta AWS "
            "existente. En esta fase no hay app móvil ni integración con el software contable."
        ),
        "estimation": """\
## Plataforma de Citas para Clínica

### Desglose de tareas

| Tarea | Horas | Coste (USD) |
|-------|------:|-------------|
| Análisis de requisitos y flujos de UX | 12 | 750 |
| Esquema de base de datos y migraciones | 8 | 500 |
| Autenticación y roles (admin, recepción, profesional) | 14 | 875 |
| API de agenda (disponibilidad, conflictos, reprogramar, cancelar) | 24 | 1,500 |
| Módulo de perfil de paciente | 12 | 750 |
| Servicio de recordatorios por email y SMS | 10 | 625 |
| Calendario de reservas (frontend) | 22 | 1,375 |
| Admin: servicios, salas y horarios | 14 | 875 |
| Informes de ocupación e inasistencias | 10 | 625 |
| Testing (unitario, integración, E2E) | 18 | 1,125 |
| Revisión de código, QA y corrección de errores | 16 | 1,000 |

### Totales

- **Horas totales:** 160
- **Coste total:** 10,000 USD

### Equipo recomendado

- 1 Desarrollador Full-Stack Senior (líder)
- 1 Desarrollador Full-Stack de nivel medio
- 1 Ingeniero QA (parcial, últimas 2 semanas)

### Duración estimada

**8 semanas** con un equipo de desarrollo de dos personas.""",
    },
    {
        "meeting_summary": (
            "El cliente es un distribuidor mayorista y quiere un portal B2B para que sus "
            "minoristas consulten el catálogo con listas de precios por cliente, vean stock "
            "disponible y hagan pedidos que se sincronicen con el ERP existente. Los pedidos "
            "pasan por los estados borrador, enviado, modificado y cancelado. Los compradores "
            "deben descargar facturas y albaranes en PDF. El acceso es por cuenta de empresa, "
            "con roles de comprador y administrador de compras, más un rol interno de staff; "
            "el login debe usar el SSO del cliente. El ERP expone una API REST; los fallos de "
            "sincronización deben ir a una cola de errores que el staff pueda reintentar. "
            "Las notificaciones por email cubren confirmación de pedido y cambios de estado. "
            "No hay checkout de consumidor, captura de pagos ni app móvil: los compradores "
            "usan el navegador de escritorio."
        ),
        "estimation": """\
## Portal B2B de Pedidos Mayoristas

### Desglose de tareas

| Tarea | Horas | Coste (USD) |
|-------|------:|-------------|
| Requisitos y diseño de integración | 16 | 1,000 |
| Modelo de datos y migraciones | 12 | 750 |
| Cuentas de empresa, usuarios y SSO | 18 | 1,125 |
| API de catálogo, listas de precios y visibilidad de stock | 22 | 1,375 |
| Flujo de pedidos (borrador, enviar, modificar, cancelar) | 28 | 1,750 |
| Documentos de factura y albarán | 12 | 750 |
| Conector ERP (sync, reintentos, cola de errores) | 32 | 2,000 |
| UI del portal de clientes | 28 | 1,750 |
| Admin interno (cuentas, precios, usuarios) | 16 | 1,000 |
| Notificaciones por email | 8 | 500 |
| Testing (unitario, integración, E2E) | 28 | 1,750 |
| QA, soporte a UAT y corrección de errores | 20 | 1,250 |

### Totales

- **Horas totales:** 240
- **Coste total:** 15,000 USD

### Equipo recomendado

- 1 Desarrollador Backend Senior (líder, responsable del conector ERP)
- 1 Desarrollador Full-Stack de nivel medio
- 1 Ingeniero QA (parcial, últimas 4 semanas)

### Duración estimada

**12 semanas** con un equipo de desarrollo de dos personas.""",
    },
    {
        "meeting_summary": (
            "El cliente necesita una herramienta web interna para unos 80 empleados que "
            "soliciten ausencias y envíen partes de horas semanales. Los tipos de ausencia "
            "(vacaciones, enfermedad, no remunerada) tienen saldos anuales y una aprobación "
            "en dos pasos: responsable de línea y, si la solicitud supera cinco días, RR. HH. "
            "Los partes de horas son entradas diarias contra proyectos, se envían semanalmente "
            "y los aprueba el responsable de línea. Los empleados inician sesión con el "
            "proveedor de identidad de la empresa. Los managers necesitan un calendario de "
            "equipo y una bandeja de aprobaciones pendientes. RR. HH. necesita una exportación "
            "CSV con el formato de la gestoría de nómina. El email avisa al siguiente "
            "aprobador y al empleado cuando hay una decisión. No hay cálculo de nómina, "
            "gastos ni app móvil: se usa desde el navegador en la red de la empresa."
        ),
        "estimation": """\
## Herramienta Interna de Ausencias y Partes de Horas

### Desglose de tareas

| Tarea | Horas | Coste (USD) |
|-------|------:|-------------|
| Requisitos y mapeo de procesos | 8 | 500 |
| Esquema de base de datos y migraciones | 6 | 375 |
| SSO con el proveedor de identidad existente | 10 | 625 |
| API de solicitudes de ausencia y reglas de saldo | 16 | 1,000 |
| API de partes de horas | 12 | 750 |
| Cadenas de aprobación y notificaciones por email | 12 | 750 |
| UI de autoservicio para empleados | 16 | 1,000 |
| Aprobaciones de managers y calendario de equipo | 12 | 750 |
| Exportación CSV para nómina | 6 | 375 |
| Testing (unitario, integración, E2E) | 12 | 750 |
| Revisión de código, QA y corrección de errores | 10 | 625 |

### Totales

- **Horas totales:** 120
- **Coste total:** 7,500 USD

### Equipo recomendado

- 1 Desarrollador Full-Stack Senior (líder)
- 1 Desarrollador Full-Stack de nivel medio
- 1 Ingeniero QA (parcial, últimas 2 semanas)

### Duración estimada

**6 semanas** con un equipo de desarrollo de dos personas.""",
    },
]

def format_examples_for_prompt(examples: list[dict]) -> str:
    """Format estimation examples into a string suitable for injection into a system prompt."""
    parts: list[str] = []
    for i, example in enumerate(examples, start=1):
        parts.append(
            f"--- EXAMPLE {i} ---\n"
            f"Meeting Summary:\n{example['meeting_summary']}\n\n"
            f"Estimation:\n{example['estimation']}\n"
        )
    return "\n".join(parts)