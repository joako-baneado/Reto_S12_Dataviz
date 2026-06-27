# Reporte Ejecutivo de Desarrollo y Visualización de Datos
## Proyecto: "El Dashboard que Convence" - Estado de la Energía Limpia en América Latina
**Curso:** Data Visualization  
**Modalidad:** Grupal (Consultoría para ONG Internacional)  
**Entregable Adicional:** Reporte Metodológico y Técnico del Dashboard  

---

# 1. Marco Estratégico Inicial y Storytelling

El diseño del dashboard se estructuró bajo los lineamientos metodológicos de **Cole Nussbaumer Knaflic** en su obra *Storytelling with Data*. Se definió el marco contextual estratégico antes de proceder con el código:

*   **Audiencia (El Quién):** Donantes internacionales de una ONG interesada en el financiamiento de proyectos de desarrollo sostenible y descarbonización en América Latina. La audiencia requiere un balance entre rigurosidad técnica y una narrativa visual clara y asimilable sin excesivo esfuerzo cognitivo.
*   **Acción Deseada (El Qué):** Convencer a los donantes de que la inversión en energías renovables modernas (eólica, solar) en América Latina es un camino de alta efectividad, demostrando que es viable descarbonizar la matriz eléctrica regional sin comprometer el desarrollo económico (PBI).
*   **Rol de los Datos (El Cómo):** Evidencia empírica extraída del dataset de consumo energético de *Our World in Data*.
*   **La Gran Idea:** *"América Latina demuestra que el auge de nuevas tecnologías renovables permite desacoplar el crecimiento económico de la contaminación, reduciendo drásticamente la intensidad de carbono de su electricidad."*
*   **La Historia de 3 Minutos:** *"América Latina tiene una base hidroeléctrica fuerte pero vulnerable a sequías. A través de este análisis, vemos que países pequeños como Uruguay y Costa Rica han liderado con éxito una transición hacia energías eólicas y solares, logrando desplomar su intensidad de carbono a niveles cercanos a cero. El análisis del PBI per Cápita nos revela que el desarrollo económico no es una barrera para descarbonizar, sino una oportunidad. Sin embargo, persiste una brecha crítica: mientras unos pocos países lideran el cambio verde, los gigantes industriales como México y Argentina permanecen rezagados en su dependencia de hidrocarburos."*

---

# 2. Paleta de Color Narrativa Justificada (Paleta 1)

Para evitar saturar la memoria visual de la audiencia, limitamos el uso a un máximo de 4 colores activos con intenciones semánticas claras:

| Color | Hex | Función Narrativa | Justificación Psicológica / Diseño |
|---|---|---|---|
| **Verde Esmeralda** | `#2a9d8f` | Avance y Sostenibilidad | Representa el progreso ecológico y el porcentaje de participación de energías renovables. |
| **Terracota / Naranja-Rojo** | `#e76f51` | Emisiones y Tensión Fósil | Color de contraste y advertencia. Se usa para la intensidad de carbono (gCO₂/kWh) y países rezagados. |
| **Amarillo Arena** | `#e9c46a` | Estado Intermedio / Transición | Color neutro secundario para países que están a medio camino en sus metas. |
| **Azul Slate / Gris Oscuro** | `#264653` | Contexto y Estructura | Ejes, rejillas de fondo, textos informativos y KPIs de soporte. Ocupa el fondo visual. |

*Nota sobre accesibilidad:* Evitamos el uso del clásico semáforo (Rojo/Verde puros) ya que resulta inaccesible para el 8% de la población masculina daltónica. El Verde Esmeralda (`#2a9d8f`) es un tono azulado (teal) y el Terracota (`#e76f51`) es un naranja terroso, lo que permite distinguirlos perfectamente tanto en pantallas ordinarias como en impresiones en escala de grises.

---

# 3. Diseño Visual y Control de la Carga Cognitiva

Se aplicaron activamente los **Principios Gestalt** de percepción visual para simplificar la interfaz de usuario:

*   **Principio de Enclosure (Cerramiento):** Las tarjetas de KPIs en la parte superior se agruparon en contenedores con un fondo gris claro tenue (`#f8f9fa`) y un borde lateral de color semántico, separándolas de los gráficos interactivos sin necesidad de líneas divisorias gruesas.
*   **Principio de Similitud:** Toda métrica relacionada con renovables mantiene el color Verde Esmeralda (`#2a9d8f`) a lo largo del dashboard, y toda métrica relacionada con contaminación/intensidad de carbono usa el Terracota (`#e76f51`).
*   **Principio de Cierre:** Los gráficos Plotly se configuraron sin bordes ni marcos pesados. El cerebro del usuario percibe naturalmente los límites del área del gráfico gracias al fondo blanco uniforme.
*   **Principio de Continuidad (Alineación):** La barra lateral con los filtros principales está perfectamente alineada a la izquierda del dashboard. La lectura de la información sigue el flujo natural de la cultura occidental en forma de **Z** (KPIs y título de acción en la esquina superior izquierda, filtros al inicio y apéndices metodológicos al final).
*   **Principio de Conexión:** Las tendencias de transición usan marcadores y líneas continuas para guiar la mirada del usuario de forma secuencial año por año.

---

# 4. Descripción Detallada de las Visualizaciones e Insights

### Visualización 1: Trayectoria de Descarbonización Eléctrica (Subplots)
*   **Tipo de Gráfico:** Subplot de 2 filas y 1 columna compartiendo el eje X (Años 2000-2022).
*   **Evitación del Doble Eje Y:** Siguiendo las directrices de Knaflic, se eliminó el doble eje Y en un mismo plano (que suele confundir al usuario). En su lugar, se separó en dos planos paralelos que permiten rastrear en el mismo año cómo sube la curva de renovables (Plano Superior, Verde) y cómo cae la curva de intensidad de emisiones (Plano Inferior, Terracota).
*   **Títulos de Acción:** *"1. La Transición en el Tiempo: A Mayor Generación Renovable, Menor Intensidad de Carbono"*.
*   **Anotaciones Narrativas Dinámicas:** Se insertaron textos integrados en el gráfico que explican hitos clave del país seleccionado:
    *   *Uruguay (2015)*: Detalla la "Revolución Eólica" que permitió reducir casi a cero su dependencia petrolera.
    *   *Costa Rica (2015)*: Explica su liderazgo histórico basado en matrices hidroeléctricas y geotérmicas.
    *   *Chile (2021)*: Destaca el auge solar en el desierto de Atacama.
    *   *México (2018)*: Señala el estancamiento e infraestructura atada a gas y combustóleo.

### Visualización 2: Riqueza por Habitante vs. Penetración de Energía Limpia
*   **Tipo de Gráfico:** Gráfico de Dispersión / Burbujas.
*   **Variables:** Eje X: PBI per Cápita (GDP / Población); Eje Y: Porcentaje de Renovables; Tamaño de la burbuja: Población.
*   **Título de Acción:** *"2. Desarrollo Sostenible: El Crecimiento Económico No Frena la Transición de la Región"* (Subtítulo: *"En [Año], las economías con mayor PBI per cápita no necesariamente lideran en energía limpia"*).
*   **Insight Narrativo:** El gráfico desmitifica que solo los países ricos pueden permitirse matrices limpias. Se observa que países con ingresos moderados tienen matrices más limpias que gigantes de alto PBI, lo que demuestra que la transición es una decisión regulatoria y política, no una limitación de recursos.

### Visualización 3: Tablero de Posiciones al Año Más Reciente (2022)
*   **Tipo de Gráfico:** Barras Horizontales ordenadas de mayor a menor.
*   **Eje Base Cero:** Se fijó obligatoriamente el eje en cero ($0$) para evitar distorsiones proporcionales en la longitud de las barras.
*   **Color Condicional:** Verde Esmeralda para líderes (>70%), Amarillo para intermedios (35-70%) y Terracota para rezagados (<35%).
*   **Título de Acción:** *"3. Brecha de Descarbonización al 2022: Unos Pocos Líderes Verdes frente a una Mayoría Fósil"*.
*   **Insight Narrativo:** Muestra la brecha real en la región, confrontando el éxito de Uruguay/Costa Rica frente a la lenta adopción de México y Argentina.

---

# 5. Fases de Limpieza y Construcción Técnica

El desarrollo se llevó a cabo utilizando el stack **Python (Streamlit + Pandas + Plotly)** y se organizó en las siguientes fases:

1.  **Exploración y Filtrado del Dataset:** Se analizó el archivo `owid-energy-data (1).csv` y se encontró que la variable `renewables_share_energy` solo estaba un 39% poblada para América Latina. Por ello, se optó por la variable `renewables_share_elec` (100% de cobertura), la cual mide con exactitud el porcentaje de electricidad de fuentes renovables.
2.  **Tratamiento de Nulos y Tipos de Datos:** Se convirtieron todas las variables a numéricas con `pd.to_numeric(errors='coerce')` para evitar fallos de lectura, y se calculó el PBI per Cápita dinámicamente.
3.  **Eliminación de Advertencias en Servidor (Streamlit deprecations):** Se reemplazaron los parámetros antiguos `use_column_width=True` y `use_container_width=True` por el estándar moderno `width="stretch"` y la omisión para las imágenes del menú lateral, resultando en una ejecución libre de logs de advertencia.
4.  **Verificación Local del Servidor Headless:** Se levantó con éxito el servidor local en el puerto `8501`. La comunicación del servidor se validó a través de peticiones HTTP automatizadas que devolvieron el código de éxito `200`.

---

# 6. Guía de Despliegue en Streamlit Community Cloud

Para entregar el dashboard al docente según las directrices de la Fase 5:

1.  **Inicializar repositorio público en GitHub:**
    *   Nombre del repositorio: `dv-grupo[N]-energia-latam` (ejemplo: `dv-grupo1-energia-latam`).
    *   Subir los archivos clave: `app.py`, `requirements.txt`, `owid-energy-data (1).csv`, `README.md` y este `Reporte_Reto.md`.
2.  **Desplegar en la Nube:**
    *   Inicia sesión en [Streamlit Community Cloud](https://streamlit.io/cloud) vinculando tu cuenta de GitHub.
    *   Haz clic en **"New app"**, selecciona tu repositorio, rama principal (`main`) y el archivo de entrada (`app.py`).
    *   Presiona **"Deploy"** y comparte el URL público en el documento de Google Docs compartido por el docente.
