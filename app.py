"""
Dashboard de Alerta Temprana Electoral N°013-25
Sistema de Monitoreo de Riesgos Electorales 2025-2026
"""

import streamlit as st
import pandas as pd

# Configuración de página (debe ser la primera llamada de Streamlit)
st.set_page_config(
    page_title="Alerta Electoral N°013-25",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Importar componentes
from utils.data_loader import load_electoral_data, get_summary_stats, filter_data
from components.header import render_header, render_info_banner, render_about
from components.filters import render_filters, render_export_options
from components.metrics import render_kpi_cards, render_regional_summary, render_top_departments
from components.map import render_map

# CSS personalizado
st.markdown("""
<style>
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Ajustar padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Estilo de métricas */
    [data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: bold;
        color: #1A1A1A;
    }
    
    /* Mejorar tablas */
    .dataframe {
        font-size: 12px;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #F5F5F5;
        border-radius: 6px;
        padding: 10px 20px;
        color: #1A1A1A;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #D32F2F;
        color: white;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #F8F9FA;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """
    Función principal de la aplicación
    """
    
    # === SIDEBAR ===
    render_about()
    
    # === CARGA DE DATOS ===
    with st.spinner("🔄 Cargando datos electorales..."):
        df = load_electoral_data()
    
    if df.empty:
        st.error("❌ No se pudieron cargar los datos. Verifique el archivo.")
        st.stop()
    
    # === FILTROS ===
    selected_macro, selected_alerts, selected_dept = render_filters(df)
    
    # Aplicar filtros
    df_filtered = filter_data(df, selected_macro, selected_alerts, selected_dept)
    
    # Opciones de exportación
    render_export_options(df_filtered)
    
    # === CONTENIDO PRINCIPAL ===
    
    # Header
    render_header()
    
    # Banner informativo
    stats = get_summary_stats(df)
    render_info_banner(
        total_municipios=stats['total_municipios'],
        total_departamentos=stats['departamentos']
    )
    
    st.markdown("---")
    
    # KPI Cards
    render_kpi_cards(df_filtered)
    
    st.markdown("---")
    
    # Mapa principal
    render_map(df_filtered)
    
    st.markdown("---")
    
    # Análisis regional y departamental
    col1, col2 = st.columns([1, 1])
    
    with col1:
        render_regional_summary(df_filtered)
    
    with col2:
        render_top_departments(df_filtered, n=10)
    
    st.markdown("---")
    
    # Tabla detallada
    with st.expander("📋 Ver Tabla Completa de Datos", expanded=False):
        st.dataframe(
            df_filtered[[
                'Departamento', 
                'Municipio', 
                'Macrorregion', 
                'Llamada a la acción',
                'Codigo Divipola'
            ]].sort_values(['Departamento', 'Municipio']),
            use_container_width=True,
            height=400
        )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666666; font-size: 12px; padding: 20px 0;">
        🛡️ Dashboard desarrollado para el Ministerio del Interior<br>
        <b>Dirección para la democracia, la participación ciudadana y la acción comunal | Grupo de Asuntos Electorales</b><br>
        Desarrollado por: Hermes Yate Bonilla
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()