"""Cet module contient des fonction pour dessiner
des figure geometrique avec la bibiotheque Turtle.

Auteurs: Fatou DIOUF, fatou.diouf2@univ-thies.sn
         Makhtar SARR, makhtar.sarr@univ-thies.sn.
"""

import genieCivilOuvrage2D as des
from turtle import*

# Dessin du mur avec un rectangle en bordure noire et avec une peinture en gris claire
des.figure.penup()
des.figure.setpos(-250, -200)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(500, 250, "black", "light grey")
des.figure.end_fill()
# Fin de la dessin du mur

# Dessin du mur en bas
des.rectangle(500, 10)
# Fin de la dessin du mur en bas

# Dessin du plafond avec un contour en noir et un fond en gris
des.figure.penup()
des.figure.setpos(-250, 50)
des.figure.pendown()
des.figure.begin_fill()
des.trapeze(500, 585, 50, 50, "black", "light grey")
des.figure.end_fill()
# Fin du dessin du plafond

# Dessin de la fenetre 1 en partant de la gauche
des.figure.penup()
des.figure.left(30)
des.figure.setpos(-235, -185)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(50, 225, "black", "dark grey")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(-230, -175)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(40, 130, "black", "white")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(-230, -175)
des.figure.pendown()
des.rectangle(20, 130)

des.figure.penup()
des.figure.setpos(-230, -175)
des.figure.pendown()
des.rectangle(40, 65)

des.figure.penup()
des.figure.setpos(-230, -10)
des.figure.pendown()
des.figure.begin_fill()
des.carre(40, "black", "white")
des.figure.end_fill()

des.figure.setpos(-230, -10)
des.rectangle(40, 20)

des.figure.setpos(-230, -10)
des.rectangle(20, 40)
# Fin dessin de la fenetre 1

# Dessin de la fenetre 2 en partant de la gauche
des.figure.penup()
des.figure.setpos(-165, -185)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(50, 225, "black", "dark grey")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(-160, -175)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(40, 130, "black", "white")
des.figure.end_fill()

des.figure.setpos(-160, -175)
des.rectangle(20, 130, "black", "white")

des.figure.setpos(-160, -175)
des.rectangle(40, 65, "black", "white")

des.figure.penup()
des.figure.setpos(-160, -10)
des.figure.pendown()
des.figure.begin_fill()
des.carre(40, "black", "white")
des.figure.end_fill()

des.figure.setpos(-160, -10)
des.rectangle(40, 20)

des.figure.setpos(-160, -10)
des.rectangle(20, 40)
# Fin dessin de la fenetre 2

# Dessin de la fenetre 3 en partant de la gauche
des.figure.penup()
des.figure.setpos(-95, -185)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(50, 225, "black", "dark grey")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(-90, -175)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(40, 130, "black", "white")
des.figure.end_fill()

des.figure.setpos(-90, -175)
des.rectangle(20, 130, "black", "white")

des.figure.setpos(-90, -175)
des.rectangle(40, 65, "black", "white")

des.figure.penup()
des.figure.setpos(-90, -10)
des.figure.pendown()
des.figure.begin_fill()
des.carre(40, "black", "white")
des.figure.end_fill()

des.figure.setpos(-90, -10)
des.rectangle(40, 20)

des.figure.setpos(-90, -10)
des.rectangle(20, 40)
# Fin dessin de la fenetre 3

# Dessin de la fenetre 1 en partant de la droite
des.figure.penup()
des.figure.left(90)
des.figure.setpos(235, -185)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(225, 50, "black", "dark grey")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(230, -175)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(130, 40, "black", "white")
des.figure.end_fill()

des.figure.setpos(230, -175)
des.rectangle(130, 20, "black", "white")

des.figure.setpos(230, -175)
des.rectangle(65, 40, "black", "white")

des.figure.penup()
des.figure.setpos(230, -10)
des.figure.pendown()
des.figure.begin_fill()
des.carre(40, "black", "white")
des.figure.end_fill()

des.figure.setpos(230, -10)
des.rectangle(20, 40)

des.figure.setpos(230, -10)
des.rectangle(40, 20)
# Fin dessin de la fenetre 1

# Dessin de la fenetre 2 en partant de la droite
des.figure.penup()
des.figure.setpos(165, -185)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(225, 50, "black", "dark grey")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(160, -175)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(130, 40, "black", "white")
des.figure.end_fill()

des.figure.setpos(160, -175)
des.rectangle(130, 20, "black", "white")

des.figure.setpos(160, -175)
des.rectangle(65, 40, "black", "white")

des.figure.penup()
des.figure.setpos(160, -10)
des.figure.pendown()
des.figure.begin_fill()
des.carre(40, "black", "white")
des.figure.end_fill()

des.figure.setpos(160, -10)
des.rectangle(20, 40)

des.figure.setpos(160, -10)
des.rectangle(40, 20)
# Fin dessin de la fenetre 2

# Dessin de la fenetre 3 en partant de la droite
des.figure.penup()
des.figure.setpos(95, -185)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(225, 50, "black", "dark grey")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(90, -175)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(130, 40, "black", "white")
des.figure.end_fill()

des.figure.setpos(90, -175)
des.rectangle(130, 20, "black", "white")

des.figure.setpos(90, -175)
des.rectangle(65, 40, "black", "white")

des.figure.penup()
des.figure.setpos(90, -10)
des.figure.pendown()
des.figure.begin_fill()
des.carre(40, "black", "white")
des.figure.end_fill()

des.figure.setpos(90, -10)
des.rectangle(20, 40)

des.figure.setpos(90, -10)
des.rectangle(40, 20)
# Fin dessin de la fenetre 3

# Dessin du poto 1 en fond blanc
des.figure.penup()
des.figure.setpos(38, -190)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(240, 75, "black", "white")
des.figure.end_fill()
# Fin dessin du poto 1

# Dessin du poto 2 en fond blanc
des.figure.penup()
des.figure.setpos(33, -190)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(240, 65, "black", "white")
des.figure.end_fill()
# Fin dessin du poto 2

# Dessin des escalier
des.figure.penup()
des.figure.setpos(31, -190)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(5, 61, "black", "white")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(29, -185)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(5, 57, "black", "white")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(27, -180)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(5, 53, "black", "white")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(25, -175)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(5, 49, "black", "white")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(23, -170)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(5, 45, "black", "white")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(21, -165)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(5, 41, "black", "white")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(38, -160)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(5, 75, "black", "white")
des.figure.end_fill()
# Fin dessin des escalier

# Dessin du mur de la porte
des.figure.penup()
des.figure.setpos(28, -155)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(205, 55, "black", "light grey")
des.figure.end_fill()
# Fin dessin du mur de la porte

# Dessin de l'ouverture de la porte
des.figure.penup()
des.figure.setpos(18, -155)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(70, 35, "black", "white")
des.figure.end_fill()
# Fin dessin de l'ouverture

# Dessin de la marche de la porte
des.figure.penup()
des.figure.setpos(18, -160)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(5, 35, "black", "white")
des.figure.end_fill()
# Fin dessin de la marche

# Dessin des vitre de la porte
des.figure.penup()
des.figure.setpos(18, -155)
des.figure.pendown()
des.rectangle(70, 17)

des.figure.penup()
des.figure.setpos(18, -155)
des.figure.pendown()
des.carre(35)
# Fin dessin des vitre

# Dessin du dome de la porte
des.figure.penup()
des.figure.setpos(18, -85)
des.figure.pendown()
des.demiCercle(17.5)
# Fin dessin de la porte

# Dessin de l'ouverture circulaire
des.figure.penup()
des.figure.setpos(-10, -35)
des.figure.pendown()
des.figure.begin_fill()
des.cercle(10)
des.figure.end_fill()
# Fin dessin de l'ouverture

# Dessin du vitre en haut de l'ouverture circulaire
des.figure.penup()
des.figure.setpos(-14, 20)
des.figure.pendown()
des.figure.begin_fill()
des.carre(28, "black")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(-14, 20)
des.figure.pendown()
des.rectangle(28, 14)
# Fin dessin du vitre

# Dessin du balcon
des.figure.penup()
des.figure.setpos(-43, 45)
des.figure.left(90)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(88, 30, "black", "white")
des.figure.end_fill()
# Fin dessin du balcon

# Dessin du mur de la case avec ses fenetres
des.figure.penup()
des.figure.setpos(-185, 75)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(100, 40, "black", "white")
des.figure.end_fill()

des.figure.setpos(-175, 75)
des.rectangle(20, 30)

des.figure.setpos(-175, 75)
des.rectangle(10, 30)

des.figure.setpos(-145, 75)
des.rectangle(20, 30)

des.figure.setpos(-145, 75)
des.rectangle(10, 30)

des.figure.setpos(-115, 75)
des.rectangle(20, 30)

des.figure.setpos(-115, 75)
des.rectangle(10, 30)

des.figure.penup()
des.figure.setpos(-85, 75)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(175, 40, "black", "white")
des.figure.end_fill()

des.figure.setpos(-70, 75)
des.rectangle(20, 30)

des.figure.setpos(-70, 75)
des.rectangle(10, 30)

des.figure.setpos(-35, 75)
des.rectangle(20, 30)

des.figure.setpos(-35, 75)
des.rectangle(10, 30)

des.figure.setpos(-5, 75)
des.rectangle(20, 30)

des.figure.setpos(-5, 75)
des.rectangle(10, 30)

des.figure.setpos(25, 75)
des.rectangle(20, 30)

des.figure.setpos(25, 75)
des.rectangle(10, 30)

des.figure.setpos(60, 75)
des.rectangle(20, 30)

des.figure.setpos(60, 75)
des.rectangle(10, 30)

des.figure.penup()
des.figure.setpos(90, 75)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(100, 40, "black", "white")
des.figure.end_fill()

des.figure.setpos(100, 75)
des.rectangle(20, 30)

des.figure.setpos(100, 75)
des.rectangle(10, 30)

des.figure.setpos(130, 75)
des.rectangle(20, 30)

des.figure.setpos(130, 75)
des.rectangle(10, 30)

des.figure.setpos(160, 75)
des.rectangle(20, 30)

des.figure.setpos(160, 75)
des.rectangle(10, 30)
# Fin dessin du mur de la case

# Dessin de la toiture
des.figure.penup()
des.figure.setpos(-135, 115)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(275, 33, "black", "light green")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(90, 115)
des.figure.pendown()
des.figure.begin_fill()
des.triangle(100, 60, 60, "black", "light green")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(-185, 115)
des.figure.pendown()
des.figure.begin_fill()
des.triangle(100, 60, 60, "black", "light green")
des.figure.end_fill()
# Fin du dessin de la toiture

exitonclick()