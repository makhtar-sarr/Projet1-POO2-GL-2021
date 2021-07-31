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
def triangle(coteA, coteB, coteC):
    angleB = degrees(acos(((coteA**2) + (coteB**2) - (coteC**2))/(2*coteA*coteB)))
    figure.forward(coteA)
    figure.left(180 - angleB)
    angleC = degrees(acos(((coteB**2) + (coteC**2) - (coteA**2))/(2*coteB*coteC)))
    figure.forward(coteB)
    figure.left(180 - angleC)
    figure.forward(coteC)

triangle(100, 100, 90)