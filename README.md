# Reto: El Dashboard que Convence ⚡
### Curso: Data Visualization — Storytelling con Datos, Paletas de Color y Despliegue Web

Este repositorio contiene la entrega del reto de visualización de datos de energía para América Latina. El dashboard narrativo e interactivo ha sido desarrollado en Python utilizando **Streamlit** y **Plotly** bajo una arquitectura de proyecto limpia y modular.
### Link del despliegue:
https://reto12dataviz.streamlit.app/

---

#### Integrantes:
Joaquin Basas
Joaquin Alvarado
Alejandro Colfer
Nathaly Anaya
Mark Esquivel

---


## 📌 Pregunta Narrativa Central
> **"América Latina: ¿Crecimiento Verde o Dependencia Fósil? El contraste entre líderes de transición y rezagados (2000-2022)"**

El objetivo del dashboard es analizar si el desarrollo económico y crecimiento en la región está logrando desacoplarse de la contaminación ambiental mediante el uso de energías renovables o si, por el contrario, los principales polos económicos se mantienen atados a la dependencia fósil.

---

## 🎨 Paleta de Color Elegida (Paleta 1 - Sostenibilidad)
Hemos seleccionado una paleta con intención narrativa clara, respetando el límite de 4 colores activos por vista:

1. **Verde Esmeralda (`#2a9d8f`)**: Representa la participación de energías renovables y el progreso hacia la sostenibilidad.
2. **Terracota / Naranja-Rojo (`#e76f51`)**: Representa la intensidad de carbono y emisiones de CO₂. Sirve como color de tensión y contraste para los combustibles fósiles.
3. **Amarillo Arena (`#e9c46a`)**: Representa las zonas de transición o estados intermedios en el ranking de países.
4. **Azul Slate / Gris Oscuro (`#264653` / `#333333`)**: Color de soporte para el fondo de texto, ejes y contexto secundario.

---

## 📂 Estructura del Proyecto
El proyecto ha sido refactorizado para seguir los estándares profesionales de desarrollo de software y ciencia de datos:

```
/
├── .gitignore             # Archivos y carpetas a excluir en Git
├── README.md              # Documentación general del proyecto (este archivo)
├── requirements.txt       # Dependencias de Python requeridas
├── app.py                 # Orquestador del Dashboard (interfaz Streamlit)
├── data/
│   └── owid-energy-data (1).csv   # Dataset original de consumo energético
├── docs/
│   └── Reporte_Reto.md    # Reporte metodológico y de Storytelling detallado
├── notebooks/
│   └── Exploracion_Datos.ipynb  # Notebook Jupyter para el análisis exploratorio preliminar
└── src/
    ├── __init__.py        # Inicializador del paquete
    ├── charts.py          # Lógica de graficación de Plotly (gráficos limpios)
    └── data_loader.py     # Carga y limpieza de datos con Pandas
```

---

## 📊 Estructura de Visualización
El dashboard consta de tres visualizaciones clave con jerarquía narrativa definida:

1. **Visualización Temporal (Subplots Compartidos)**: Muestra la correlación directa entre el incremento de la generación eléctrica renovable (curva superior verde) y la caída en la intensidad de carbono (curva inferior terracota), evitando la fatiga cognitiva del doble eje Y. Incluye anotaciones de storytelling para Uruguay, Costa Rica, Chile y México.
2. **Visualización de Correlación (Burbuja)**: Cruza el PBI per Cápita con el porcentaje de energías renovables para desmitificar que el desarrollo económico impide la transición verde.
3. **Visualización Comparativa (Barras Horizontales)**: Clasifica a los países al 2022 en Líderes, Transición y Rezagados usando colores condicionales con base en cero ($0$).

---

## 🚀 Instrucciones para Ejecución Local

1. Asegúrate de tener instalado Python 3.8 o superior.
2. Instala las dependencias especificadas en `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el servidor de desarrollo local de Streamlit desde la carpeta raíz:
   ```bash
   streamlit run app.py
   ```
4. Abre la dirección http://localhost:8501 en tu navegador web.

---

## 🌐 Instrucciones para el Despliegue en Streamlit Community Cloud

Para desplegar este dashboard de manera pública y gratuita en la nube de Streamlit:

1. **Subir el código a GitHub**:
   - Crea un repositorio público en GitHub llamado `dv-grupo[N]-energia-latam` (reemplaza `[N]` por el número de tu grupo).
   - Realiza un `git push` de toda la estructura de archivos al repositorio.

2. **Conectar con Streamlit Cloud**:
   - Ingresa a [Streamlit Community Cloud](https://streamlit.io/cloud) e inicia sesión con tu cuenta de GitHub.
   - Haz clic en **"New app"**.
   - Selecciona tu repositorio recién creado, la rama (`main`) y establece `app.py` como el archivo principal.
   - Haz clic en **"Deploy"**.

3. **Obtener URL público**:
   - Una vez desplegado, copia el URL público generado y pégalo en la hoja compartida de Google Docs habilitada por el docente.
