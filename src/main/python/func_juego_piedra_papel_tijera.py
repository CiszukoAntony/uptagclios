import random
def jugar():
    """
    
    Ejecuta una partida del juego Piedra, Papel o Tijera contra la computadora.
     ---
     
    La función solicita la elección del usuario por consola, valida la entrada,
    genera una opción aleatoria para la computadora y determina el resultado
    (gana el usuario, gana la computadora o hay un empate).
    
    inputs:
       usuario = input("Elige una opción (piedra, papel, tijera): ").lower()
    
    
    """
    opciones = ["piedra", "papel", "tijera"]
    
    print("=" * 35)
    print("¡Bienvenido a Piedra, Papel o Tijera!")
    print("=" * 35)
    
    # Entrada del jugador
    usuario = input("Elige una opción (piedra, papel, tijera): ").lower()
    
    # Validar que la entrada sea correcta
    if usuario not in opciones:
        print("❌ Opción no válida. Inténtalo de nuevo escribiendo piedra, papel o tijera.")
        return

    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"\nTú elegiste: {usuario.capitalize()}")
    print(f"La computadora eligió: {computadora.capitalize()}\n")
    
    # Determinar el ganador
    if usuario == computadora:
        print("🤝 ¡Es un empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("🎉 ¡Ganaste! ¡Felicitaciones!")
    else:
        print("😢 Perdiste. ¡Suerte para la próxima!")

# Ejecutar el juego
if __name__ == "__main__":
    jugar()
