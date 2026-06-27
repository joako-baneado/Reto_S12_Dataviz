import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_decarbonization(df_country, selected_analysis_country, selected_years):
    fig1 = make_subplots(
        rows=2, cols=1, 
        shared_xaxes=True, 
        vertical_spacing=0.12,
        subplot_titles=(
            "Participación de Energía Renovable en la Electricidad (%)", 
            "Intensidad de Carbono de la Generación Eléctrica (gCO₂/kWh)"
        )
    )
    
    fig1.add_trace(go.Scatter(
        x=df_country['year'],
        y=df_country['renewables_share_elec'],
        name="% Elec. Renovable",
        line=dict(color='#2a9d8f', width=4),
        mode='lines+markers'
    ), row=1, col=1)
    
    fig1.add_trace(go.Scatter(
        x=df_country['year'],
        y=df_country['carbon_intensity_elec'],
        name="Intensidad de Carbono",
        line=dict(color='#e76f51', width=4, dash='dash'),
        mode='lines+markers'
    ), row=2, col=1)
    
    fig1.update_layout(
        title=dict(
            text=f"Trayectoria de Descarbonización Eléctrica en {selected_analysis_country} ({selected_years[0]}-{selected_years[1]})",
            font=dict(size=18, family='Outfit')
        ),
        xaxis2=dict(title="Año", gridcolor='#e9ecef'),
        xaxis=dict(gridcolor='#e9ecef'),
        yaxis1=dict(
            range=[-5, 105],
            gridcolor='#e9ecef'
        ),
        yaxis2=dict(
            gridcolor='#e9ecef'
        ),
        showlegend=False,
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(l=50, r=50, t=80, b=50),
        height=600
    )
    
    # ----------------- ANOTACIONES NARRATIVAS DINÁMICAS (FASE 4) -----------------
    if selected_analysis_country == 'Uruguay':
        fig1.add_annotation(
            x=2015,
            y=90,
            xref="x",
            yref="y",
            text="<b>Revolución Eólica</b>:<br>Uruguay multiplicó su energía eólica,<br>reduciendo a casi cero su dependencia del petróleo.",
            showarrow=True,
            arrowhead=2,
            arrowcolor="#264653",
            ax=-100,
            ay=30,
            bgcolor="#f1f3f5",
            bordercolor="#2a9d8f",
            borderwidth=2,
            borderpad=4
        )
    elif selected_analysis_country == 'Costa Rica':
        fig1.add_annotation(
            x=2015,
            y=98,
            xref="x",
            yref="y",
            text="<b>Liderazgo Histórico</b>:<br>Costa Rica ha mantenido casi un 100%<br>de electricidad limpia gracias a su matriz hidro y geotérmica.",
            showarrow=True,
            arrowhead=2,
            arrowcolor="#264653",
            ax=-80,
            ay=50,
            bgcolor="#f1f3f5",
            bordercolor="#2a9d8f",
            borderwidth=2,
            borderpad=4
        )
    elif selected_analysis_country == 'Chile':
        fig1.add_annotation(
            x=2021,
            y=55,
            xref="x",
            yref="y",
            text="<b>Auge Solar y Descarbonización</b>:<br>Chile acelera su transición solar en el desierto de Atacama,<br>reduciendo significativamente la intensidad de CO2.",
            showarrow=True,
            arrowhead=2,
            arrowcolor="#264653",
            ax=-120,
            ay=-50,
            bgcolor="#f1f3f5",
            bordercolor="#2a9d8f",
            borderwidth=2,
            borderpad=4
        )
    elif selected_analysis_country == 'Mexico':
        fig1.add_annotation(
            x=2018,
            y=16,
            xref="x",
            yref="y",
            text="<b>Estancamiento Fósil</b>:<br>A pesar de su gran potencial solar y eólico,<br>la matriz mexicana sigue dependiendo de gas y combustóleo.",
            showarrow=True,
            arrowhead=2,
            arrowcolor="#264653",
            ax=60,
            ay=-40,
            bgcolor="#f1f3f5",
            bordercolor="#e76f51",
            borderwidth=2,
            borderpad=4
        )
    else:
        max_yr = df_country['year'].max()
        max_ren_val = df_country[df_country['year'] == max_yr]['renewables_share_elec'].values[0]
        fig1.add_annotation(
            x=max_yr,
            y=max_ren_val,
            xref="x",
            yref="y",
            text=f"<b>Estado al {max_yr}</b>:<br>{max_ren_val:.1f}% de renovables.",
            showarrow=True,
            arrowhead=1,
            ax=-50,
            ay=-30,
            bgcolor="#f1f3f5",
            bordercolor="#264653"
        )
    return fig1

def plot_wealth_vs_renewables(df_scatter, selected_scatter_year):
    fig2 = px.scatter(
        df_scatter,
        x='gdp_per_capita',
        y='renewables_share_elec',
        size='population',
        color='country',
        hover_name='country',
        size_max=60,
        labels={
            'gdp_per_capita': 'PBI per Cápita (USD Ajustado)',
            'renewables_share_elec': '% de Electricidad Renovable',
            'population': 'Población'
        },
        title=f"En {selected_scatter_year}, las economías con mayor PBI per cápita no necesariamente lideran en energía limpia"
    )
    
    fig2.update_layout(
        xaxis=dict(gridcolor='#e9ecef', title_font=dict(family='Outfit')),
        yaxis=dict(gridcolor='#e9ecef', range=[-5, 105], title_font=dict(family='Outfit')),
        paper_bgcolor='white',
        plot_bgcolor='white',
        height=500,
        legend_title="Países"
    )
    return fig2

def plot_ranking_bar(df_compare, latest_year):
    def assign_color(row):
        val = row['renewables_share_elec']
        if val > 70:
            return '#2a9d8f'
        elif val >= 35:
            return '#e9c46a'
        else:
            return '#e76f51'
            
    df_compare['color'] = df_compare.apply(assign_color, axis=1)
    
    fig3 = go.Figure()
    
    fig3.add_trace(go.Bar(
        y=df_compare['country'],
        x=df_compare['renewables_share_elec'],
        orientation='h',
        marker_color=df_compare['color'],
        text=df_compare['renewables_share_elec'].apply(lambda x: f"{x:.1f}%"),
        textposition='outside',
        hoverinfo='y+x'
    ))
    
    fig3.update_layout(
        title=dict(
            text=f"Participación de Renovables al {latest_year}: Uruguay y Costa Rica lideran, México y Argentina se rezagan",
            font=dict(size=18, family='Outfit')
        ),
        xaxis=dict(
            title="% Participación Renovables",
            range=[0, 115],
            gridcolor='#e9ecef'
        ),
        yaxis=dict(gridcolor='#e9ecef'),
        paper_bgcolor='white',
        plot_bgcolor='white',
        height=500,
        margin=dict(l=100, r=50, t=50, b=50)
    )
    return fig3
