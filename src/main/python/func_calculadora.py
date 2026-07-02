"""
Módulo para la ejecución de una calculadora numérica básica e interactiva.
--- 
Args:
    None.
--- 
Returns:
    None.
--- 
Raises:
    None.
--- 
"""

import math
from utils import module_error,clear_window,ansi_text
from func_comprobacion import validar_flotante,validar_divisor,validar_entero
def calculadora():
    """
    Despliega un menú interactivo en consola para realizar operaciones aritméticas, 
    cálculo de potencias, raíces (cuadrada, cúbica, enésima) y funciones trigonométricas.
    ---
    Args:
        None.
    ---
    Returns:
        None.
    ---
    Raises:
        None.
    ---
    """
    # Calculadora Numerica Basica
    print("Bienvenido a la calculadora basica de python")
    # Menu de la calculadora
    while True:
        print("Ingresa cual operacion quieres realizar")
        print(f"{ansi_text.ORANGE}={ansi_text.RESET}"*90)
        print(f"""{ansi_text.BLUE}
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Potencia
        6. Raiz Cuadrada
        7. Raiz Cubica
        8. Raiz Enesima
        9. Coseno
        10. Seno
        11. Tangente
        12. Salir{ansi_text.RESET}""")
        print(f"{ansi_text.ORANGE}={ansi_text.RESET}"*90)
        
        op = validar_entero ("Elija una operacion: ")
        #opcion no valida
        if op not in [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]:
            print("Error la opcion es del 1 al 12")
        else:  
            #suma
            if op == 1:
                num1= validar_flotante("ingrese el valor del primer numero a sumar: ")
                num2= validar_flotante("ingrese el valor del segundo numero a sumar: ")
                print("el resultado de la suma es: ", num1+num2)
            #resta
            elif op == 2:
                num1= validar_flotante("ingrese el valor del minuendo de la resta: ")
                num2= validar_flotante("ingrese el valor del sustraendo de la resta: ")
                print("el resultado de la resta es: ", num1-num2)
            #multiplicacion
            elif op == 3:
                num1= validar_flotante("ingrese el valor del primer numero a multiplicar: ")
                num2= validar_flotante("ingrese el valor del segundo numero a multiplicar: ")
                print("el resultado de la multiplicacion es: ", num1*num2)
            #division
            elif op == 4:
                num1= validar_flotante("ingrese el valor del dividendo: ")
                num2= validar_divisor("ingrese el valor del divisor: ")
                print("el resultado de la division es: ", num1/num2)
                print("el cociente de la division es: ", num1//num2)
                print("el resto de la division es: ", num1%num2)
            #potencia
            elif op == 5:
                num1= validar_flotante("ingrese el valor de la base de la potencia: ")
                num2= validar_flotante("ingrese el valor de el exponente de la potencia: ")
                print("el resultado de la multiplicacion es: ", num1**num2)
            # raiz cuadrada
            elif op == 6:
                num1 = validar_flotante("ingrese el valor de su raiz cuadrada: ")
                
                if num1 < 0:
                    print("Math ERROR: Resultado imaginario/complejo no soportado.")
                else:
                    resultado = math.sqrt(num1)
                    # Usamos round para que quede limpio y con los mismos decimales que tu otra opción
                    print(f"el resultado de la raiz cuadrada de {num1} es: {round(resultado, 9)}")
            #raiz cubica
            elif op == 7:
                num1= validar_flotante("ingrese el valor de su raiz cubica: ")
                print(f"el resultado de la raiz cubica de {num1} es: ", round(math.cbrt(num1), 9))
            #raiz enesima
            elif op == 8:
                while True:
                    radicando = validar_flotante("ingrese el valor del radicando de su raiz enesima: ")
                    indice = validar_flotante("ingrese el valor indice del su raiz enesima: ")
                    
                    # 1. Filtro de Índice Cero (Math ERROR)
                    if indice == 0:
                        print("Math ERROR: División por cero (Índice no puede ser 0).")
                        continue  # Reinicia el bucle para pedir los datos otra vez
                        
                    # 2. Filtro de Radicando Cero con Índice Negativo (Math ERROR)
                    elif radicando == 0 and indice < 0:
                        print("Math ERROR: División por cero.")
                        continue  # Reinicia el bucle
                        
                    # 3. Caso Radicando Cero con Índice Positivo
                    elif radicando == 0:
                        print("el resultado es: 0.0")
                        break
                        
                    # 4. Filtro de Radicando Negativo
                    elif radicando < 0:
                        # .is_integer() verifica si el float no tiene decimales significativos (ej. 3.0, 5.0)
                        if indice.is_integer() and int(indice) % 2 != 0:
                            resultado = math.copysign(abs(radicando) ** (1 / indice), radicando)
                            print(f"el resultado es: {round(resultado, 9)}")
                            break
                        else:
                            print("Math ERROR: Resultado imaginario/complejo no soportado.")
                            continue
                        
                    # 5. Casos normales (Radicando positivo con índices positivos, negativos o decimales)
                    else:
                        resultado = radicando ** (1 / indice)
                        print(f"el resultado es: {round(resultado, 9)}")
                        break
            #coseno
            elif op == 9:
                num1=validar_flotante("ingrese los grados de su coseno: ")
                resultado = math.cos(math.radians(num1))
                print(f"el resultado del coseno de {num1}° es: ",resultado)
            #seno
            elif op == 10:
                num1=validar_flotante("ingrese los grados de su seno: ")
                resultado = math.sin(math.radians(num1))
                print(f"el resultado del seno de {num1}° es: ",resultado)
            #tagente
            elif op == 11:
                num1=validar_flotante("ingrese los grados de su tangente: ")
                resultado = math.tan(math.radians(num1))
                print(f"el resultado de la tangente de {num1}° es: ",resultado)
            #salida
            elif op == 12:
                print("Se ha cerrado el programa")
                break
                
        continuar = input("Desea continuar (s/n): ").lower()
        if continuar != "s":
            print("Saliste del programa")
            break
### Comprobación de main ###

if __name__ == "__main__":
    clear_window()
    module_error(__name__, __file__, __package__, __doc__)