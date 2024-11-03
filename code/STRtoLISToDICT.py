import pandas as pd
import ast   # convierte de manera segura cadenas en estructuras de datos de Python.


# Función que convierte valores de tipo str que representan listas o diccionarios en su forma real de Python (list o dict). 
# También maneja valores nulos (NaN) y casos en los que la conversión falla. 

def convert_list_dict(value: any) -> dict | list | None:        
    if pd.isna(value):  # maneja valores nulos
        return None

    if isinstance(value, str): 
        try:            
            value = value.replace('Null', 'None')   # # Reemplaza'Null' por 'None' 
            return ast.literal_eval(value)  # convierte cadena de forma segura
        except (ValueError, SyntaxError) as e:
            print(f"Error convirtiendo el valor: {value}\nError: {e}") # Maneja errores potenciales y proporciona información para la depuración
            return value
    
    return value 

# Devuelve un dict o list si la conversión es exitosa, None si el valor es nulo (NaN), o el valor original si no es una cadena a convertir.
