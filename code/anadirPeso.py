import pandas as pd

def add_weight(row, columna, weight=3):
    '''
    Concatena el texto de una columna específica con 'overview', 
    aumentando su relevancia mediante la repetición.
    
    Parameters:
    ----------
    row (pandas.Series): La fila actual del DataFrame sobre la cual se aplica la función.
    columna (str): El nombre de la columna cuyo contenido se multiplicará para incrementar su peso.
    weight (int): El número de veces que se repetirá el contenido de la columna para darle más importancia.
    
    Returns:
    ----------
    str: El texto combinado de 'overview' y la columna especificada, con la columna ponderada.
    
    
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