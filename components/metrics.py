import streamlit as st
import pandas as pd
from utils.config import ALERT_COLORS, ALERT_PRIORITY

def render_kpi_cards(df: pd.DataFrame):
    """
    Tarjetas KPI con diseño ejecutivo minimalista
    """
    st.markdown("""
    <div style="
        font-size: 14px;
        font-weight: 600;
        color: #1A1A1A;
        margin-bottom: 20px;
        letter-spacing: 0.5px;
    ">DISTRIBUCIÓN DE ALERTAS POR NIVEL</div>
    """, unsafe_allow_html=True)
    
    # Obtener conteos por tipo de alerta
    alert_counts = df['Llamada a la acción'].value_counts()
    
    # Ordenar por prioridad
    alert_order = sorted(ALERT_PRIORITY.keys(), key=lambda x: ALERT_PRIORITY[x])
    
    # Crear 5 columnas
    cols = st.columns(5)
    
    alert_labels = {
        'Inmediata': 'INMEDIATA',
        'Urgente': 'URGENTE',
        'Prioritaria': 'PRIORITARIA',
        'Observación permanente': 'MONITOREO',
        'Ordinaria': 'ORDINARIA'
    }
    
    for idx, alert_type in enumerate(alert_order):
        count = alert_counts.get(alert_type, 0)
        percentage = (count / len(df) * 100) if len(df) > 0 else 0
        
        with cols[idx]:
            st.markdown(f"""
            <div style="
                background: #FFFFFF;
                border: 1px solid #E0E0E0;
                border-left: 4px solid {ALERT_COLORS[alert_type]};
                padding: 20px 16px;
                border-radius: 4px;
                text-align: center;
            ">
                <div style="
                    font-size: 32px;
                    font-weight: 600;
                    color: {ALERT_COLORS[alert_type]};
                    margin-bottom: 8px;
                ">{count:,}</div>
                <div style="
                    font-size: 10px;
                    letter-spacing: 1px;
                    color: #666666;
                    font-weight: 600;
                    margin-bottom: 4px;
                ">{alert_labels[alert_type]}</div>
                <div style="
                    font-size: 11px;
                    color: #999999;
                ">{percentage:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)


def render_regional_summary(df: pd.DataFrame):
    """
    Análisis ejecutivo por macrorregión
    """
    st.markdown("""
    <div style="
        font-size: 14px;
        font-weight: 600;
        color: #1A1A1A;
        margin-bottom: 20px;
        letter-spacing: 0.5px;
    ">ANÁLISIS POR MACRORREGIÓN</div>
    """, unsafe_allow_html=True)
    
    # Agrupar por macrorregión
    regional = df.groupby(['Macrorregion', 'Llamada a la acción']).size().unstack(fill_value=0)
    
    # Calcular alertas críticas (Inmediata + Urgente)
    if 'Inmediata' in regional.columns and 'Urgente' in regional.columns:
        regional['Críticas'] = regional['Inmediata'] + regional['Urgente']
    else:
        regional['Críticas'] = 0
    
    regional['Total'] = regional.sum(axis=1)
    regional = regional.sort_values('Críticas', ascending=False)
    
    # Mostrar tabla
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Renombrar columnas para presentación ejecutiva
        display_df = regional[['Inmediata', 'Urgente', 'Prioritaria', 'Críticas', 'Total']].copy()
        display_df.columns = ['Inmediatas', 'Urgentes', 'Prioritarias', 'Críticas', 'Total']
        
        st.dataframe(
            display_df,
            use_container_width=True,
            height=280
        )
    
    with col2:
        st.markdown("""
        <div style="
            font-size: 12px;
            font-weight: 600;
            color: #666666;
            margin-bottom: 12px;
            letter-spacing: 0.5px;
        ">REGIONES PRIORITARIAS</div>
        """, unsafe_allow_html=True)
        
        for region in regional.head(3).index:
            criticas = regional.loc[region, 'Críticas']
            total = regional.loc[region, 'Total']
            pct = (criticas / total * 100) if total > 0 else 0
            
            st.markdown(f"""
            <div style="
                background: #FFFFFF;
                padding: 16px;
                border-radius: 4px;
                margin-bottom: 12px;
                border: 1px solid #E0E0E0;
                border-left: 3px solid #C62828;
            ">
                <div style="
                    font-weight: 600;
                    color: #1A1A1A;
                    font-size: 13px;
                    margin-bottom: 6px;
                ">{region}</div>
                <div style="
                    font-size: 11px;
                    color: #666666;
                    line-height: 1.5;
                ">
                    {criticas:,} alertas críticas ({pct:.1f}%)<br>
                    {total:,} municipios bajo monitoreo
                </div>
            </div>
            """, unsafe_allow_html=True)


def render_top_departments(df: pd.DataFrame, n: int = 10):
    """
    Ranking de departamentos con alertas críticas
    """
    st.markdown(f"""
    <div style="
        font-size: 14px;
        font-weight: 600;
        color: #1A1A1A;
        margin-bottom: 20px;
        letter-spacing: 0.5px;
    ">TOP {n} DEPARTAMENTOS CON ALERTAS CRÍTICAS</div>
    """, unsafe_allow_html=True)
    
    # Filtrar solo alertas críticas
    critical = df[df['Llamada a la acción'].isin(['Inmediata', 'Urgente'])]
    
    if len(critical) > 0:
        dept_counts = critical['Departamento'].value_counts().head(n)
        
        # Crear gráfico de barras
        chart_data = pd.DataFrame({
            'Departamento': dept_counts.index,
            'Alertas Críticas': dept_counts.values
        })
        
        st.bar_chart(
            chart_data.set_index('Departamento'),
            color='#C62828',
            height=400
        )
    else:
        st.info("No se registran alertas críticas en los datos filtrados")