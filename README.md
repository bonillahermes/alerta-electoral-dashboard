# 🗳️ Dashboard de Alerta Temprana Electoral N°013-25

Sistema profesional de visualización geoespacial para monitoreo de riesgos electorales.

## 🚀 Instalación Rápida

```bash
# 1. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Agregar archivo de datos
# Copiar alerta_georeferenciada.xlsx a carpeta data/

# 4. Ejecutar
streamlit run app.py
```

## 📁 Estructura del Proyecto

```
alerta-electoral-dashboard/
├── app.py
├── requirements.txt
├── .streamlit/config.toml
├── data/
│   └── alerta_georeferenciada.xlsx
├── components/
│   ├── header.py
│   ├── metrics.py
│   ├── map.py
│   └── filters.py
└── utils/
    ├── config.py
    └── data_loader.py
```

## 🌐 Deploy en Streamlit Cloud

1. Crear repositorio en GitHub
2. Push del proyecto
3. Ir a share.streamlit.io
4. Conectar repositorio
5. Deploy automático

## 📝 Uso

- Filtros en sidebar
- Mapa interactivo con capas
- Exportar datos filtrados
- Vista de mapa de calor

## 📧 Soporte

Dashboard desarrollado para la Registraduría Nacional del Estado Civil de Colombia.
