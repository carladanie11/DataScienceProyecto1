import pandas as pd

def add_weight(row, columna, weight=3):
    '''
    Función que concatena el texto de una columna  hacia 'overview',
    multiplicando su contenido para darles más peso.
    
    Parameters:
    ----------
    row (pandas.Series): iteracion de filas 'overview' y la columna a multiplicar
    columna (str): nombre de la columna que quiere multiplicar su informacion
    weight (int): Número de veces que el texto se repite para aumentar su peso
    
    Returns:
    ----------
    str: El texto combinado y ponderado
    
    ejemplo de uso: 
    ---------------
        df['overview'] = df.apply(lambda row: add_weight(row, 'combined_companies', weight=3), axis=1)
    '''
    overview = row['overview']
    texto = row[columna]
    
    if pd.isna(texto):
        # Si no hay compañías, devuelve solo el overview
        return overview
    
    # Ponderar las compañías repitiéndolas 'weight' veces
    weighted_text = ' '.join([texto] * weight)
    
    # Concatenar el overview con las compañías ponderadas
    return f"{overview} {weighted_text}"