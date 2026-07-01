import math
import cmath
from func_comprobacion import validar_flotante,validar_divisor,validar_entero
def calculadora():
    # Calculadora Numerica Basica

    print("Bienvenido a la calculadora basica de python")
    # Menu de la calculadora
    while True:
        print("Ingresa cual operacion quieres realizar")
        
        print("""
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Potencia
        6. Raiz Cuadrada
        7. Raiz Cubica
        8. Coseno
        9. Seno
        10. Tangente
        11. Salir""")
        
        op = validar_entero ("Elija una operacion: ")
        
        if op not in [1, 2, 3, 4, 5,6,7,8,9,10,11]:
            print("Error la opcion es del 1 al 11")
            
        else:  
            if op == 1:
                num1= validar_flotante("ingrese el valor del primer numero a sumar: ")
                num2= validar_flotante("ingrese el valor del segundo numero a sumar: ")
                print("el resultado de la suma es: ", num1+num2)
            elif op == 2:
                num1= validar_flotante("ingrese el valor del minuendo de la resta: ")
                num2= validar_flotante("ingrese el valor del sustraendo de la resta: ")
                print("el resultado de la resta es: ", num1-num2)
            elif op == 3:
                num1= validar_flotante("ingrese el valor del primer numero a multiplicar: ")
                num2= validar_flotante("ingrese el valor del segundo numero a multiplicar: ")
                print("el resultado de la multiplicacion es: ", num1*num2)
            elif op == 4:
                num1= validar_flotante("ingrese el valor del dividendo: ")
                num2= validar_divisor("ingrese el valor del divisor: ")
                print("el resultado de la division es: ", num1/num2)
                print("el cociente de la division es: ", num1//num2)
                print("el resto de la division es: ", num1%num2)
            elif op == 5:
                num1= validar_flotante("ingrese el valor de la base de la potencia: ")
                num2= validar_flotante("ingrese el valor de el exponente de la potencia: ")
                print("el resultado de la multiplicacion es: ", num1**num2)
            elif op == 6:
                num1= validar_flotante("ingrese el valor de su raiz cuadrada: ")
                print(f"el resultado de la raiz cuadrada de {num1} es: ", cmath.sqrt(num1))
            elif op == 7:
                num1= validar_flotante("ingrese el valor de su raiz cubica: ")
                print(f"el resultado de la raiz cubica de {num1} es: ", round(math.cbrt(num1), 9))
            elif op == 8:
                num1=validar_flotante("ingrese los grados de su coseno: ")
                resultado = math.cos(math.radians(num1))
                print(f"el resultado del coseno de {num1}° es: ",resultado)
            elif op == 9:
                num1=validar_flotante("ingrese los grados de su seno: ")
                resultado = math.sin(math.radians(num1))
                print(f"el resultado del seno de {num1}° es: ",resultado)
            elif op == 10:
                num1=validar_flotante("ingrese los grados de su tangente: ")
                resultado = math.tan(math.radians(num1))
                print(f"el resultado de la tangente de {num1}° es: ",resultado)
            elif op == 11:
                print("Se ha cerrado el programa")
                
        continuar = input("Desea continuar (s/n): ").lower()
        if continuar != "s":
            print("Saliste del programa")
            break
calculadora()