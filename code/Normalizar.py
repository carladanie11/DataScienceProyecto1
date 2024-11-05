import re

def normalizar_texto(text: str) -> str:
    '''
    Normaliza el texto eliminando caracteres especiales, convirtiendo a minúsculas 
    y reduciendo múltiples espacios a uno solo.
    
    Parameters:
    ----------
    text (str): El texto a normalizar.
    
    Returns:
    ----------
    str: El texto normalizado.
    '''
    text = text.lower()  # Convertir a minúsculas
    text = re.sub(r'\s+', ' ', text)  # Reemplaza múltiples espacios por un solo espacio
    text = re.sub(r'[^\w\s]', '', text)  # Eliminar caracteres especiales
    return text.strip()  # Eliminar espacios al principio y al final