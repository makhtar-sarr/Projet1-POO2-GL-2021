# Projet1-POO2-GL-2021
C'est un projet de **Programmation Orientee Object 2** realise par **Fatou DIOUF** et **Makhtar SARR**, etudiants en **Licence 3 Informatique** option **Genie Logiciel**. Il s’agira de construire une bibliothèque de fonction, qui permettra le dessin de figures en utilisant l’outil turtle de python.
## Bibliotheque `genieCivilOuvrage2D.py`
Cette bibliotheque importe la bibliotheque `turtle`. Elle contient une variable `figure` de type `Turtle()` et les methodes suivantes:
* cercle;
* demi-cercle;
* carre;
* triangle;
* rectangle;
* polygone;
* trapeze;
* losange;
* elypse.
### Diagramme des flux
![DF](https://user-images.githubusercontent.com/78378063/128629994-6ee4acb3-a236-4cc6-ac17-3a78bba47e62.png)
### Tableau des flux
<table>
    <th>
        <tr>
            <td>Programme Principal</td>
            <td>Fournit(Entrées)</td>
            <td>Reçoit(Sorties)</td>
        </tr>
    </th>
    <tbody>
        <tr>
            <td>cercle</td>
            <td>rayon</td>
            <td>Rien</td>
        </tr>
        <tr>
            <td>demi-cercle</td>
            <td>rayon</td>
            <td>Rien</td>
        </tr>
        <tr>
            <td>Carre</td>
            <td>cote</td>
            <td>Rien</td>
        </tr>
        <tr>
            <td>triangle</td>
            <td>coteA, coteB, coteC</td>
            <td>Rien</td>
        </tr>
        <tr>
            <td>rectangle</td>
            <td>longueur, largeur</td>
            <td>Rien</td>
        </tr>
        <tr>
            <td>polygone</td>
            <td>nbrCote, cote1</td>
            <td>Rien</td>
        </tr>
        <tr>
            <td>trapeze</td>
            <td>base1, base2, coteD, coteG</td>
            <td>Rien</td>
        </tr>
        <tr>
            <td>losange</td>
            <td>cote</td>
            <td>Rien</td>
        </tr>
        <tr>
            <td>elypse</td>
            <td>rayon</td>
            <td>Rien</td>
        </tr>
    </tbody>
</table>
### Fonction cercle
#### Description
Cette methode dessine un **cercle** en utilisant la methode `circle` de la bibliotheque `turtle`. Elle prend en parametre le `rayon` du cercle a tracer en pixel, la `couleur` qui est optionnelle.
#### Code python
```python
def cercle(rayon, couleur = "black"):
    figure.color(couleur)
    figure.circle(rayon)
```
#### Resultat
```python
cercle(100)
```
![cercle](https://user-images.githubusercontent.com/78378063/128608950-c93aa567-d8b5-43b0-a6d5-7b0e6c30e102.png)
### Fonction demi-cercle
#### Description
Cette methode va nous permettre de dessiner un **demi-cercle** avec toujours la methode `circle` de `turtle`, mais dans ce cas nous allons renseigner l'angle d'arret. Elle prend un parametre obligatoire, le `rayon` et un optionnel, la `couleur`.
#### Code python
```python
def demiCercle(rayon, couleur = "black"):
    figure.left(90)
    figure.color(couleur)
    figure.circle(rayon, 180)
```
#### Resultat
```python
demiCercle(100)
```
![demiCercle](https://user-images.githubusercontent.com/78378063/128609126-f4271e8e-7a48-421a-9a74-d24c21b3b967.png)
### Fonction carre
#### Description
Cette methode va nous permettre de dessiner un carre avec `turtle` en utilisant une boucle `for`. Elle prend un parametre obligatoire, `cote` du carre en pixel et deux optionnels, la `couleur` et le remplissage ici `remplis`.
#### Code python
```python
def carre(cote, couleur = "black", remplis = "white"):
    figure.color(couleur, remplis)
    for i in range(4):
        figure.forward(cote)
        figure.left(90)
```
#### Resultat
```python
carre(100)
```
![carre](https://user-images.githubusercontent.com/78378063/128609147-3b75ede6-6ae7-4c26-880b-3976c24c2aad.png)
### Fonction triangle
#### Description
Cette methode va nous permettre de dessiner un **triangle** avec `turtle` en utilisant le théorème d’**Al Kashi!
**. Elle prend trois parametres obligatoires, `coteA`, `coteB`, `coteC` qui represente la mesure des trois cotes en pixel et deux optionnels, la `couleur` et le remplissage ici `couleur1`.
#### Code python
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
#### Resultat
```python
triangle(100, 90, 70)
```
![triangle](https://user-images.githubusercontent.com/78378063/128609388-a68bb3ff-51d4-4b25-9127-c0a47234f986.png)
### Fonction rectangle
#### Description
Cette methode va nous permettre de dessiner un **rectangle** avec `turtle` en utilisant une boucle `for`. Elle prend deux parametres obligatoires, `longueur`, `largeur` en pixel et deux optionnels, la `couleur` du contour et le remplissage ici `couleur2`.
#### Code python
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
#### Resultat
```python
rectangle(100, 50)
```
![rectangle](https://user-images.githubusercontent.com/78378063/128609309-ba7abaee-b9e0-410f-9e18-524124bf2dfb.png)
### Fonction polygone
#### Description
Cette methode va nous permettre de dessiner un **polygone** avec `turtle` en utilisant une boucle `for`. Elle prend deux parametres obligatoires, `nbrCote`, `cote1` et deux optionnels, `cote2` et `cote3`.
#### Code python
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
#### Resultat
```python
polygone(5, 50)
```
![polygone](https://user-images.githubusercontent.com/78378063/128609244-66415cb6-8629-44e4-b713-25ed24b0ba57.png)
### Fonction trapeze
#### Description
Cette methode va nous permettre de dessiner un **tapeze** avec `turtle` en utilisant des methodes telles que `forward` et `left`. Elle prend 4 parametres obligatoires, `base1`, `base2`, `coteD`, `coteG` et deux optionnels, `couleur` et `couleur2`.
#### Code python
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
#### Resultat
```python
trapeze(85, 210, 75, 75)
```
![trapeze](https://user-images.githubusercontent.com/78378063/128609348-c3cc5930-4aed-4a78-aee8-814355158002.png)
### Fonction losange
#### Description
Cette methode va nous permettre de dessiner un **losange** avec `turtle` en utilisant des methodes telles que `forward` qui nous permet d'avancer et `right` qui nous permet de tourner a l'angle voulu dans une boucle `for`. Elle prend un parametre obligatoires, `cote` et deux optionnels, `couleur` et `couleur2` pour le contour et le remplissage.
#### Code python
```python
def losange(cote, couleur = "black", couleur2 = "black"):
    figure.color(couleur, couleur2)
    figure.right(-30)
    for i in range(4):
        figure.forward(cote)
        figure.right(60*(1+i%2))
```
#### Resultat
```python
losange(100)
```
![losange](https://user-images.githubusercontent.com/78378063/128609215-59e351f6-4e0a-48b5-a906-97a272c145a0.png)
### Fonction elypse
#### Description
Cette methode va nous permettre de dessiner un **elypse** avec `turtle` en utilisant des methodes telles que `forward` qui nous permet d'avancer, `left` qui nous permet de tourner a gauche selon l'angle voulu, `circle` et une boucle `for`. Elle prend un parametre obligatoires, `rayon` et un optionnel, `couleur`.
#### Code python
```python
def elypse(rayon, couleur = "black"):
    figure.color(couleur)
    figure.left(135)
    for i in range(2) :
        figure.circle(rayon, 90)
        figure.circle(rayon//4, 90)
```
#### Resultat
```python
elypse(100)
```
![elypse](https://user-images.githubusercontent.com/78378063/128609183-7ca71ea9-40c5-43d1-98e2-7de467aa6020.png)  
Cliquer ici pour voir le code complet de [`genieCivilOuvrage2D.py`](https://github.com/makhtar-sarr/Projet1-POO2-GL-2021/blob/main/genieCivilOuvrage2D.py)
## Pont
Dans ce fichier on a dessine un pont grace aux bibliotheques `genieCivilOuvrage2D` et `turtle`. Ci-dessous se trouve le resulte du pont.  
![pont](https://user-images.githubusercontent.com/78378063/128631352-3c1483da-934e-4fe6-b9e2-83b37ff05238.png)  
Cliquer ici pour voir le code complet de [`pont.py`](https://github.com/makhtar-sarr/Projet1-POO2-GL-2021/blob/main/pont.py)
## Facade
Dans ce fichier on a dessine la facade d'un maison grace aux bibliotheques `genieCivilOuvrage2D` et `turtle`. Ci-dessous se trouve le resulte de la facade.  
![facade](https://user-images.githubusercontent.com/78378063/128631800-d023062b-842d-4042-850d-6a1d0f7a6031.png)  
Cliquer ici pour voir le code complet de [`facade.py`](https://github.com/makhtar-sarr/Projet1-POO2-GL-2021/blob/main/facade.py)
## Documentation
Cliquer ici pour voir la [documentation](https://github.com/makhtar-sarr/Projet1-POO2-GL-2021/blob/main/Projet1%20POO2%20LI3%20GL.pdf)
