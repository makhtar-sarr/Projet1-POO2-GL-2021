"""Cet module contient des fonction pour dessiner
des figure geometrique avec la bibiotheque Turtle.

Auteurs: Fatou DIOUF, fatou.diouf2@univ-thies.sn
         Makhtar SARR, makhtar.sarr@univ-thies.sn.
"""

from turtle import*
from math import*

figure = Turtle()

# Objectifs: Dessiner un cercle avec la bibliothèque Turtle.
# Methode: Utilisation de la méthode circle.
# Besoins: rayon et couleur (optionnelle).
# Connus: -
# Entrees: rayon.
# Sorties: -
# Resultats: dessin d'un cercle.
# Hypotheses: rayon > 0.
def cercle(rayon, couleur = "black"):
    figure.color(couleur)
    figure.circle(rayon)

# Objectifs: Dessiner un demi-cercle avec la bibliothèque Turtle.
# Methode: Utilisation de la méthode circle.
# Besoins: rayon et couleur (optionnelle).
# Connus: -
# Entrees: rayon.
# Sorties: -
# Resultats: dessin d'un demi-cercle.
# Hypotheses: rayon > 0.
def demiCercle(rayon, couleur = "black"):
    figure.left(90)
    figure.color(couleur)
    figure.circle(rayon, 180)

# Objectifs: Dessiner un carré avec la bibliothèque Turtle.
# Methode: Utilisation des méthodes forward et left dans une boucle for.
# Besoins: coté, couleur (optionnelle).
# Connus: -
# Entrees: coté.
# Sorties: -
# Resultats: dessin d'un carré.
# Hypotheses: coté > 0.
def carre(cote, couleur = "black", remplis = "white"):
    figure.color(couleur, remplis)
    for i in range(4):
        figure.forward(cote)
        figure.left(90)

# Objectifs: Dessiner un triangle avec la bibliothèque Turtle.
# Methode: Utilisation des méthodes de directions.
# Besoins: coteA,coteB,coteC, couleurs (optionnelle).
# Connus: -
# Entrees: coteA,coteB,coteC.
# Sorties: -
# Resultats: dessin d'un triangle.
# Hypotheses: coteA > 0,coteB > 0,coteC > 0.
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

# Objectifs: Dessiner un rectangle avec la bibliothèque Turtle.
# Methode: utilisation des méthodes de direction dans une boucle for.
# Besoins: longueur,largeur, couleur.
# Connus: -
# Entrees: longueur,largeur.
# Sorties: -
# Resultats: dessin d'un triangle.
# Hypotheses: longueur > 0, largeur > 0, longueur > largeur.
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

# Objectifs: Dessin d'un polygone avec la bibliothèque turtle.
# Methode: Utilisation des méthodes de direction dans une boucle for avec des test de condition et l'utilisation.
#  des méthodes triangle, carre et rectangle.
# Besoins: nbrCote, cote1, cote2,(optionnel) cote3 (optionnel).
# Connus: -
# Entrees: nbrCote, cote1, cote2, cote3.
# Sorties: -
# Resultats: dessin d'un polygone.
# Hypotheses: nbrCote >= 3, cote1 > 0, cote2 > 0, cote3 > 0.
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

# Objectifs: Dessin d'un trapèze avec la bibliothèque turtle
# Methode: Utilisation des méthodes de direction
# Besoins: base1,base2,coteD, coteG, couleurs(optionnel)
# Connus: -
# Entrees: base1,base2,coteD, coteG
# Sorties: -
# Resultats: dessin d'un trapèze
# Hypotheses: base1 > 0, base2 > 0, base1 > base2,coteD > 0, cote
def trapeze(base1, base2, coteD, coteG, couleur = "black", couleur2 = "black"):
    figure.color(couleur, couleur2)
    figure.forward(base1)
    figure.left(30)
    figure.forward(coteD)
    figure.left(150)
    figure.forward(base2)
    figure.left(150)
    figure.forward(coteG)

# Objectifs: Dessiner un losange avec la bibliothèque turtle
# Methode: utilisation des méthodes de direction dans une boucle for
# Besoins: coté, couleur (optionnel)
# Connus: -
# Entrees: coté
# Sorties: -
# Resultats: Dessin d'un losange
# Hypotheses: coté > 0
def losange(cote, couleur = "black", couleur2 = "black"):
    figure.color(couleur, couleur2)
    figure.right(-30)
    for i in range(4):
        figure.forward(cote)
        figure.right(60*(1+i%2))

# Objectifs: dessiner un ellipse avec la bibliothèque turtle
# Methode: utilisation des méthodes de direction dans une boucle for
# Besoins: rayon , couleur (optionnel)
# Connus: -
# Entrees: rayon
# Sorties: -
# Resultats: dessin d'une ellipse
# Hypotheses: rayon > 0
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
