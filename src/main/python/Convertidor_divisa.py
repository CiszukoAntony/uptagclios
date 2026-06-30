import requests

def obtener_codigo_moneda(mensaje: str) -> str:
    """Solicita y valida un código de moneda de 3 letras ingresado por el usuario."""
    while True:
        codigo = input(mensaje).strip().upper()
        if len(codigo) == 3 and codigo.isalpha():
            return codigo
        print("  Error: El código debe tener exactamente 3 letras (ej. USD, EUR, MXN).\n")


def obtener_monto(desde_moneda: str) -> float:
    """Solicita y valida que el monto a convertir sea un número positivo."""
    while True:
        try:
            monto = float(input(f"Ingrese la cantidad en {desde_moneda}: "))
            if monto > 0:
                return monto
            print("  Error: El monto debe ser mayor que cero.")
        except ValueError:
            print("  Error: El monto debe ser un número válido (usa el punto para decimales).")


def obtener_tasa_cambio(desde_moneda: str, hacia_moneda: str) -> float:
    """Efectúa la petición a la API y extrae la tasa de cambio específica.
    
    Esta es la función clave para la reutilización del módulo.

    Args:
        desde_moneda (str): Código de la moneda base (ej. 'USD').
        hacia_moneda (str): Código de la moneda destino (ej. 'EUR').

    Returns:
        float: La tasa de cambio correspondiente.

    Raises:
        ValueError: Si las monedas no son válidas o no tienen soporte.
        requests.RequestException: Si ocurre un problema con la red o el servidor.
    """
    desde_moneda = desde_moneda.strip().upper()
    hacia_moneda = hacia_moneda.strip().upper()
    
    url = f"https://open.er-api.com/v6/latest/{desde_moneda}"
    
    # timeout de 5 segundos para evitar que el código se quede congelado
    respuesta = requests.get(url, timeout=5)
    
    if respuesta.status_code != 200:
        raise requests.RequestException(f"El servidor respondió con código {respuesta.status_code}.")
        
    datos = respuesta.json()
    
    if datos.get("result") == "error" or datos.get("result") != "success":
        raise ValueError(f"La moneda '{desde_moneda}' no es válida o no está soportada.")
        
    tasas = datos.get("rates", {})
    
    if hacia_moneda not in tasas:
        raise ValueError(f"No se encontró la moneda de destino '{hacia_moneda}'.")
        
    return float(tasas[hacia_moneda])


def convertir_divisas(monto: float, desde_moneda: str, hacia_moneda: str) -> float:
    """Realiza la conversión matemática utilizando la tasa de cambio obtenida.

    Args:
        monto (float): Cantidad de dinero a convertir.
        desde_moneda (str): Moneda de origen.
        hacia_moneda (str): Moneda de destino.

    Returns:
        float: El monto final convertido.
    """
    tasa = obtener_tasa_cambio(desde_moneda, hacia_moneda)
    return monto * tasa


def conversor_tiempo_real() -> None:
    """Ejecuta la interfaz de consola del conversor de divisas en tiempo real."""
    print("--- CONVERSOR DE DIVISAS EN TIEMPO REAL ---")
    print("Lista de códigos de monedas más comunes:")  
    print("USD: Dólar estadounidense   | EUR: Euro              | GBP: Libra esterlina")
    print("JPY: Yen japonés            | AUD: Dólar australiano | CAD: Dólar canadiense")
    print("MXN: Peso mexicano          | BRL: Real brasileño    | CLP: Peso chileno")
    print("COP: Peso colombiano        | ARS: Peso argentino")
    print("-" * 50)

    desde_moneda = obtener_codigo_moneda("Convertir desde (ej. USD): ")
    hacia_moneda = obtener_codigo_moneda("Convertir a (ej. EUR): ")
    monto = obtener_monto(desde_moneda)

    print("\n  Consultando tasas de cambio en vivo...")
    
    try:
        # Usamos las funciones de lógica 
        tasa_cambio = obtener_tasa_cambio(desde_moneda, hacia_moneda)
        resultado = convertir_divisas(monto, desde_moneda, hacia_moneda)
        
        print("\n=================== RESULTADO ===================")
        print(f"[Tasa actual: 1 {desde_moneda} = {tasa_cambio:,.4f} {hacia_moneda}]")
        print(f"{monto:,.2f} {desde_moneda} equivalen a {resultado:,.2f} {hacia_moneda}")
        print("=================================================")
            
    except ValueError as e:
        print(f"\n  Error de validación: {e}")
    except requests.exceptions.Timeout:
        print("\n  Error: El servidor tardó demasiado en responder. Inténtalo más tarde.")
    except requests.exceptions.RequestException as e:
        print(f"\n  Error de conexión: {e}")


if __name__ == "__main__":
    # Esto solo se ejecuta si corres este script de forma directa
    conversor_tiempo_real()