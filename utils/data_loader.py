import pandas as pd
import streamlit as st

@st.cache_data
def load_electoral_data(filepath: str = 'data/alerta_georeferenciada.xlsx') -> pd.DataFrame:
    """Carga y valida datos de alerta electoral"""
    try:
        df = pd.read_excel(filepath)
        
        required_cols = ['Codigo Divipola', 'Departamento', 'Municipio', 
                        'Macrorregion', 'Llamada a la acción', 'Latitud', 'Longitud']
        
        missing = set(required_cols) - set(df.columns)
        if missing:
            st.error(f"Columnas faltantes: {missing}")
            return pd.DataFrame()
        
        # Conversión de coordenadas desde string
        # Limpiar espacios y reemplazar comas por puntos
        df['Latitud'] = df['Latitud'].astype(str).str.strip().str.replace(',', '.')
        df['Longitud'] = df['Longitud'].astype(str).str.strip().str.replace(',', '.')
        
        # Convertir a numérico
        df['Latitud'] = pd.to_numeric(df['Latitud'], errors='coerce')
        df['Longitud'] = pd.to_numeric(df['Longitud'], errors='coerce')
        
        # Eliminar registros sin coordenadas válidas
        initial_count = len(df)
        df = df.dropna(subset=['Latitud', 'Longitud'])
        dropped = initial_count - len(df)
        
        if dropped > 0:
            st.warning(f"⚠️ Se excluyeron {dropped} municipios sin coordenadas válidas")
        
        return df
    
    except FileNotFoundError:
        st.error(f"❌ Archivo no encontrado: {filepath}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Error al cargar datos: {str(e)}")
        return pd.DataFrame()


def get_summary_stats(df: pd.DataFrame) -> dict:
    """Calcula estadísticas resumen del dataset"""
    return {
        'total_municipios': len(df),
        'departamentos': df['Departamento'].nunique(),
        'macroregiones': df['Macrorregion'].nunique(),
        'por_alerta': df['Llamada a la acción'].value_counts().to_dict(),
        'por_macroregion': df['Macrorregion'].value_counts().to_dict()
    }


def filter_data(df: pd.DataFrame, 
                macroregiones: list = None, 
                alertas: list = None,
                departamentos: list = None) -> pd.DataFrame:
    """Aplica filtros múltiples al dataset"""
    filtered = df.copy()
    
    if macroregiones:
        filtered = filtered[filtered['Macrorregion'].isin(macroregiones)]
    
    if alertas:
        filtered = filtered[filtered['Llamada a la acción'].isin(alertas)]
    
    if departamentos:
        filtered = filtered[filtered['Departamento'].isin(departamentos)]
    
    return filtered
