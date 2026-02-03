import random
import turtle

def drawSquare():
    # Taille max en pixels
    MAX_SIZE = 400

    # la taille aléatoire 
    size = random.randint(1, MAX_SIZE)

    # choix aléatoire de la position
    turtle.setx(random.random(0, MAX_SIZE))
    turtle.sety(random.random(0, MAX_SIZE))


def drawTriangle():
    # Taille max en pixels
    MAX_SIZE = 400

    # la taille aléatoire 
    size = random.randint(1, MAX_SIZE)

    # choix aléatoire de la position
    turtle.setx(random.random(0, MAX_SIZE))
    turtle.sety(random.random(0, MAX_SIZE))


def drawCircle():
    # Taille max en pixels
    MAX_SIZE = 400

    # la taille aléatoire 
    size = random.randint(1, MAX_SIZE)

    # choix aléatoire de la position
    turtle.setx(random.random(0, MAX_SIZE))
    turtle.sety(random.random(0, MAX_SIZE))


# on demande à l'utilisateur de saisir un nombre entier entre 0 et 9
n = 0

while n < 0 and n > 9:
    print("[+] Saisir un nombre entier entre 0 - 9: ")
    if(n < 0 and n > 9):
        print(f"[!] {n} est invalide [!]")


# on dessine n formes géométriques aléatoires
for i in n:
    # on choisie la forme de manière aléatoire 
    form = random.randint(0, 2)

    # on dessine la forme
    if form == 0:
        drawCircle()
    elif form == 1:
        drawSquare()
    else:
        drawTriangle()
