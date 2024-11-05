def lista_a_str(val: any) -> str:
    """
    Convierte una lista a string. en caso de ser una lista, si no retorna su valor original.

    Parameters
    ----------
    val (list):
        El valor a evaluar. Si es una lista, se convertirá a string; de lo contrario, se devolverá el valor original.

    Returns
    -------
    val (str):
        Si el valor es una lista, retorna un string. devuelve el valor original sin modificar.
    """
    if isinstance(val, list):
        return str(val)
    else:
        return val
    