"""Cet module contient des fonction pour dessiner
des figure geometrique avec la bibiotheque Turtle.

Auteurs: Fatou DIOUF, fatou.diouf2@univ-thies.sn
         Makhtar SARR, makhtar.sarr@univ-thies.sn.
"""

from turtle import*
from math import*

figure = Turtle()

# Objectifs:
# Methode:
# Besoins:
# Connus:
# Entrees:
# Sorties:
# Resultats:
# Hypotheses:
def cercle(rayon, couleur = "black"):
    figure.color(couleur)
    figure.circle(rayon)

# Objectifs:
# Methode:
# Besoins:
# Connus:
# Entrees:
# Sorties:
# Resultats:
# Hypotheses:
def demiCercle(rayon, couleur = "black"):
    figure.color(couleur)
    figure.circle(rayon, 180)
# Objectifs:
# Methode:
# Besoins:
# Connus:
# Entrees:
# Sorties:
# Resultats:
# Hypotheses:
def carre(cote, couleur = "black", ramplis = "white"):
    figure.color(couleur, ramplis)
    for i in range(4):
        figure.forward(cote)
        figure.left(90)

# Objectifs:
# Methode:
# Besoins:
# Connus:
# Entrees:
# Sorties:
# Resultats:
# Hypotheses:
def triangle(coteA, coteB, coteC, couleur = "black", couleur1 = "white"):
    figure.color(couleur, couleur1)
    angleB = degrees(acos(((coteA**2) + (coteB**2) - (coteC**2))/(2*coteA*coteB)))
    figure.forward(coteA)
    figure.left(180 - angleB)
    angleC = degrees(acos(((coteB**2) + (coteC**2) - (coteA**2))/(2*coteB*coteC)))
    figure.forward(coteB)
    figure.left(180 - angleC)
    figure.forward(coteC)
    angleA = degrees(acos(((coteB**2) + (coteA**2) - (coteC**2))/(2*coteB*coteA)))
    figure.left(180 - angleA)

# Objectifs:
# Methode:
# Besoins:
# Connus:
# Entrees:
# Sorties:
# Resultats:
# Hypotheses:
def rectangle(longueur, largeur, couleur = "black", couleur2='black'):
    figure.color(couleur, couleur2)
    if longueur != largeur:
        for i in range(2):
            figure.forward(longueur)
            figure.left(90)
            figure.forward(largeur)
            figure.left(90)
    else:
        print("erreur")

# Objectifs:
# Methode:
# Besoins:
# Connus:
# Entrees:
# Sorties:
# Resultats:
# Hypotheses:
def polygone(nbrCote, cote1, cote2 = 0, cote3 = 0):
    if nbrCote == 3 and cote3 != 0:
        triangle(cote1, cote2, cote3)
    elif nbrCote == 4 and cote2 == 0:
        carre(cote1)
    elif nbrCote == 4 and cote3 == 0:
        rectangle(cote1, cote2)
    elif nbrCote > 4 and cote2 == 0:
        for i in range(nbrCote):
            figure.forward(cote1)
            figure.left(360/nbrCote)
    else:
        print("erreur")

# Objectifs:
# Methode:
# Besoins:
# Connus:
# Entrees:
# Sorties:
# Resultats:
# Hypotheses:

def trapeze(base1, base2, coteD, coteG, couleur = "black", couleur2 = "black"):
    figure.color(couleur, couleur2)
    figure.forward(base1)
    figure.left(30)
    figure.forward(coteD)
    figure.left(150)
    figure.forward(base2)
    figure.left(150)
    figure.forward(coteG)

# Objectifs:
# Methode:
# Besoins:
# Connus:
# Entrees:
# Sorties:
# Resultats:
# Hypotheses:

def losange(cote, couleur = "black", couleur2 = "black"):
    figure.color(couleur, couleur2)
    figure.right(-30)
    for i in range(4):
        figure.forward(cote)
        figure.right(60*(1+i%2))

# Objectifs:
# Methode:
# Besoins:
# Connus:
# Entrees:
# Sorties:
# Resultats:
# Hypotheses:
def elypse(rayon, couleur = "black"):
    figure.color(couleur)
    figure.left(135)
    for i in range(2) :
        figure.circle(rayon, 90)
        figure.circle(rayon//4, 90)
def demiElypse(rayon, couleur = "black"):
    figure.left(45)
    figure.circle(rayon//35, 90)
    figure.circle(rayon, 90)
    figure.circle(rayon//35, 90)

# trapeze(30, 50, 20, 20)