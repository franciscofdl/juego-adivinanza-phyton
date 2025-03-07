import random   

numero_secreto = random.randint(1,100)
adivinado = False
cant_max_intentos = 5
suma_cant_intentos = 0

print ("¡Bienvenido al juego de adivinar el número secreto. Tendrás", cant_max_intentos, "intentos")

while not adivinado and suma_cant_intentos < cant_max_intentos:
    entrada = input ("Ingrese un número del 1 al 99: ")
    numero = int (entrada)
    if numero == numero_secreto:
        print ("¡Felicitaciones! Has adivinado el número secreto")
        adivinado = True
        break
    
    elif numero < numero_secreto:
        print("El número secreto es mayor al ingresado")
    
    else:
        print("El número secreto es menor al ingresado")

    suma_cant_intentos += 1

if not suma_cant_intentos < cant_max_intentos:
    print("GAME OVER. No has podido adivinar dentro de los", cant_max_intentos, "intentos. El número secreto es", numero_secreto)
