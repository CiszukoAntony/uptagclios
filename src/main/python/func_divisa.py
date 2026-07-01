from func_comprobacion import validar_mayor_cero

def convertir():
    """
    Solicita al usuario las divisas de origen y destino, junto con el monto, 
    para calcular y mostrar el resultado de la conversión.

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
    moneda = ["bolivares", "bolívares", "usd", "eur"]

    # Validación de la moneda que se desea convertir
    while True:
        de = input("De (bolivares, usd, eur): ").lower()
        if de in moneda:
            break
        print("Error: Moneda. Intenta de nuevo.")

    # Validación de la moneda a la que se desea convertir
    while True:
        a = input("A (bolivares, usd, eur): ").lower()
        if a in moneda:
            break
        print("Error: Moneda. Intenta de nuevo.")

    # Validación del monto a convertir
    while True:
        try:
            monto = validar_mayor_cero("Monto a convertir: ")
            break
        except ValueError:
            print("Error: Por favor ingresa un número válido.\n")

    # Paso 1: Convertir a la moneda que se desea convertir (base)
    if de in ["bolivares", "bolívares"]:
        base = monto
    elif de == "usd":
        base = monto * 633.02
    elif de == "eur":
        base = monto * 710.10

    # Paso 2: Convertir de la base a la moneda de destino
    if a in ["bolivares", "bolívares"]:
        resultado = base
    elif a == "usd":
        resultado = base / 633.02
    elif a == "eur":
        resultado = base / 710.10

    # Paso 3: Mostrar el resultado
    print(f"Resultado: {resultado:.2f} \n")


# Bucle principal del menú
while True:
    print("\n--- CONVERSOR DE DIVISAS ---")
    print("1. Convertir")
    print("2. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "2":
        print("Hasta luego.")
        break
        
    elif opcion == "1":
        convertir()
        
    else:
        print("Opción inválida.")