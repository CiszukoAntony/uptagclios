"""
Módulo para la validación de diferentes tipos de datos numéricos ingresados por el usuario.
--- 
Args:
    None.
--- 
Returns:
    None.
--- 
Raises:
    ValueError: Si el valor ingresado no corresponde al tipo de dato esperado (manejado internamente).
--- 
"""
from utils import module_error,clear_window

def validar_flotante(mensaje):
    """
    Solicita un número flotante y no se detiene hasta que sea válido.
    ---
    Args:
        mensaje (str): El mensaje que se mostrará al usuario en la consola.
    ---
    Returns:
        float: El número flotante válido ingresado por el usuario.
    ---
    Raises:
        ValueError: Si ocurre un error al intentar convertir la entrada a float.
    ---
    """
    while True:
        try:
            valor = float(input(mensaje))
            return valor  # Retorna el valor de inmediato y rompe el ciclo
        except ValueError:
            print("Error: Introduzca un número válido.")

def validar_divisor(mensaje):
    """
    Solicita un número flotante y se asegura de que no sea cero.
    ---
    Args:
        mensaje (str): El mensaje que se mostrará al usuario en la consola.
    ---
    Returns:
        float: El número flotante válido y distinto de cero ingresado por el usuario.
    ---
    Raises:
        ValueError: Si ocurre un error al intentar convertir la entrada a float.
    ---
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor != 0:
                return valor
            else:
                print("Error: El divisor no puede ser cero. Intente de nuevo.")
        except ValueError:
            print("Error: Introduzca un número válido.")
def validar_num_positivo(mensaje):
    """
    Solicita un número flotante y se asegura de que sea mayor o igual a cero.
    ---
    Args:
        mensaje (str): El mensaje que se mostrará al usuario en la consola.
    ---
    Returns:
        float: El número flotante mayor o igual a cero ingresado por el usuario.
    ---
    Raises:
        ValueError: Si ocurre un error al intentar convertir la entrada a float.
    ---
    """
    while True:
        try:
            valor = float(input(mensaje))
            if 0<=valor:
                return valor
            else:
                print("Error:La cantidad debe ser mayor o igual a cero. Intente de nuevo.")
        except ValueError:
            print("Error: Introduzca un número válido.")
def validar_entero(mensaje):
    """
    Solicita un número entero y no se detiene hasta que sea válido.
    ---
    Args:
        mensaje (str): El mensaje que se mostrará al usuario en la consola.
    ---
    Returns:
        int: El número entero válido ingresado por el usuario.
    ---
    Raises:
        ValueError: Si ocurre un error al intentar convertir la entrada a int.
    ---
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor  # Retorna el valor de inmediato y rompe el ciclo
        except ValueError:
            print("Error: Introduzca un número válido.")
def validar_mayor_cero(mensaje):
    """
    Solicita un número flotante y se asegura de que sea mayor a cero.
    ---
    Args:
        mensaje (str): El mensaje que se mostrará al usuario en la consola.
    ---
    Returns:
        float: El número flotante estrictamente mayor a cero ingresado por el usuario.
    ---
    Raises:
        ValueError: Si ocurre un error al intentar convertir la entrada a float.
    ---
    """
    while True:
        try:
            valor = float(input(mensaje))
            if 0<valor:
                return valor
            else:
                print("Error:La cantidad debe ser mayor o igual a cero. Intente de nuevo.")
        except ValueError:
            print("Error: Introduzca un número válido.")
### Comprobación de main ###

if __name__ == "__main__":
    clear_window()
    module_error(__name__, __file__, __package__, __doc__)