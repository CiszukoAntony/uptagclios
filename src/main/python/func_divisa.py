def convertir(monto, de, a):


    # Paso 1: elegir la moneda que se usara como base
    if de in ["bolivares", "bolívares", "BOLIVARES", "Bolivares"]:
        base = monto
    elif de in ["usd", "USD", "Usd"]:
        base = monto * 623.02
    elif de in ["eur", "EUR", "Eur"]:
        base = monto * 710.10
    else:
        return None 

    # Paso 2: la moneda a la que se quiere convertir pe
    if a in ["bolivares", "bolívares", "BOLIVARES", "Bolivares"]:
        return base
    elif a in ["usd", "USD", "Usd"]:
        return base / 623.02
    elif a in ["eur", "EUR", "Eur"]:
        return base / 710.10
    else:
        return None

while True:
    print("\n--- CONVERSOR DE DIVISAS ---")
    print("1. Convertir")
    print("2. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "2":
        print("Hasta luego.")
        break
        
    elif opcion == "1":
        de = input("De (bolivares, usd, eur): ")
        a = input("A (bolivares, usd, eur): ")
        monto = float(input("Cantidad: "))
        
        resultado = convertir(monto, de, a)
        
        if resultado is not None:
            print(f"Resultado: {resultado:.2f} {a}")
        else:
            print("Error: Moneda no reconocida.")
            
    else:
        print("Opción inválida.")