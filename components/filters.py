import streamlit as st
import pandas as pd
from utils.config import ALERT_ICONS, ALERT_PRIORITY

def render_filters(df: pd.DataFrame) -> tuple:
    """
    Renderiza controles de filtrado en sidebar
    
    Returns:
        Tupla (macroregiones, alertas, departamentos) seleccionados
    """
    st.sidebar.markdown("## Filtros")
    
    # Filtro por Macrorregión
    st.sidebar.markdown("### Macrorregión")
    all_macro = st.sidebar.checkbox("Todas las macroregiones", value=True)
    
    if all_macro:
        selected_macro = None
    else:
        selected_macro = st.sidebar.multiselect(
            "Seleccione macroregiones:",
            options=sorted(df['Macrorregion'].unique()),
            default=None
        )
    
    st.sidebar.markdown("---")
    
    # Filtro por Tipo de Alerta
    st.sidebar.markdown("### ⚠️ Tipo de Alerta")
    
    # Crear opciones con iconos
    alert_options = sorted(
        df['Llamada a la acción'].unique(),
        key=lambda x: ALERT_PRIORITY[x]
    )
    
    alert_display = {
        alert: f"{ALERT_ICONS[alert]} {alert}" 
        for alert in alert_options
    }
    
    selected_alerts = st.sidebar.multiselect(
        "Seleccione niveles de alerta:",
        options=alert_options,
        format_func=lambda x: alert_display[x],
        default=None
    )
    
    st.sidebar.markdown("---")
    
    # Filtro por Departamento
    st.sidebar.markdown("### 🏛️ Departamento")
    
    # Búsqueda de departamento
    search_dept = st.sidebar.text_input(
        "Buscar departamento:",
        placeholder="Escriba para buscar..."
    )
    
    dept_options = sorted(df['Departamento'].unique())
    
    if search_dept:
        dept_options = [d for d in dept_options if search_dept.lower() in d.lower()]
    
    selected_dept = st.sidebar.multiselect(
        "Seleccione departamentos:",
        options=dept_options,
        default=None
    )
    
    st.sidebar.markdown("---")
    
    # Botón de reset
    if st.sidebar.button("🔄 Limpiar Filtros", use_container_width=True):
        st.rerun()
    
    # Mostrar resumen de filtros activos
    active_filters = []
    if selected_macro:
        active_filters.append(f"{len(selected_macro)} macroregión(es)")
    if selected_alerts:
        active_filters.append(f"{len(selected_alerts)} tipo(s) de alerta")
    if selected_dept:
        active_filters.append(f"{len(selected_dept)} departamento(s)")
    
    if active_filters:
        st.sidebar.info(f"**Filtros activos:** {', '.join(active_filters)}")
    
    return selected_macro, selected_alerts, selected_dept


def render_export_options(df: pd.DataFrame):
    """
    Opciones para exportar datos filtrados
    """
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📥 Exportar Datos")
    
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        # Exportar a CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📄 CSV",
            data=csv,
            file_name="alerta_electoral_filtrado.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    with col2:
        # Exportar a Excel
        from io import BytesIO
        buffer = BytesIO()
        df.to_excel(buffer, index=False, engine='openpyxl')
        excel_data = buffer.getvalue()
        
        st.download_button(
            label="📊 Excel",
            data=excel_data,
            file_name="alerta_electoral_filtrado.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
    
    # Resumen de registros
    st.sidebar.metric("Registros visibles", len(df))