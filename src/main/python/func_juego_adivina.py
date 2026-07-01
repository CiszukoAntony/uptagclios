import random
import utils

def juego_adivina_el_numero():
    """
    Ejecuta el juego completo de 'Adivina el número'.
    
    Esta función centraliza toda la lógica del juego:
    1. Muestra la bienvenida.
    2. Genera un número aleatorio entre 1 y 100.
    3. Solicita y valida que la entrada del usuario sea un número entero.
    4. Compara el intento, da pistas (alto/bajo) y cuenta los intentos.
    5. Permite reiniciar el juego al terminar.
    """
    while True:
        # Configuración inicial de la partida
        numero_secreto = random.randint(1, 100)
        intentos = 0
        adivinado = False
        
        # Bienvenida
        print("=" * 45)
        print(f"{utils.ansi_text.GREEN} ¡BIENVENIDO AL JUEGO DE ADIVINA EL NÚMERO! ")
        print("=" * 45)
        print("He pensado un número entre 1 y 100.")
        print("Intenta adivinarlo en el menor número de intentos posible.\n")
        
        # Bucle principal de la partida actual
        while not adivinado:
            intentos += 1
            print(f"--- Intento número {intentos} ---")
            
            # Bucle de solicitud y validación de datos
            while True:
                try:
                    intento_usuario = int(input("Introduce tu número: "))
                    break  # Salimos del bucle de validación si es un entero válido
                except ValueError:
                    print("❌ Entrada inválida. Por favor, introduce un número entero.")
            
            # Verificación del número
            if intento_usuario < numero_secreto:
                print("➡️ Demasiado bajo. ¡Intenta con uno más grande!\n")
            elif intento_usuario > numero_secreto:
                print("➡️ Demasiado alto. ¡Intenta con uno más chico!\n")
            else:
                print("\n🎉 ¡Felicidades! ¡Has adivinado el número secreto!")
                print(f"🏆 Te tomó un total de {intentos} intentos ganar la partida.\n")
                adivinado = True
        
        # Preguntar si desea volver a jugar
        otra_vez = input("¿Quieres jugar otra partida? (s/n): ").lower().strip()
        if otra_vez != 's':
            print("\n👋 ¡Gracias por jugar! Hasta la próxima.")
            break
        print("\n" * 2)  # Separador para la nueva partida

# Para ejecutar el juego directamente
if __name__ == "__main__":
    juego_adivina_el_numero()
