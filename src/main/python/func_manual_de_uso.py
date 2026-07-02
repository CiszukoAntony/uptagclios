"""
Módulo principal del Manual de Uso del Sistema Operativo.
---
Este módulo contiene las funciones para mostrar instrucciones y
guías de uso de las diferentes herramientas del sistema.
---
Args:
    None.
---
Returns:
    None.
---
Raises:
    Exception: Si ocurre un error inesperado al ejecutar el programa.
---
"""
# Manual de Uso Simple
# Este programa muestra instrucciones básicas de uso

from utils import clear_window, module_error

def mostrar_menu():
    
    """muestra el menu de opciones"""
    
    print("\n" + "="*40)
    print("        MANUAL DE USO      ")
    print("="*40)
    print("1. calculadora.")
    print("2. conversión de divisas.")
    print("3. piedra,papel,tijera.")
    print("4. adivina el número.")
    print("5. información y creditos.")
    print("6. salir.")
    print("="*40)
    
#ahora se continua con las opciones
#enpezando con las divisas.

def mostrar_conversion_de_divisa():
    
    """muestra la información sobre la conversión de divisas"""
    
    print("\n[conversion de divisas]")
    print("para el correcto uso de esta funcion, no se debe colocar numeros negativos,no se debe colocar una divisa la cual no esta en el conversor, la cantidad de la moneda solicitada debe ser logica y correcta, en caso de no cumplir con estos parametros la conversion asi tambien como el programa no iniciara.") 
    print("Presiona ENTER para continuar...")
    input()
    
    #seguimos con adivinar el número.
    
def mostrar_adivina_el_numero():
    
    """muestra la información sobre adivinar el numero"""
        
    print("\n[adivina el número]")
    print("para el correcto uso de esta funcion se necesita daber que: no de podren colocar numeros negativos asi mismo como no se deben colocar letros signos o algun simbolo mas, no se debe exceder el valor numerico preestablecido o sea se del 1 al 100, en caso tal de colocar un valor incorrecto bien sea numerico o simbolico el programa no iniciara y se debera colocar un valor correcto.")
    print("Presiona ENTER para continuar...")
    input()
    
    #el siguiente piedra papel o tijeras.
    
def mostrar_piedra_papel_tijeras():
    
    """muestra la información sobre piedra,papel tijeras"""
    
    print("\n[piedra,papel,tijera]")
    print("para el correcto uso de esta función no se debe seleccionar otra opción que no este implicita en el juego, se debe respetar las instrucciones dentro de este para que no haya errores, no se debe usar ninguna simbologia o carácter especial, en dado caso de esta situación el juego no iniciará o dara errores a la hora de continuar.")
    print("Presiona ENTER para continuar...")
    input()
    
    #ahora con información y creditos.
    
def mostrar_informacion_creditos():
    
    """muestra información sobre los creditos y algo amdde información"""
    
    print("\n[Información y creditos]")
    print("una vez dentro se mostrara la información mas relevante del oroyecto ais como los créditos correspondientes a los autores, no se debera mover ni modificar nada ya que podria dañar el proyecto y afectar su rendimiento, lo autores de este proyecto son: francisco García, santaigo rojas,ivan quevedo,luis colina y hanzer sivira :.")
    print("Presiona ENTER para continuar...")
    input()
    
    #y por ultimo la calculadora
    
def mostrar_calculadora():
    
    """muestra la información sobre la calculadora"""
    
    print("\n[calculadora]")
    print("Este programa es una herramienta simple")
    print("para el correcto uso de la calculadora se le pide al usuario que no ingrese ningún otro valor que no ingrese ninguna opcion que no posea la calculadora asi como también ningun valor que no sea numerico en tal caso de que so llegue a pasar la calculadora fallara y tendra que iniciar denuevo.")
    print("Presiona ENTER para continuar...")
    input()

# Programa principal

def main():
    
    """Esta función controla el flujo principal del programa mostrando el menú
    de opciones al usuario, procesando su selección y llamando a las funciones
    correspondientes. El bucle se mantiene activo hasta que el usuario elige
    la opción de salir (6)."""
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "1":
            mostrar_calculadora()
        elif opcion == "2":
          mostrar_conversion_de_divisa()
        elif opcion == "3":
            mostrar_piedra_papel_tijeras()  
        elif opcion == "4":
            mostrar_adivina_el_numero()
        elif opcion == "5":
            mostrar_informacion_creditos()
        elif opcion == "6":
            print("\n¡Hasta luego! Gracias por usar el manual.")
            break
        else:
            print("\n¡Opción inválida! Por favor, elige 1-6.")
            print("Presiona ENTER para continuar...")
            input()
if __name__ == "__main__":
    clear_window()
    module_error(__name__, __file__, __package__)