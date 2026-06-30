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

    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    
    ORANGE = "\033[38;5;208m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    GREEN = "\033[32m"

    #STYLES
    BLUE_BACKGROUND_BOLD = "\033[1;34;40m"
    ORANGE_BACKGROUND_BOLD = "\033[1;38;5;208;40m"

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
                line = f"{ansi_text.WHITE}{msg} | {ansi_text.RESET}{ansi_text.BLUE_BACKGROUND_BOLD}[{ansi_text.RESET}{ansi_text.ORANGE_BACKGROUND_BOLD}{bar}{ansi_text.RESET}{ansi_text.BLUE_BACKGROUND_BOLD}]{ansi_text.RESET}{ansi_text.WHITE} | {remaining} {sec_text}{ansi_text.RESET}{padding}"
                print(f"\r{line}", end="", flush=True)
                time.sleep(1)

            # Mensaje final: rellenamos con espacios suficientes para tapar cualquier texto anterior
            print(f"\n \r{ansi_text.GREEN}{msg} | [{"/" * (elapsed+1) + " " * (remaining-1)}] | 0 segundo... | BARRA COMPLETADA. {ansi_text.RESET}{' ' * 50} \n")

    except Exception as e:
        print(f"\n{ansi_text.RED}Error: {e}{ansi_text.RESET}")

# Comprobacion de nombre de usuario.

username = "usser"

def init_username():
    """
    Solicita el nombre del usuario, lo valida para evitar campos vacíos,
    limpia espacios innecesarios (incluso internos) y lo registra de forma global.
    """
    global username  # Modificamos la variable global
    
    while True:
        new_username = input(
            f"{ansi_text.WHITE}¿Cual es tu nombre de usuario?{ansi_text.RESET}"
            f"{ansi_text.GRAY}...{ansi_text.RESET}"
            f"{ansi_text.BLUE_BACKGROUND_BOLD}\n >>> {ansi_text.RESET}"
        )
        
        correct_username = " ".join(new_username.split()).title()
        
        if correct_username == "":
            print(f"{ansi_text.RED}Error: El nombre no puede estar vacío. Por favor, ingresa un nombre válido.{ansi_text.RESET}\n")
            continue  # Reinicia el ciclo para volver a pedir el nombre

        if not correct_username.replace(" ", "").isalpha():
            print(f"{ansi_text.RED}Error: El nombre solo debe contener letras (no se permiten números ni símbolos).{ansi_text.RESET}\n")
            continue
            
        username = correct_username
        break
    
    loading(2, 1, f"Registrando usuario... {username}")
    return username

def call_username():
    """
    Devuelve el nombre del usuario registrado con estilos ANSI aplicados.
    """
    global username
    # Corregido: Añadida la 'f' de f-string y la variable real
    return f"{ansi_text.CYAN}{username}{ansi_text.RESET}"

def module_error(module_name, module_file, module_package, module_doc):
    print(f"{ansi_text.RED}======================================================================{ansi_text.RESET}")
    print(f"{ansi_text.RED}ADVERTENCIA DE SEGURIDAD DEL SISTEMA OS{ansi_text.RESET}")
    print(f"{ansi_text.RED}======================================================================{ansi_text.RESET}")
    print(f"Error: No puedes iniciar el sistema desde un módulo.")
    print(f"Por razones de arquitectura modular, debes ejecutar el archivo principal.\n")
    
    print(f"{ansi_text.GRAY}Datos de depuración del Intérprete:{ansi_text.RESET}")
    print(f"- Entorno (__name__): {module_name} (Modo de ejecución directa)")
    print(f"- Paquete (__package__): {module_package}")
    print(f"- Ubicación: {module_file}")
    print(f"- Documentación activa:\n{module_doc}")
    print(f"{ansi_text.RED}======================================================================{ansi_text.RESET}")
    print(f"\n{ansi_text.GREEN}SOLUCIÓN: Ejecuta en tu terminal: python main.py{ansi_text.RESET}\n")

def main_error(module_name, module_file, module_package, module_doc):
    print(f"{ansi_text.RED}======================================================================{ansi_text.RESET}")
    print(f"{ansi_text.RED}Error: hubo un error ejecutando el modulo principal{ansi_text.RESET}")
    print(f"{ansi_text.RED}======================================================================{ansi_text.RESET}")
    
    print(f"{ansi_text.GRAY}Datos de depuración del Intérprete:{ansi_text.RESET}")
    print(f"- Entorno (__name__): {module_name}")
    print(f"- Paquete (__package__): {module_package}")
    print(f"- Ubicación: {module_file}")
    print(f"- Documentación activa:\n{module_doc}")
    print(f"{ansi_text.RED}======================================================================{ansi_text.RESET}")
    print(f"\n{ansi_text.GREEN}SOLUCIÓN: Ejecuta en tu terminal: python main.py de nuevo o contacte a servicio de soporte tecnico.{ansi_text.RESET}\n")

### Comprobación de main ###

if __name__ == "__main__":
    clear_window()
    module_error(__name__, __file__, __package__, __doc__)