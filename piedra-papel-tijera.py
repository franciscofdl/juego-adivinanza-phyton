#-----------------------------------------
#OPCION 1

nombre1 = input("¿Cómo se llama el jugador 1?: ")
nombre2 = input("¿Cómo se llama el jugador 2?: ")

print("¡Hola",nombre1,"!")
jugador1 = input("¿Qué eliges? ¿Piedra, papel o tijera?: ")

print("¡Hola",nombre2,"!")
jugador2 = input("¿Qué eliges? ¿Piedra, papel o tijera?: ")

if jugador1 == jugador2:
    print("Ha sido un empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    print("Ha ganado", nombre1)
else:
    print("Ha ganado", nombre2)

#--------------------------------------------
#OPCION 2: Definiendo variables de condicion

nombre1 = input("¿Cómo se llama el jugador 1?: ")
nome2 = input("¿Cómo se llama el jugador 2?: ")

print("¡Hola",nombre1,"!")
jugador1 = input("¿Qué eliges? ¿Piedra, papel o tijera?: ")

print("¡Hola",nombre2,"!")
jugador2 = input("¿Qué eliges? ¿Piedra, papel o tijera?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado", nombre1)
else:
    print("Ha ganado", nombre2)