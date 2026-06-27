import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    # Cargar directamente el CSV de la carpeta data/
    df = pd.read_csv("data/owid-energy-data (1).csv")
    
    # Países de América Latina
    lac_countries = [
        'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Costa Rica',
        'Cuba', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala',
        'Haiti', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay',
        'Peru', 'Uruguay', 'Venezuela'
    ]
    
    # Filtrar por países de AL y año >= 2000
    df_filtered = df[(df['country'].isin(lac_countries)) & (df['year'] >= 2000)].copy()
    
    # Columnas numéricas clave a limpiar
    numeric_cols = [
        'renewables_share_elec', 'carbon_intensity_elec', 'gdp', 
        'population', 'electricity_generation', 'energy_per_capita',
        'greenhouse_gas_emissions'
    ]
    
    for col in numeric_cols:
        if col in df_filtered.columns:
            df_filtered[col] = pd.to_numeric(df_filtered[col], errors='coerce')
            
    # Calcular métricas auxiliares
    df_filtered['gdp_per_capita'] = df_filtered['gdp'] / df_filtered['population']
    
    return df_filtered
