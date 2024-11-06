# Sistema de Recomendación de Películas

Un sistema de recomendación de películas basado en FastAPI que proporciona información detallada sobre películas, directores, actores y recomendaciones personalizadas.

## Tabla de Contenido
1. [Introducción](#introducción)
2. [Instalación y Requisitos](#instalación-y-requisitos)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Uso y Ejecución](#uso-y-ejecución)
5. [Datos y Fuentes](#datos-y-fuentes)
6. [Metodología](#metodología)
7. [Resultados y Conclusiones](#resultados-y-conclusiones)
8. [Contribución y Colaboración](#contribución-y-colaboración)
9. [Licencia](#licencia)

## Introducción

Este proyecto implementa un sistema de recomendación de películas utilizando FastAPI. El sistema permite a los usuarios obtener información detallada sobre películas, incluyendo estadísticas de lanzamiento, puntuaciones, información sobre actores y directores, así como recomendaciones personalizadas basadas en similitud de contenido.

## Instalación y Requisitos

### Requisitos Previos
- Python 3.11 
- pip (gestor de paquetes de Python)

### Instalación

1. Clonar el repositorio:
```bash
git clone [https://github.com/carladanie11/DataScienceProyecto1.git]
cd [DataScienceProyecto1]
```

2. Crear un entorno virtual e instalar las dependencias:

- En este proyecto se utilizo anaconda-navigator para crear el ambiente virtual 
Otra alternativa para crearlo es la siguiente:
- Crear un entorno virtual: python -m venv venv
- Activar el entorno virtual:
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

- Intalar las dependencias:
pip install -r requirements.txt
Las principales dependencias incluyen:
- FastAPI 0.112.2
- pandas 2.2.2
- scikit-learn 1.5.1
- numpy 1.26.4
- nltk 3.9.1


## Estructura del Proyecto

```
.
├── code/: Contiene scripts de Python que se utilizan para la transformación de datos y preprocesamiento. 
│   
├── data/
│   ├── credits.parquet: Archivos de datos en formato Parquet.
│   ├── movies_dataset.parquet:Archivos de datos en formato Parquet.
│   └── processed_data/: Datos procesados después de realizar transformaciones.
├── notebooks/
│   ├── eda.ipynb: Exploratory Data Analysis (análisis exploratorio de datos).
│   ├── etlCredits.ipynb: Procesos ETL para eL dataset credits.
│   ├── etlMovies.ipynb: Procesos ETL para el dataset movies.
│   └── model.ipynb: creación y evaluación del modelo de machine learning.
├── src/
│   └── main.py: Archivo principal de la aplicación.
├── requirements.txt: Archivo que especifica las dependencias de Python.
├── README.md: Archivo donde se describe este proyecto, cómo configurarlo y cómo usarlo.
└── LICENSE: Archivo donde se definen los términos legales bajo los cuales este proyecto está disponible.
```

## Uso y Ejecución

Para iniciar el servidor FastAPI:

```bash
uvicorn src.main:app --reload
```

### Endpoints Disponibles

1. `/cantidad_filmaciones_mes/{mes}`: Retorna la cantidad de películas estrenadas en un mes específico
2. `/cantidad_filmaciones_dia/{dia}`: Retorna la cantidad de películas estrenadas en un día específico
3. `/score_titulo/{titulo}`: Proporciona información sobre el score de una película
4. `/votos_titulo/{titulo}`: Muestra información sobre los votos de una película
5. `/obtener_actor/{actor}`: Proporciona estadísticas sobre un actor específico
6. `/obtener_director/{director}`: Muestra información sobre un director y sus películas
7. `/recomendacion/{titulo}`: Genera recomendaciones de películas similares

## Datos y Fuentes

El proyecto utiliza datos procesados de películas almacenados en formato parquet:
- `movies_dataset`: Dataset principal de películas
- `credits`: Información sobre elencos y equipos de producción

Los datos han sido procesados y transformados los cuales se presentan en la carpeta processed_data

## Metodología

El sistema implementa:
1. Procesamiento ETL de datos de películas
2. Análisis exploratorio de datos (EDA)
3. Sistema de recomendación basado en similitud de contenido
4. API RESTful para acceder a la información y recomendaciones

Se utilizan técnicas de:
- Procesamiento de texto y NLP
- Vectorización TF-IDF
- Similitud del coseno para recomendaciones
- Reducción de dimensionalidad

## Resultados y Conclusiones

El sistema proporciona:
- Análisis detallado de películas y estadísticas
- Información sobre rendimiento de actores y directores
- Recomendaciones personalizadas basadas en contenido
- API accesible y documentada, implementada con FastAPI y desplegada en Render.com.

Link a la API en Render: https://datascienceproyecto1-7.onrender.com
Link video en YouTube: https://youtu.be/EzoDrYsMtCI/docs

## Contribución y Colaboración

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Cree una nueva rama 
3. Commit sus cambios
4. Push a la rama 
5. Abra un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia incluida en el archivo LICENSE.