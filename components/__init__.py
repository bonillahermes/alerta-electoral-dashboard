# components/__init__.py
"""
Componentes modulares del dashboard electoral
"""

from .header import render_header, render_info_banner, render_about
from .metrics import render_kpi_cards, render_regional_summary, render_top_departments
from .map import render_map, create_electoral_map
from .filters import render_filters, render_export_options

__all__ = [
    'render_header',
    'render_info_banner',
    'render_about',
    'render_kpi_cards',
    'render_regional_summary',
    'render_top_departments',
    'render_map',
    'create_electoral_map',
    'render_filters',
    'render_export_options'
]
