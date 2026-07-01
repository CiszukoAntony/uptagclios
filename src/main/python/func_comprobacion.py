def validar_flotante(mensaje):
    """Solicita un número flotante y no se detiene hasta que sea válido."""
    while True:
        try:
            valor = float(input(mensaje))
            return valor  # Retorna el valor de inmediato y rompe el ciclo
        except ValueError:
            print("Error: Introduzca un número válido.")

def validar_divisor(mensaje):
    """Solicita un número flotante y se asegura de que no sea cero."""
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
    """Solicita un número flotante y se asegura de que sea mayor a cero."""
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
    """Solicita un número entero y no se detiene hasta que sea válido."""
    while True:
        try:
            valor = int(input(mensaje))
            return valor  # Retorna el valor de inmediato y rompe el ciclo
        except ValueError:
            print("Error: Introduzca un número válido.")