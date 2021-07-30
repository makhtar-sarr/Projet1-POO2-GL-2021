"""Cet module contient des fonction pour dessiner
des figure geometrique avec la bibiotheque Turtle.

Auteurs: Fatou DIOUF, <votre mail ici>
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
def triangle(coteA, coteB, angleC):
    coteC = sqrt((coteA**2) + (coteB**2) - (2*coteA*coteB*cos(angleC)))
    figure.forward(coteA)
    figure.left(180 - angleC)
    figure.forward(coteB)
    angleB = degrees(acos(((coteA**2) + (coteB**2) - (coteC**2))/(2*coteA*coteB)))
    print(angleB)
    figure.left(180 - angleB)
    figure.forward(coteC)

triangle(50, 50, 30)