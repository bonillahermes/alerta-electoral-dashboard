import folium
from folium import plugins
import streamlit as st
from streamlit_folium import folium_static
import pandas as pd
from utils.config import ALERT_COLORS, COLOMBIA_CENTER, DEFAULT_ZOOM, MAP_CONFIG

def create_electoral_map(df: pd.DataFrame) -> folium.Map:
    """
    Crea mapa interactivo de alertas electorales
    
    Args:
        df: DataFrame con datos georeferenciados
        
    Returns:
        Objeto folium.Map
    """
    # Inicializar mapa
    m = folium.Map(
        location=COLOMBIA_CENTER,
        zoom_start=DEFAULT_ZOOM,
        tiles=MAP_CONFIG['tiles'],
        control_scale=True
    )
    
    # Agregar control de capas
    feature_groups = {}
    
    # Crear grupos por tipo de alerta
    for alert_type in df['Llamada a la acción'].unique():
        feature_groups[alert_type] = folium.FeatureGroup(name=alert_type)
    
    # Agregar marcadores
    for _, row in df.iterrows():
        alert_type = row['Llamada a la acción']
        
        # Popup con información detallada
        popup_html = f"""
        <div style="font-family: Arial; width: 200px;">
            <h4 style="margin: 0; color: {ALERT_COLORS[alert_type]};">
                {row['Municipio']}
            </h4>
            <hr style="margin: 5px 0;">
            <p style="margin: 3px 0;"><b>Departamento:</b> {row['Departamento']}</p>
            <p style="margin: 3px 0;"><b>Macrorregión:</b> {row['Macrorregion']}</p>
            <p style="margin: 3px 0;"><b>Alerta:</b> {alert_type}</p>
            <p style="margin: 3px 0; font-size: 10px; color: gray;">
                Código: {row['Codigo Divipola']}
            </p>
        </div>
        """
        
        # Crear marcador circular
        folium.CircleMarker(
            location=[row['Latitud'], row['Longitud']],
            radius=7,
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=f"{row['Municipio']} - {alert_type}",
            color=ALERT_COLORS[alert_type],
            fill=True,
            fillColor=ALERT_COLORS[alert_type],
            fillOpacity=0.7,
            weight=2
        ).add_to(feature_groups[alert_type])
    
    # Agregar grupos al mapa
    for group in feature_groups.values():
        group.add_to(m)
    
    # Agregar control de capas
    folium.LayerControl(collapsed=False).add_to(m)
    
    # Agregar minimap
    minimap = plugins.MiniMap(toggle_display=True)
    m.add_child(minimap)
    
    # Agregar medidor de coordenadas
    plugins.MousePosition().add_to(m)
    
    # Agregar botón de pantalla completa
    plugins.Fullscreen(
        position='topright',
        title='Pantalla completa',
        title_cancel='Salir de pantalla completa',
        force_separate_button=True
    ).add_to(m)
    
    return m


def render_map(df: pd.DataFrame):
    """
    Renderiza el mapa en Streamlit
    """
    if df.empty:
        st.warning("⚠️ No hay datos para visualizar")
        return
    
    st.markdown("### Mapa de Alertas Electorales")
    
    # Crear tabs para diferentes vistas
    tab1, tab2 = st.tabs(["Vista General", "Mapa de Calor"])
    
    with tab1:
        m = create_electoral_map(df)
        folium_static(m, width=MAP_CONFIG['width'], height=MAP_CONFIG['height'])
        
        # Leyenda personalizada
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
            border: 1px solid #E0E0E0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        ">
            <b style="color: #1A1A1A;">💡 Funcionalidades del mapa:</b>
            <ul style="font-size: 12px; margin: 5px 0; color: #555555;">
                <li>Clic en marcadores para ver detalles del municipio</li>
                <li>Use el control de capas (esquina superior derecha) para filtrar alertas</li>
                <li>Botón de pantalla completa disponible</li>
                <li>Minimapa en esquina inferior izquierda</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        # Mapa de calor
        heat_map = create_heat_map(df)
        folium_static(heat_map, width=MAP_CONFIG['width'], height=MAP_CONFIG['height'])


def create_heat_map(df: pd.DataFrame) -> folium.Map:
    """
    Crea mapa de calor basado en concentración de alertas críticas
    """
    m = folium.Map(
        location=COLOMBIA_CENTER,
        zoom_start=DEFAULT_ZOOM,
        tiles=MAP_CONFIG['tiles']
    )
    
    # Filtrar solo alertas críticas
    critical = df[df['Llamada a la acción'].isin(['Inmediata', 'Urgente'])]
    
    if len(critical) > 0:
        # Preparar datos para heatmap
        heat_data = [[row['Latitud'], row['Longitud']] for _, row in critical.iterrows()]
        
        # Agregar heatmap
        plugins.HeatMap(
            heat_data,
            min_opacity=0.3,
            max_zoom=18,
            radius=15,
            blur=20,
            gradient={
                '0.0': 'blue',
                '0.5': 'yellow',
                '0.7': 'orange',
                '1.0': 'red'
            }
        ).add_to(m)
    
    return m