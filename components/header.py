import streamlit as st
from datetime import datetime as dt

def render_header():
    """
    Renderiza encabezado ejecutivo profesional
    """
    fecha_actual = dt.now().strftime('%d de %B de %Y - %H:%M')
    
    st.markdown(f"""
    <div style="
        background: #FFFFFF;
        padding: 40px 30px;
        border-bottom: 3px solid #C62828;
        margin-bottom: 40px;
    ">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="flex: 1;">
                <div style="
                    font-size: 11px;
                    letter-spacing: 2px;
                    color: #666666;
                    font-weight: 600;
                    margin-bottom: 8px;
                ">Fuente: Defensoría del Pueblo</div>
                <h1 style="
                    margin: 0;
                    color: #1A1A1A;
                    font-size: 32px;
                    font-weight: 600;
                    letter-spacing: -0.5px;
                ">
                    Alerta Temprana Electoral N°013-25
                </h1>
                <p style="
                    margin: 8px 0 0 0;
                    color: #666666;
                    font-size: 14px;
                    font-weight: 400;
                ">
                    Sistema de Monitoreo de Riesgos Electorales | Procesos 2025-2026
                </p>
            </div>
            <div style="
                text-align: right;
                font-size: 11px;
                color: #999999;
                line-height: 1.6;
            ">
                <div style="font-weight: 600; color: #666666;">Dirección para la democracia, la participación ciudadana y la acción comunal</div>
                <div>Grupo de Asuntos Electorales</div>
                <div style="margin-top: 8px; color: #999999;">Actualizado: {fecha_actual}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_info_banner(total_municipios: int, total_departamentos: int):
    """
    Banner ejecutivo con métricas principales
    """
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: #FFFFFF;
            padding: 24px;
            border-radius: 4px;
            border: 1px solid #E0E0E0;
            text-align: center;
        ">
            <div style="
                font-size: 36px;
                font-weight: 600;
                color: #1A1A1A;
                margin-bottom: 8px;
            ">{total_municipios:,}</div>
            <div style="
                font-size: 11px;
                letter-spacing: 1px;
                color: #666666;
                font-weight: 500;
            ">MUNICIPIOS</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: #FFFFFF;
            padding: 24px;
            border-radius: 4px;
            border: 1px solid #E0E0E0;
            text-align: center;
        ">
            <div style="
                font-size: 36px;
                font-weight: 600;
                color: #1A1A1A;
                margin-bottom: 8px;
            ">{total_departamentos}</div>
            <div style="
                font-size: 11px;
                letter-spacing: 1px;
                color: #666666;
                font-weight: 500;
            ">DEPARTAMENTOS</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 24px;
            border-radius: 4px;
            border: 1px solid #E0E0E0;
            text-align: center;
        ">
            <div style="
                font-size: 36px;
                font-weight: 600;
                color: #1A1A1A;
                margin-bottom: 8px;
            ">7</div>
            <div style="
                font-size: 11px;
                letter-spacing: 1px;
                color: #666666;
                font-weight: 500;
            ">MACRORREGIONES</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="
            background: #FFFFFF;
            padding: 24px;
            border-radius: 4px;
            border: 1px solid #E0E0E0;
            text-align: center;
        ">
            <div style="
                font-size: 36px;
                font-weight: 600;
                color: #1A1A1A;
                margin-bottom: 8px;
            ">2025-26</div>
            <div style="
                font-size: 11px;
                letter-spacing: 1px;
                color: #666666;
                font-weight: 500;
            ">PERÍODO ELECTORAL</div>
        </div>
        """, unsafe_allow_html=True)


def render_about():
    """
    Información institucional en sidebar
    """
    st.sidebar.markdown("---")
    
    with st.sidebar.expander("Acerca del sistema"):
        st.markdown("""
        **Sistema de Alerta Temprana Electoral**
        
        Herramienta de visualización geoespacial para el monitoreo 
        y seguimiento de riesgos electorales en el territorio nacional.
        
        **Clasificación de alertas:**
        - **Inmediata**: Intervención inmediata requerida
        - **Urgente**: Alta prioridad de atención
        - **Prioritaria**: Atención preferencial
        - **Observación permanente**: Monitoreo continuo
        - **Ordinaria**: Seguimiento estándar
        
        ---
        
        **Información institucional:**
        
        Defensoría del Pueblo  
        Dirección para la democracia, la participación ciudadana y la acción comunal
        Grupo de Asuntos Electorales
        
        **Responsable técnico:**  
        Hermes Yate Bonilla
        
        **Versión:** 1.0.0  
        **Año:** 2025
        """)
    
    with st.sidebar.expander("Instructivo de uso"):
        st.markdown("""
        **Navegación del sistema:**
        
        1. Utilice los filtros laterales para segmentar información
        2. Interactúe con el mapa haciendo clic en los marcadores
        3. Analice las métricas en los paneles superiores
        4. Exporte los datos mediante los botones de descarga
        5. Active/desactive capas con el control del mapa
        
        **Funciones avanzadas:**
        
        - Vista de mapa de calor para concentración de riesgos
        - Análisis comparativo por macrorregiones
        - Rankings de departamentos críticos
        - Exportación en formatos CSV y Excel
        """)
    
    st.sidebar.markdown("---")
    st.sidebar.caption("© 2025 Defensoría del Pueblo de Colombia")
