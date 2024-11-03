import pandas as pd

def convertir_csv_a_parquet(
    csv_path: str,  # Ruta del archivo CSV
    parquet_path: str,  # Ruta archivo para guardar parquet
    columns_to_drop: list = None,  # Lista de columnas que se eliminarán del dataset antes de transformarlo 
    dtype_conversion: dict = None,  # Diccionario que especifica columnas a convertir con su tipo de dato.
    fillna_values: dict = None   # Diccionario que especifica columnas que se rellenarán de valores nulos a valores establecidos por el usuario.
) -> None:
        
    # Cargar el dataset
    df = pd.read_csv(csv_path)

    # Eliminar columnas si se especifica
    if columns_to_drop:
        df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

    # Rellenar valores nulos si se especifica
    if fillna_values:
        df.fillna(value=fillna_values, inplace=True)
        
    # Convertir tipos de datos si se especifica
    if dtype_conversion:
        for column, dtype in dtype_conversion.items():
            if column in df.columns:
                try:
                    df[column] = df[column].astype(dtype)
                except (ValueError, TypeError):
                    print(f"Warning: Conversion de columna '{column}' a '{dtype}' falló. Se intentará con pd.to_numeric.")
                    df[column] = pd.to_numeric(df[column], errors='coerce')
    
    # Guardar como Parquet  
    df.to_parquet(parquet_path, engine='pyarrow', compression='snappy', index=False)

