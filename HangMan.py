import random

palabras = ["papaya", "melon", "sandia", "manzana", "mango"]

random.shuffle(palabras)

adivina = list(palabras[0])

mostrar = []

mostrar.extend(adivina)

for i in range(len(mostrar)):
    mostrar[i] = "_ "

print()

count = 0
intentos = 10

while count < len(adivina):
    print("Tienes ", intentos, " intentos para adivinar la palabra completa\n")
    usuario = input("Que letra contiene la palabra? \n")
    usuario = usuario.lower()

    for i in range(len(adivina)):
        if adivina[i] == usuario:
            mostrar[i] = usuario
            count += 1

    if usuario != adivina[i]:
        intentos = intentos - 1

    if intentos == 0:
        print("Perdiste! \nIntenta de nuevo!")
        break
    if count == len(adivina):
        print("Felicidades! \nGanaste!")

    print(" ".join(mostrar))
    print()
