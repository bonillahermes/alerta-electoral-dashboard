# Configuración global del dashboard

# Paleta de colores por nivel de alerta
ALERT_COLORS = {
    'Inmediata': '#D32F2F',
    'Urgente': '#FF6F00',
    'Prioritaria': '#FBC02D',
    'Observación permanente': '#1976D2',
    'Ordinaria': '#66BB6A'
}

# Iconos por nivel de alerta
ALERT_ICONS = {
    'Inmediata': '🔴',
    'Urgente': '🟠',
    'Prioritaria': '🟡',
    'Observación permanente': '🔵',
    'Ordinaria': '🟢'
}

# Orden de prioridad (para ordenamiento)
ALERT_PRIORITY = {
    'Inmediata': 1,
    'Urgente': 2,
    'Prioritaria': 3,
    'Observación permanente': 4,
    'Ordinaria': 5
}

# Macrorregiones de Colombia
MACROREGIONES = [
    'Amazónica',
    'Caribe',
    'Centro Andina',
    'Noroccidente',
    'Nororiente',
    'Orinoquía',
    'Sur Occidente'
]

# Coordenadas centro de Colombia
COLOMBIA_CENTER = [4.5, -73.0]
DEFAULT_ZOOM = 6

# Configuración del mapa
MAP_CONFIG = {
    'tiles': 'CartoDB positron',
    'width': 1400,
    'height': 700
}

# Títulos y textos
DASHBOARD_TITLE = "🗳️ Alerta Temprana Electoral N°013-25"
DASHBOARD_SUBTITLE = "Monitoreo de Riesgos Electorales 2025-2026"
DATA_SOURCE = "Fuente: Defensoría del Pueblo"