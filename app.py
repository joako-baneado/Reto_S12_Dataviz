import streamlit as st
import pandas as pd
import src.data_loader as dl
import src.charts as ch

# Configuración de página
st.set_page_config(
    page_title="América Latina: ¿Crecimiento Verde o Dependencia Fósil?",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS personalizado para un acabado premium
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #264653;
        line-height: 1.2;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        font-size: 1.3rem;
        color: #555555;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    .card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #2a9d8f;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #264653;
        margin-bottom: 0.5rem;
    }
    
    .card-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #2a9d8f;
    }
    
    .card-value-red {
        font-size: 2.2rem;
        font-weight: 800;
        color: #e76f51;
    }
    
    .color-legend {
        display: flex;
        gap: 1.5rem;
        margin-bottom: 2rem;
        background: #f1f3f5;
        padding: 1rem;
        border-radius: 8px;
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.9rem;
        font-weight: 600;
    }
    
    .legend-color {
        width: 15px;
        height: 15px;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- CARGA DE DATOS -----------------

try:
    df = dl.load_data()
except Exception as e:
    st.error(f"Error al cargar el archivo de datos: {e}")
    st.stop()

# ----------------- SIDEBAR / FILTROS -----------------

st.sidebar.image("https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=300&q=80")
st.sidebar.title("Configuración del Dashboard")

st.sidebar.markdown("""
Explora y filtra los datos de consumo y transición energética en América Latina.
""")

# Selector de rango de años
year_min = int(df['year'].min())
year_max = int(df['year'].max())
selected_years = st.sidebar.slider(
    "Selecciona el Rango de Años:",
    min_value=year_min,
    max_value=year_max,
    value=(2000, 2022)
)

# Selector de países (Multiselect)
all_countries = sorted(df['country'].unique())
default_countries = ['Brazil', 'Chile', 'Colombia', 'Mexico', 'Uruguay', 'Costa Rica', 'Argentina']
selected_countries = st.sidebar.multiselect(
    "Selecciona los Países para Comparar:",
    options=all_countries,
    default=default_countries
)

# Filtrar dataframe basado en selecciones del Sidebar
df_filtered = df[
    (df['year'] >= selected_years[0]) & 
    (df['year'] <= selected_years[1]) & 
    (df['country'].isin(selected_countries))
]

# ----------------- HEADER PRINCIPAL Y STORYTELLING -----------------

st.markdown('<h1 class="main-title">América Latina: ¿Crecimiento Verde o Dependencia Fósil?</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">El contraste entre los líderes de la transición energética y los países rezagados frente al desafío climático (2000-2022)</p>', unsafe_allow_html=True)

# Leyenda de Paleta de Color Justificada
st.markdown("""
<div class="color-legend">
    <div class="legend-item">
        <div class="legend-color" style="background-color: #2a9d8f;"></div>
        <span><b>Verde Esmeralda (#2a9d8f)</b>: Energía Renovable y Sostenibilidad (Avance)</span>
    </div>
    <div class="legend-item">
        <div class="legend-color" style="background-color: #e76f51;"></div>
        <span><b>Terracota (#e76f51)</b>: Intensidad de Carbono y Emisiones (Tensión)</span>
    </div>
    <div class="legend-item">
        <div class="legend-color" style="background-color: #e9c46a;"></div>
        <span><b>Amarillo Arena (#e9c46a)</b>: Rango de Transición / Puntos Intermedios</span>
    </div>
    <div class="legend-item">
        <div class="legend-color" style="background-color: #264653;"></div>
        <span><b>Azul Slate (#264653)</b>: Contexto e Información de Soporte</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Breve introducción narrativa
st.write("""
Históricamente, América Latina ha disfrutado de una ventaja comparativa en energías limpias gracias a su abundante recurso hidroeléctrico. Sin embargo, en las últimas dos décadas, 
el rápido crecimiento de la demanda eléctrica y las sequías recurrentes han obligado a la región a tomar un camino crítico: acelerar la adopción de nuevas energías renovables (solar, eólica) 
o retroceder hacia la quema de combustibles fósiles. 

Este dashboard analiza si el desarrollo de la región está logrando **desacoplar el crecimiento económico de la contaminación ambiental**, o si por el contrario, algunos países están atrapados en su dependencia fósil.
""")

# ----------------- SECCIÓN 1: METRICAS CLAVE (KPIs) -----------------
st.markdown("### Estado Actual de la Región (Año Seleccionado / Reciente)")

latest_year = selected_years[1]
df_latest_region = df[(df['year'] == latest_year) & (df['country'].isin(selected_countries))]

if not df_latest_region.empty:
    col1, col2, col3 = st.columns(3)
    
    # KPI 1: Promedio de renovables
    avg_ren = df_latest_region['renewables_share_elec'].mean()
    col1.markdown(f"""
    <div class="card">
        <div class="card-title">Participación Promedio de Renovables ({latest_year})</div>
        <div class="card-value">{avg_ren:.1f}%</div>
        <p style="font-size: 0.85rem; color: #555;">De la electricidad generada en los países seleccionados.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # KPI 2: Intensidad de Carbono promedio
    avg_carbon = df_latest_region['carbon_intensity_elec'].mean()
    col2.markdown(f"""
    <div class="card" style="border-left-color: #e76f51;">
        <div class="card-title">Intensidad de Carbono Eléctrica ({latest_year})</div>
        <div class="card-value-red">{avg_carbon:.1f} <span style="font-size: 1.1rem; font-weight: normal;">gCO₂/kWh</span></div>
        <p style="font-size: 0.85rem; color: #555;">Emisiones de CO₂ emitidas por kilovatio-hora de electricidad.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # KPI 3: Líder de la transición
    leader_row = df_latest_region.sort_values(by='renewables_share_elec', ascending=False).iloc[0]
    col3.markdown(f"""
    <div class="card" style="border-left-color: #e9c46a;">
        <div class="card-title">Líder en Energía Limpia ({latest_year})</div>
        <div class="card-value" style="color: #e9c46a;">{leader_row['country']}</div>
        <p style="font-size: 0.85rem; color: #555;">Registra un <b>{leader_row['renewables_share_elec']:.1f}%</b> de generación eléctrica renovable.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("No hay suficientes datos disponibles para los filtros seleccionados.")

st.markdown("---")

# ----------------- SECCIÓN 2: GRÁFICO 1 - EVOLUCIÓN EN EL TIEMPO -----------------
st.markdown("### 1. La Transición en el Tiempo: A Mayor Generación Renovable, Menor Intensidad de Carbono")
st.write("""
Al analizar la relación temporal entre la participación de energía renovable y la intensidad de carbono en la generación eléctrica, 
observamos una tendencia de desacoplamiento claro: **a medida que aumenta la generación renovable (curva verde), la huella de carbono de la electricidad (curva terracota descontinua) disminuye de manera drástica**.
""")

# Selector individual de país para análisis detallado
selected_analysis_country = st.selectbox(
    "Selecciona un país para ver su curva detallada de descarbonización:",
    options=selected_countries if selected_countries else all_countries,
    index=0
)

df_country = df[(df['country'] == selected_analysis_country) & (df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]

if not df_country.empty:
    fig1 = ch.plot_decarbonization(df_country, selected_analysis_country, selected_years)
    st.plotly_chart(fig1, width="stretch")
else:
    st.info("No hay datos disponibles para el país y el rango de años seleccionados.")

st.markdown("---")

# ----------------- SECCIÓN 3: GRÁFICO 2 - PBI VS TRANSICIÓN -----------------
st.markdown("### 2. Desarrollo Sostenible: El Crecimiento Económico No Frena la Transición de la Región")
st.write("""
Desmitificando el supuesto conflicto entre desarrollo y ecología: la distribución de las burbujas demuestra que **el nivel de ingresos por habitante no determina el éxito de la transición**. Países con PBI per cápita similar toman caminos energéticos radicalmente distintos.
*El tamaño de las burbujas representa la población de cada país.*
""")

# Selector del año para el scatter plot
selected_scatter_year = st.selectbox(
    "Selecciona el año para analizar la correlación económica:",
    options=range(selected_years[0], selected_years[1] + 1),
    index=len(range(selected_years[0], selected_years[1] + 1)) - 1
)

df_scatter = df[(df['year'] == selected_scatter_year) & (df['country'].isin(selected_countries))].copy()
df_scatter = df_scatter.dropna(subset=['gdp_per_capita', 'renewables_share_elec'])

if not df_scatter.empty:
    fig2 = ch.plot_wealth_vs_renewables(df_scatter, selected_scatter_year)
    st.plotly_chart(fig2, width="stretch")
    st.caption("Nota: El tamaño de la burbuja refleja el tamaño de la población. Los países ubicados en la parte superior derecha están logrando un alto desarrollo con matrices eléctricas verdes.")
else:
    st.warning("No hay suficientes datos económicos (PBI) para los países seleccionados en el año seleccionado.")

st.markdown("---")

# ----------------- SECCIÓN 4: GRÁFICO 3 - COMPARATIVA FINAL -----------------
st.markdown("### 3. Brecha de Descarbonización al 2022: Unos Pocos Líderes Verdes frente a una Mayoría Fósil")
st.write("""
Este ranking muestra la brecha real entre los países de la región. El color de las barras ayuda a identificar inmediatamente a los **Líderes de Transición** (verde, >70%), 
aquellos en **Camino Intermedio** (amarillo, 35-70%) y los **Rezagados Fósiles** (terracota, <35%).
""")

df_compare = df[(df['year'] == latest_year) & (df['country'].isin(selected_countries))].copy()

if not df_compare.empty:
    df_compare = df_compare.sort_values(by='renewables_share_elec', ascending=True)
    fig3 = ch.plot_ranking_bar(df_compare, latest_year)
    st.plotly_chart(fig3, width="stretch")
else:
    st.warning("No hay suficientes datos disponibles para generar el ranking.")

# ----------------- FOOTER / CONCLUSIÓN NARRATIVA -----------------
st.markdown("---")
st.markdown("#### Conclusiones Clave del Storytelling")
st.markdown("""
1. **Liderazgo Verde Exitoso**: Países como **Uruguay** y **Costa Rica** demuestran que es técnicamente posible alcanzar matrices eléctricas superiores al 90% de fuentes renovables, habiendo reducido drásticamente su intensidad de carbono.
2. **El Gran Desafío de los Gigantes**: **Brasil** se beneficia enormemente de su hidroelectricidad tradicional, mientras que **México** y **Argentina** muestran un avance lento, estancados por sus abundantes reservas e infraestructura orientada a combustibles fósiles (gas y petróleo).
3. **El Camino Adelante**: La descarbonización eléctrica no depende de la riqueza del país (como demuestra el Bubble Chart), sino de la voluntad política, el marco regulatorio y la inversión planificada en energías renovables modernas (solar y eólica).
""")
