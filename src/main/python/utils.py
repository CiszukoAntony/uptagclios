# Documentacion del modulo utils.py

"""
Modulo de utilidades para el sistema operativo.
--- 
Args:
    None.
--- 
Returns:
    None.
--- 
Raises:
    Exception: Si ocurre un error inesperado.
--- 
"""

# Importacion de librerias y modulos.

import time
import os
import random
import math
import platform
import sys

# Datos del modulo.

__name__ = "__utils__"
__file__ = "utils.py"
__package__ = "__uptagclios__"

### UTILIDADES ###

# Colores y estilos ANSI

class ansi_text:
    """
    Clase para almacenar códigos ANSI para colores.
    --- 
    Args:
        None.
    --- 
    Returns:
        None.
    --- 
    Raises:
        None.
    """
    # COLORS
    RESET = "\033[0m"
    WHITE = "\033[97m"
    BLACK = "\033[30m"
    GRAY = "\033[90m"

    BLUE = "\033[40m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    
    ORANGE = "\033[38;5;208m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    GREEN = "\033[32m"

    #STYLES
    BLUE_BACKGROUD_BOLD = "\033[1;34;40m"
    ORANGE_BACKGROUD_BOLD = "\033[1;38;5;208;40m"

# Limpieza de pantalla.

def clear_window():
    """
    Función para limpiar la pantalla.
    ---

    Args:
        None.
    ---

    Returns:
        None.
    ---

    Raises:
        Exception: Si ocurre un error inesperado.
    ---
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Barra de carga del OS.

def loading(seconds: int = 3, show_bar: bool = True, msg:str = "Cargando..."):
    """
    Función para esperar segundos mostrando una barra de carga animada de forma decreciente.
    Si se ingresa 1 segundo o menos, simplemente espera sin mostrar la barra.
    ---

    Args:
        seconds (int): Número de segundos a esperar.
    ---

    Returns:
        None.
    ---
    """

    try:
        # Si es False o 0, o es 1 segundo o menos, no tiene sentido mostrar la barra de progreso
        if show_bar == False or show_bar == 0 or seconds <= 1:
            time.sleep(seconds)
            return

        else:
            # Cuenta regresiva (decreciente) de seconds hasta 1
            # elapsed cuenta cuántos segundos han pasado para llenar la barra de izquierda a derecha
            for remaining in range(seconds, 0, -1):
                elapsed = seconds - remaining  # Cuántos segundos ya pasaron
                # La barra se llena de izquierda a derecha conforme pasa el tiempo
                bar = "/" * elapsed + " " * remaining
                if remaining == 1:
                    sec_text = "segundo faltante..."
                else:
                    sec_text = "segundos faltantes..."

                # Construimos el texto visible (sin contar códigos ANSI invisibles)
                visible_text = f"[{bar}] {remaining} {sec_text}"
                # Rellenamos con espacios hasta un ancho fijo para borrar cualquier resto anterior
                padding = " " * max(0, 60 - len(visible_text))
                line = f"\n{ansi_text.WHITE}{msg} | {ansi_text.RESET}{ansi_text.BLUE_BACKGROUD_BOLD}[{ansi_text.RESET}{ansi_text.ORANGE_BACKGROUD_BOLD}{bar}{ansi_text.RESET}{ansi_text.BLUE_BACKGROUD_BOLD}]{ansi_text.RESET}{ansi_text.WHITE} | {remaining} {sec_text}{ansi_text.RESET}{padding}"
                print(f"\r{line}", end="", flush=True)
                time.sleep(1)

            # Mensaje final: rellenamos con espacios suficientes para tapar cualquier texto anterior
            print(f"\n \r{ansi_text.GREEN}{msg} | [{"/" * (elapsed+1) + " " * (remaining-1)}] | 0 segundo... | BARRA COMPLETADA. {ansi_text.RESET}{' ' * 50} \n")

    except Exception as e:
        print(f"\n{ansi_text.RED}Error: {e}{ansi_text.RESET}")

### Comprobación de main ###

if __name__ == "__main__":
    pass
else:
    clear_window()
    print(f"\nError: no estas ejecutando el modulo principal\n")
    print(f"Modulo: {__name__}\nARCHIVO: {__file__}\nPAQUETE: {__package__}\nDOCUMENTACION:\n {__doc__}")