# Funcion para desanidar columnas en un DataFrame de pandas
import pandas as pd
from pandas import DataFrame

def desanidar_columna(df:DataFrame, # DataFrame original
                       columna:str, # Nombre de la columna que se va a desanidar
                       nombre_nueva_tabla: str, # nombre que se le asignará al nuevo DataFrame desanidado
                       indice_increment:int=0) -> DataFrame: # Un valor opcional para incrementar el índice y crear un ID único
    
    df = df
    
    # Crear el ID único en el DataFrame original
    df[f'{columna}_id'] = df.index + indice_increment

    # Desanidar con Explode
    df_exploded = df.explode(columna)

    # Normalizar los datos
    nombre_nueva_tabla = pd.json_normalize(df_exploded[columna])
    # Añadir el ID único al DataFrame desanidado para que se pueda relacionar con el DataFrame original
    nombre_nueva_tabla[f'{columna}_id'] = df_exploded[f'{columna}_id'].values

    return nombre_nueva_tabla # La función devuelve el DataFrame desanidado.