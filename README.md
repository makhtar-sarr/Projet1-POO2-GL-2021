# Projet1-POO2-GL-2021
Il s’agira de construire une bibliothèque de fonction, qui permettra le dessin de figures en utilisant l’outil turtle de python.
## Fonction cercle
### Description
Cette methode dessine un **cercle** en utilisant la methode `circle` de la bibliotheque `turtle`. Elle prend en parametre le `rayon` du cercle a tracer en pixel, la `couleur` qui est optionnelle.
### Code python
```python
def cercle(rayon, couleur = "black"):
    figure.color(couleur)
    figure.circle(rayon)
```
### Resultat
```python
cercle(100)
```
[cercle(100)]: /images/cercle.png "cercle de rayon 100 px"
## Fonction demi-cercle
### Description
Cette methode va nous permettre de dessiner un **demi-cercle** avec toujours la methode `circle` de `turtle`, mais dans ce cas nous allons renseigner l'angle d'arret. Elle prend un parametre obligatoire, le `rayon` et un optionnel, la `couleur`.
### Code python
```python
def demiCercle(rayon, couleur = "black"):
    figure.left(90)
    figure.color(couleur)
    figure.circle(rayon, 180)
```
### Resultat
```python
demiCercle(100)
```
[demiCercle(100)]: /images/demiCercle.png "demi-cercle de rayon 100 px"
## Fonction carre
### Description
Cette methode va nous permettre de dessiner un carre avec `turtle` en utilisant une boucle `for`. Elle prend un parametre obligatoire, `cote` du carre en pixel et deux optionnels, la `couleur` et le remplissage ici `remplis`.
### Code python
```python
def carre(cote, couleur = "black", remplis = "white"):
    figure.color(couleur, remplis)
    for i in range(4):
        figure.forward(cote)
        figure.left(90)
```
### Resultat
```python
carre(100)
```
[carre(100)]: /images/carre.png "carre de cote 100 px"
## Fonction triangle
### Description
Cette methode va nous permettre de dessiner un **triangle** avec `turtle` en utilisant le théorème d’**Al Kashi**. Elle prend trois parametres obligatoires, `coteA`, `coteB`, `coteC` qui represente la mesure des trois cotes en pixel et deux optionnels, la `couleur` et le remplissage ici `couleur1`.
### Code python
```python
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
```
### Resultat
```python
triangle(100, 90, 70)
```
[triangle(100, 90, 70)]: /images/triangle.png "carre de cote 100 px"
## Fonction rectangle
### Description
Cette methode va nous permettre de dessiner un **rectangle** avec `turtle` en utilisant une boucle `for`. Elle prend deux parametres obligatoires, `longueur`, `largeur` en pixel et deux optionnels, la `couleur` du contour et le remplissage ici `couleur2`.
### Code python
```python
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
```
### Resultat
```python
rectangle(100, 50)
```
[rectangle(100, 50)]: /images/rectangle.png "retangle de longueur 100 et de largeur 50px"
## Fonction polygone
### Description
Cette methode va nous permettre de dessiner un **polygone** avec `turtle` en utilisant une boucle `for`. Elle prend deux parametres obligatoires, `nbrCote`, `cote1` et deux optionnels, `cote2` et `cote3`.
### Code python
```python
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
```
### Resultat
```python
polygone(5, 50)
```
[polygone(5, 50)]: /images/polygone.png "polygone de cote 5 de 50 px"
## Fonction trapeze
### Description
Cette methode va nous permettre de dessiner un **tapeze** avec `turtle` en utilisant des methodes telles que `forward` et `left`. Elle prend 4 parametres obligatoires, `base1`, `base2`, `coteD`, `coteG` et deux optionnels, `couleur` et `couleur2`.
### Code python
```python
def trapeze(base1, base2, coteD, coteG, couleur = "black", couleur2 = "black"):
    figure.color(couleur, couleur2)
    figure.forward(base1)
    figure.left(30)
    figure.forward(coteD)
    figure.left(150)
    figure.forward(base2)
    figure.left(150)
    figure.forward(coteG)
```
### Resultat
```python
trapeze(85, 210, 75, 75)
```
[trapeze(85, 210, 75, 75)]: /images/trapeze.png "trapeze de petite base 85 et de grande base 210px"
## Fonction losange
### Description
Cette methode va nous permettre de dessiner un **losange** avec `turtle` en utilisant des methodes telles que `forward` qui nous permet d'avancer et `right` qui nous permet de tourner a l'angle voulu dans une boucle `for`. Elle prend un parametre obligatoires, `cote` et deux optionnels, `couleur` et `couleur2` pour le contour et le remplissage.
### Code python
```python
def losange(cote, couleur = "black", couleur2 = "black"):
    figure.color(couleur, couleur2)
    figure.right(-30)
    for i in range(4):
        figure.forward(cote)
        figure.right(60*(1+i%2))
```
### Resultat
```python
losange(100)
```
[losange(100)]: /images/losange.png "losange de cote 100px"
## Fonction elypse
### Description
Cette methode va nous permettre de dessiner un **elypse** avec `turtle` en utilisant des methodes telles que `forward` qui nous permet d'avancer, `left` qui nous permet de tourner a gauche selon l'angle voulu, `circle` et une boucle `for`. Elle prend un parametre obligatoires, `rayon` et un optionnel, `couleur`.
### Code python
```python
def elypse(rayon, couleur = "black"):
    figure.color(couleur)
    figure.left(135)
    for i in range(2) :
        figure.circle(rayon, 90)
        figure.circle(rayon//4, 90)
```
### Resultat
```python
elypse(100)
```
[elypse(100)]: /images/elypse.png "elypse de rayon 100px"