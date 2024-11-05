
# Importaciones y configuracion

import os
from fastapi import FastAPI
import pandas as pd
import numpy as np 
import joblib

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

# Carga de datos

# Cargar DataFrames

# df = pd.read_parquet('data/processed_data/movies/movies_dataset_etl.parquet')
df = pd.read_parquet('/home/carla/Documentos/DataScienceProyecto1/DataScienceProyecto1/data/processed_data/movies/movies_dataset_etl.parquet')


df_cast = pd.read_parquet('/home/carla/Documentos/DataScienceProyecto1/DataScienceProyecto1/data/processed_data/credits/cast_desanidado.parquet')
df_crew = pd.read_parquet('/home/carla/Documentos/DataScienceProyecto1/DataScienceProyecto1/data/processed_data/credits/crew_desanidado.parquet')

df_modelo = pd.read_parquet('/home/carla/Documentos/DataScienceProyecto1/DataScienceProyecto1/data/processed_data/modelo_dataset.parquet')


# Cargar modelos

directory = os.path.join(BASE_DIR, '../data/processed_data/')

vectorizer = joblib.load(os.path.join(directory, 'vectorizer.pkl'))
matriz_reducida = joblib.load(os.path.join(directory, 'matriz_reducida.pkl'))


# Diccionario para mapear meses en español a números
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

# Diccionario para mapeo de meses y dias (permiten convertir nombres de meses y días en español a números)
dias = {
    "lunes": 0, "martes": 1, "miercoles": 2, "jueves": 3,
    "viernes": 4, "sabado": 5, "domingo": 6
}


# Endpoints de la API

@app.get("/")
async def root():
    return {"message": "/docs/ para ver la api."}



# Cantidad de Filmaciones por Mes (devuelve la cantidad de películas estrenadas en un mes específico)


@app.get("/cantidad_filmaciones_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str) -> dict:
   
    # Convertir el mes a minúsculas para evitar problemas de capitalización
    mes = mes.lower()
    
    # Verificar que el mes está en el diccionario
    if mes not in meses:
        return {"error": "Mes no válido. Introduzca un mes en español."}
    
    # Obtener el número del mes a travez del diccionario creado.
    numero_mes = meses[mes]
    
    # Contar cuántas películas fueron estrenadas en ese mes
    cantidad = df[df['release_date'].dt.month == numero_mes].shape[0]
    
    return {"cantidad": f"{cantidad} películas fueron estrenadas en los meses de {mes.capitalize()}"}



# Cantidad de Filmaciones por Día (devuelve el número de películas estrenadas en un día específico)


@app.get("/cantidad_filmaciones_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str) -> dict:
    
    # Convertir el dia a minúsculas para evitar problemas de capitalización
    dia = dia.lower()
    
    # Verificar que el día está en el diccionario
    if dia not in dias:
        return {"error": "Día no válido. Introduzca un día en español, sin tildes. Entre Lunes y Domingo."}
    
    # Obtener el número del mes a travez del diccionario creado.
    numero_dia = dias[dia]
    
    # Contar cuántas películas fueron estrenadas en ese día.
    cantidad = df[df['release_date'].dt.dayofweek == numero_dia].shape[0]
    
    return {"message": f"{cantidad} películas fueron estrenadas en los días {dia.capitalize()}"}



# Información sobre Películas (devuelve información sobre una película en función de su título)


@app.get('/score_titulo/{titulo}')
async def score_titulo(titulo: str) -> dict:
   
    # Para evitar problemas de capitalización. Verifica que el dataframe tambien este en minusculas.
    titulo = titulo.lower()
    
    # Busca el titulo en el DataFrame
    pelicula = df[df['title'] == titulo]
    
    if pelicula.empty:
        return {"message": f"No se encontró la película '{titulo}. Verifica los espacios o el nombre correcto en ingles/español.'"}
    
    anio = pelicula['release_year'].values[0]
    score = pelicula['popularity'].values[0]
    
    return {"message": f"La pelicula {titulo} fue estrenada en el año {anio} con un score/popularidad de {score}."}



# Información sobre Votos (proporciona información sobre la cantidad de votos y el promedio para una película específica)


@app.get('/votos_titulo/{titulo}')
async def votos_titulo(titulo: str) -> dict:
   
    # Para evitar problemas de capitalización. Verifica que el dataframe tambien este en minusculas.                    
    titulo = titulo.lower()
    
    # Busca el titulo en el DataFrame
    pelicula = df[df['title'] == titulo]
    
    if pelicula.empty:
        return {"message": f"No se encontró la película '{titulo}. Verifica los espacios o el nombre correcto en ingles/español.'"}
    
    votos = pelicula['vote_count'].values[0]
    
    if votos < 2000:
        return {"message": "La pelicula cuenta con menos de 2000 valoraciones, elige otra pelicula."}
    
    anio = pelicula['release_year'].values[0]
    promedio = pelicula['vote_average'].values[0]

    return {
        "message": f"La película {titulo} fue estrenada en el año {anio}. La misma cuenta con un total de {votos} valoraciones, con un promedio de {promedio}"
    }



# Información sobre Actores (proporciona datos sobre cuántas películas ha hecho un actor y sus retornos)


@app.get('/obtener_actor/{actor}')
async def get_actor(actor: str) -> dict:
    
    # Para evitar problemas de capitalización. Verifica que el dataframe tambien este en minusculas. 
    actor = actor.lower()
    
    # Filtra por el actor ingresado.
    filtro_actor = df_cast[df_cast['name'] == actor]
    
    if filtro_actor.empty:
        return {"message": f"El actor {actor} no se encontró en la base de datos."}
    
    # Cuenta sus peliculas con el id del dataframe original.
    cantidad_peliculas = filtro_actor['id_df'].nunique()
    
    # Array con los id de las peliculas .
    array_peliculas = filtro_actor['id_df'].unique()
    
    # Coincidencias del actor con los id.
    coincidencias = df[df['id'].isin(array_peliculas)]
    
    # Suma de retornos del actor.
    retorno = round(coincidencias['return'].sum(),2)
    # Promedio
    promedio = round(coincidencias['return'].mean(),2)
    
    
    return {
        "message": f"El actor {actor} ha participado de {cantidad_peliculas} filmaciones, el mismo ha conseguido un retorno de {retorno} veces la inversion. Con un promedio de {promedio} por filmación"
    } 



# Información sobre Directores (proporciona información sobre un director, sus películas y sus retornos)


@app.get('/obetener_director/{director}')
async def get_director(director: str) -> dict:
   
    # Para evitar problemas de capitalización. Verifica que el dataframe tambien este en minusculas. 
    director = director.lower()
    
    # Filtra por el director ingresado.
    filtro_director = df_crew[df_crew['name'] == director]
    
    if filtro_director.empty:
        return {"message": f"El director {director} no se encontró en la base de datos. Recuerda solo poner un cargo de Director."}
    
    # Array con los id de las peliculas.
    array_peliculas = filtro_director['id_df'].unique()

    # Coincidencias del director con movies_dataset a travez de su id.
    coincidencias = df[df['id'].isin(array_peliculas)]
    
    # Suma de retornos del director.
    retorno = round(coincidencias['return'].sum(),2)
    
    # Lista de cada pelicula del director
    peliculas = [
    {
        "Titulo": row['title'],
        "Fecha de estreno": row['release_year'],
        "Costo": row['budget'],
        "Ganancia": row['revenue'],
        "Retorno": row['return']
    }
    for _, row in coincidencias.iterrows()  # coincidencias es el DataFrame filtrado de películas
]
    
    return {
        "Nombre": director,
        "Retorno Total": retorno,
        "Peliculas": peliculas
}
    
  
  
  # Recomendaciones de Películas (devuelve una lista de películas similares a la ingresada)
    
@app.get('/recomendacion/{titulo}')
async def recomendacion(titulo: str) ->dict:
    
    titulo = titulo.lower()
    # Encuentra el índice de la película
    idx = df_modelo.index[df_modelo['title'] == titulo].tolist()
    if not idx:
        return {"Error": "Película no encontrada"}
    idx = idx[0]
    
    # Calcula la similitud del coseno solo para la película seleccionada
    sim_scores = cosine_similarity(matriz_reducida[idx].reshape(1, -1), matriz_reducida)

    # Obtén los puntajes de similitud para la película seleccionada
    sim_scores = list(enumerate(sim_scores[0]))
    # Ordena las películas basadas en la similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Devuelve los títulos de las películas más similares
    movie_indices = [i[0] for i in sim_scores[1:6]]
    recomendaciones = df_modelo['title'].iloc[movie_indices].tolist()
    
    return {"Recomendaciones": recomendaciones}