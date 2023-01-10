from math import *
import os, sys
import random
random.seed()

# Fonction qui affiche la grille
def affichage_grille(grille):
    # int(sqrt(len(grille)) correspond à la longeur/largeur de la grille
    # ici la grille est un carré de 5*5 alors int(sqrt(len(grille))=5
    print("╔═════╦═════╦═════╦═════╦═════╦═════╗")
    print("║     ║  A  ║  B  ║  C  ║  D  ║  E  ║")
    for ligne in range(int((len(grille) ** 0.5))):  # pour ligne allant de 0 à 4
        print("╠═════╬═════╬═════╬═════╬═════╬═════╣")
        print("║ ", (ligne + 1), " ║", end="")  # on print la valeur de la ligne
        for colonne in range(int((len(grille) ** 0.5))):  # pour colonne allant de 0 à 4
            print(" ", grille[ligne * int((len(grille)**0.5)) + colonne], " ║", end="")  # ligne*5+colonne
        print()
    print("╚═════╩═════╩═════╩═════╩═════╩═════╝")


# Fonction qui teste si une coordonnée est bien située dans la grille
def est_dans_grille(ligne, colonne, grille):
    # On teste si la ligne est située entre 0 et la fin de la grille (ici 4)
    if ligne < str(0) or ligne > str(len(grille) ** 0.5):  ## len(grille)**0.5 == sqrt(len(grille))
        return False
    # On teste si la colonne est située entre 0 et la fin de la grille (ici 4)
    if ord(colonne) - 64 < 0 or ord(colonne) - 64 > len(grille) ** 0.5:
        # ord(colonne) convertit une lettre en un nombre en partant de "A"=65, suivi de "B"=66, etc...
        # donc ord(colonne)-64 avec "A" donne 1 pour exemple
        return False
    return True


##Teste si la position écrite a bien 2 valeur (une ligne, une colonne)
def Position_valide(coordonnee):
    while len(coordonnee) != 2:
        print("Cette coordonnée n'est pas valide")
        print("Veuillez ressaisir des coordonnees")
        coordonnee = input()
    return coordonnee


# Fonction qui va demander d'écrire une coordonnee et tester si elle est située dans la grille ou non
def saisir_coordonnees(grille):
    print("Entrez une coordonnée xy valide (entre 1A et 5E)")
    coordonnee = input()  # on demande une coordonnee
    coordonnee = Position_valide(coordonnee)  # on teste si cette coordonnee a bien deux valeurs
    while (est_dans_grille(coordonnee[0], coordonnee[1], grille) == False):
        # tant que la coordonnee n'est pas située dans la grille on répète le même processus
        print("Cette coordonnée n'est pas situé dans la grille, veuillez ressaisir des coordonnnees")
        coordonnee = input()
        coordonnee = Position_valide(coordonnee)  # teste si coordonnee a deux valeurs
    return coordonnee


def choix_grille():
    print("Choisissez une grille \n", "1 pour la grille du début de partie \n",
          "2 pour une grille de milieu de partie \n", "3 pour une grille de fin de partie \n") # \n revient à la ligne
    choix = None  # on met aucun type à choix pour rentrer dans la boucle
    while isinstance(choix, int) == False:  # tant que choix n'est pas un entier on redemande une valeur valide
        try:
            choix = int(input())
            while not (1 <= choix <= 3):  # si choix n'est pas compris entre 0 et 3
                print("Votre nombre n'est pas compris entre 0 et 3:")
                choix = int(input())
        except ValueError:
            print("Vous devez écrire un nombre entre 0 et 3")  # si choix n'est pas un entier on renvoie ce message
    if choix == 1: grille, tour = ["O"] * 3 + ["X"] * 2 + ["O"] * 3 + ["X"] * 2 + ["O"] * 2 + [" "] + ["X"] * 2 + ["O"] * 2 + ["X"] * 3 + ["O"] * 2 + ["X"] * 3, 1  # configuration grille du début, tour=1 correspond au joueur 1
    if choix == 2: grille, tour = [" "] + ["O"] + [" "] * 3 + ["O"] * 3 + [" "] + ["X"] + ["O"] + [" "] + ["X"] + [" "] + ["O"] + [" "] * 2 + ["X"] * 3 + ["O"] * 2 + ["X"] * 3 , 1  # configuration grille de milieu, tour=1 correspond au joueur 1
    if choix == 3: grille, tour = [" "] * 7 + ["X"] + [" "] * 3 + ["X"] + [" "] + ["O"] + [" "] + ["O"] + [" "] * 7 + ["O"] * 2, 2  # configuration grille de fin cas pas assez de pions
    
    return grille, tour


# Fonction qui permet de passer au joueur suivant
def joueur_suivant(tour):
    if tour == 1:
        tour = 2
        return tour
    if tour == 2:
        tour = 1
        return tour


# Fonction qui affiche quel joueur à le droit de jouer
def affichage_tour(tour):
    if tour == 1:
        print("C'est au tour du joueur ", tour, " ('O')")
        return tour
    if tour == 2:
        print("C'est au tour du joueur ", tour, "('X')")
        return tour


# Fonction qui permet de sélectionner un pion et qui vérifie bien que l'on a pas choisi une coordonnée vide
def selection_pion(grille):
    print("Selectionnez un pion:")
    coordonnee_pion = saisir_coordonnees(grille)  # Permet d'affecter une coordonnée valide au pion
    ligne, colonne = int(coordonnee_pion[0]), ord(coordonnee_pion[1]) - 64  # Coordonnées de la ligne/colonne
    while grille[(ligne - 1) * int(len(grille) ** 0.5) + (
            colonne - 1)] == " ":  # tant l'ensemble ligne/colonne ne correspond pas à un pion (on fait colonne-1 et ligne-1 car le début d'une liste est liste[0] et non liste[1])
        print("Vous avez selectionné une case vide, veuillez selectionner un pion:")
        coordonnee_pion = saisir_coordonnees(grille)  # On redemande une coordonnée valide à affecter au pion
        ligne, colonne = int(coordonnee_pion[0]), ord(coordonnee_pion[1]) - 64  # Permet d'actualiser le test while
    return coordonnee_pion


##Teste si on a sélectionné le bon pion (allié)
def test_deplacement_simple_tour(ligne_pion, colonne_pion, grille, tour):
    if tour == 1:  # si c'est au tour du joueur 1
        pion_allie, pion_adverse = "O", "X"
    if tour == 2:  # si c'est au tour du joueur 2
        pion_allie, pion_adverse = "X", "O"
    if not grille[(ligne_pion - 1) * int(len(grille) ** 0.5) + (
            colonne_pion - 1)] == pion_allie:  # si les coordonnées du pion choisi ne correspondent pas à un pion allié
        print("Vous devez sélectionner un pion allié!")
        return False
    return True


# Fonction de test qui vérifie la validité du déplacement simple
def test_deplacement_simple(coordonnee_pion, coordonnee_deplacement, tour):
    ligne_pion, colonne_pion = int(coordonnee_pion[0]), ord(
        coordonnee_pion[1]) - 64  # Coordonnées de la ligne/colonne du pion
    ligne_deplacement, colonne_deplacement = int(coordonnee_deplacement[0]), ord(
        coordonnee_deplacement[1]) - 64  # Coordonnées de la ligne/colonne du déplacement
    # si on a pas choisi un pion allié
    if test_deplacement_simple_tour(ligne_pion, colonne_pion, grille, tour) == False:
        return False
    if coordonnee_pion == coordonnee_deplacement:  # teste si les deux coordonnées sont égales
        print("Vous essayez de déplacer le pion sur lui-même!")
        return False
    if grille[(ligne_deplacement - 1) * int(len(grille) ** 0.5) + (
            colonne_deplacement - 1)] != " ":  # teste si les coordonnées de coordonnee_deplacement ne correspondent pas à un pion dans la grille
        print("Il y a déjà un pion ici!")
        return False
    if (not ((1 <= abs(ligne_deplacement - ligne_pion) <= 1 and abs(colonne_deplacement - colonne_pion) == 0) or (
            1 <= abs(colonne_deplacement - colonne_pion) <= 1 and abs(ligne_deplacement - ligne_pion) == 0) or(
            1 <= abs(ligne_deplacement - ligne_pion) <= 1 and 1 <= abs(colonne_deplacement - colonne_pion) <= 1 
            ))):
        print("Il y a une trop grande distance dans votre déplacement!")
        return False
    return True


# Fonction qui permet d'effectuer un déplacement simple (d'une case à une case adjacente)
def deplacement_simple(grille, tour):
    coordonnee_pion = selection_pion(grille)  # On demande de sélectionner un pion
    print("Où voulez-vous déplacer le pion?")
    coordonnee_deplacement = saisir_coordonnees(grille)  # On demande où veux-t-on le déplacer
    if test_deplacement_simple(coordonnee_pion, coordonnee_deplacement,
                               tour) == False:  # On vérifie la validité du déplacement
        return choix_deplacement(grille, tour)  # return pour éviter que la fonction continue de marcher
    # Affecte la valeur du pion dans la zone de la grille où on veut le déplacer
    grille[(int(coordonnee_deplacement[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_deplacement[1]) - 64 - 1)] = \
    grille[(int(coordonnee_pion[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 - 1)]
    # Supprime la valeur du pion initial dans la grille
    grille[(int(coordonnee_pion[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 - 1)] = ' '
    return True


# Fonction de test qui vérifie la validité du déplacement saut en fonction du tour du joueur
def test_deplacement_saut_tour(coordonnee_pion, coordonnee_deplacement, ligne_pion, colonne_pion, ligne_deplacement,
                               colonne_deplacement, tour, pion_allie, pion_adverse):
    if grille[(ligne_pion - 1) * int(len(grille) ** 0.5) + (colonne_pion - 1)] != pion_allie:
        print("Vous devez sélectionner un pion allié!")
        return False
    if grille[(ligne_deplacement - 1) * int(len(grille) ** 0.5) + (
            colonne_deplacement - 1)] == pion_adverse:  # teste si les coordonnées de coordonnee_deplacement correspondent à un pion adverse dans la grille
        print("Vous ne pouvez pas sauter ici!")
        return False
    if grille[(ligne_deplacement - 1) * int(len(grille) ** 0.5) + (
            colonne_deplacement - 1)] != ' ' :  # teste si les coordonnées de coordonnee_deplacement ne correspondent pas à une case vide dans la grille
        print("Vous ne pouvez pas sauter ici!")
        return False
    if ((colonne_pion == colonne_deplacement and ligne_deplacement == ligne_pion + 2)):  # cas saut vers le bas
        if grille[(int(ligne_pion)) * int(len(
                grille) ** 0.5) + colonne_pion - 1] != pion_adverse:  # on vérifie la ligne au dessus
            print("Vous devez sauter par dessus un pion adverse")
            return False
        return True
    if ((colonne_pion == colonne_deplacement and ligne_deplacement == ligne_pion - 2)):  # cas saut vers le haut
        if grille[(int(ligne_pion - 2)) * int(len(
                grille) ** 0.5) + colonne_pion - 1] != pion_adverse:  # on vérifie la ligne en dessous
            print("Vous devez sauter par dessus un pion adverse")
            return False
        return True
    if ((ligne_deplacement == ligne_pion and colonne_deplacement == colonne_pion + 2)):  # cas saut vers la droite
        if grille[(int(ligne_pion - 1)) * int(len(
                grille) ** 0.5) + colonne_pion] != pion_adverse:  # on vérifie la ligne à droite
            print("Vous devez sauter par dessus un pion adverse")
            return False
        return True
    if ((ligne_deplacement == ligne_pion and colonne_deplacement == colonne_pion - 2)):  # cas saut vers la gauche
        if grille[(int(ligne_pion - 1)) * int(len(
                grille) ** 0.5) + colonne_pion - 2] != pion_adverse:  # on vérifie la ligne à gauche
            print("Vous devez sauter par dessus un pion adverse")
            return False
        return True
  


# Fonction de test qui vérifie la validité du déplacement saut
def test_deplacement_saut(coordonnee_pion, coordonnee_deplacement, tour):
    ligne_pion, colonne_pion = int(coordonnee_pion[0]), ord(coordonnee_pion[1]) - 64
    ligne_deplacement, colonne_deplacement = int(coordonnee_deplacement[0]), ord(coordonnee_deplacement[1]) - 64
    if (not ((2 <= abs(ligne_deplacement - ligne_pion) <= 2 and abs(colonne_deplacement - colonne_pion) == 0) or (
            2 <= abs(colonne_deplacement - colonne_pion) <= 2 and abs(ligne_deplacement - ligne_pion) == 0) or (
              (2 <= abs(ligne_deplacement - ligne_pion) <= 2 and 2 <= abs(colonne_deplacement - colonne_pion)<= 2)
            ))):
      print("Il y a une trop grande distance dans votre déplacement!")
      return False
    if tour == 1:  # si c'est au tour du joueur 1
        pion_allie, pion_adverse = "O", "X"
        # On effectue une seconde série de test en rapport avec le tour du joueur
        if test_deplacement_saut_tour(coordonnee_pion, coordonnee_deplacement, ligne_pion, colonne_pion,
                                      ligne_deplacement, colonne_deplacement, tour, pion_allie, pion_adverse) == False:
            return False
        else:
            return True

    if tour == 2:  # si c'est au tour du joueur 2
        pion_allie, pion_adverse = "X", "O"
        # On effectue une seconde série de test en rapport avec le tour du joueur
        if test_deplacement_saut_tour(coordonnee_pion, coordonnee_deplacement, ligne_pion, colonne_pion,
                                      ligne_deplacement, colonne_deplacement, tour, pion_allie, pion_adverse) == False:
            return False
        else:
          return True
    if coordonnee_pion == coordonnee_deplacement:  # teste si les deux coordonnées sont égales
        print("Vous essayez de déplacer le pion sur lui-même!")
        return False
    # Vérifie si coordonnee_deplacement est bien à 2 de distances par rapport à coordonnee_pion, et également sur une case allignée
    if not ((ligne_deplacement == ligne_pion and colonne_deplacement == colonne_pion + 2) or (
            ligne_deplacement == ligne_pion and colonne_deplacement == colonne_pion - 2)
            or (colonne_deplacement == colonne_pion and ligne_deplacement == ligne_pion + 2) or (
                    colonne_deplacement == colonne_pion and ligne_deplacement == ligne_pion - 2)):
        print("Vous devez effectuer un saut de 2 cases allignées au maximum")
        return False


def deplacement_saut(grille, tour):
    coordonnee_pion = selection_pion(grille)  # On demande de sélectionner un pion
    print("Où voulez-vous déplacer le pion?")
    coordonnee_deplacement = saisir_coordonnees(grille)  # On demande où veux-t-on le déplacer
    if test_deplacement_saut(coordonnee_pion, coordonnee_deplacement, tour) == False:
        return False  # return pour éviter que la fonction continue de marcher
    # Affecte la valeur du pion dans la zone de la grille où on veut le déplacer
    else:
      grille[(int(coordonnee_deplacement[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_deplacement[1]) - 64 - 1)] = \
      grille[(int(coordonnee_pion[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 - 1)]
      # Supprime la valeur du pion initial dans la grille
      grille[(int(coordonnee_pion[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 - 1)] = ' '
      # Supprime la valeur du pion en cas de la direction diagonal vers en bas la droite
      grille[(int(coordonnee_pion[0])) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64)] = ' '
      # Supprime la valeur du pion en cas de la direction diagonal vers en bas la gauche
      grille[(int(coordonnee_pion[0])) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 -2)] = ' '
      #dia haut gauche
      grille[(int(coordonnee_pion[0])-2) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 -2)] = ' '
      #dia haut droite
      grille[(int(coordonnee_pion[0])-2) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64)] = ' '
      #haute
      grille[(int(coordonnee_pion[0]) - 2) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 - 1)] = ' '
      #bas
      grille[(int(coordonnee_pion[0])) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 - 1)] = ' '
      #droite
      grille[(int(coordonnee_pion[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64)] = ' '
      #gauche
      grille[(int(coordonnee_pion[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 -2)] = ' '
      return True


def test_fin_de_partie_bloque(grille, pion_allie, pion_adverse):
    pion_adjacent, mouvement_impossible = 0, 0
    for ligne in range(int(len(grille) ** 0.5)):  # Pour ligne allant de 0 à 5
        for colonne in range(int(len(grille) ** 0.5)):  # Pour colonne allant de 0 à 5
            if grille[ligne * int(
                    len(grille) ** 0.5) + colonne] == pion_allie:  # On effectue les tests pour chaque pions alliés
                if ligne - 1 != -1:  # On teste si on ne sort pas de la grille en haut
                    pion_adjacent += 1  # On compte chaques pions adjacents au pion allié
                    if grille[(ligne - 1) * int(len(
                            grille) ** 0.5) + colonne] == pion_adverse:  # Si le pion adjacent est un pion adverse, aucun mouvement n'est possible
                        mouvement_impossible += 1
                    else:
                        return False  # Si le pion adjacent n'est pas un pion adverse, alors le joueur n'est pas bloqué
                if ligne + 1 != 5:  # On teste si on ne sort pas de la grille en bas
                    pion_adjacent += 1
                    if grille[(ligne + 1) * int(len(grille) ** 0.5) + colonne] == pion_adverse:
                        mouvement_impossible += 1
                    else:
                        return False
                if colonne - 1 != -1:  # On teste si on ne sort pas de la grille à gauche
                    pion_adjacent += 1
                    if grille[(ligne) * int(len(grille) ** 0.5) + colonne - 1] == pion_adverse:
                        mouvement_impossible += 1
                    else:
                        return False
                if colonne + 1 != 5:  # On teste si on ne sort pas de la grille à droite
                    pion_adjacent += 1
                    if grille[(ligne) * int(len(grille) ** 0.5) + colonne + 1] == pion_adverse:
                        mouvement_impossible += 1
                    else:
                        return False
    if pion_adjacent == mouvement_impossible:
        return True


def fin_de_partie(grille, tour):
    X, O = 0, 0
    # TEST CAS PAS ASSEZ DE PIONS:
    for element in grille:  # On parcourt la liste  et compte chaque occurence de "X" et "O"
        if element == "X": X += 1
        if element == "O": O += 1
    if O == 0:  # S'il y a moins de 2 pions d'un type, la partie est terminée
        print("Le joueur 1 n'a plus de pions pour jouer => gagnant J2")
        return True
    if X == 0:  # S'il y a moins de 2 pions d'un type, la partie est terminée
        print("Le joueur 2 n'a plus de pions pour jouer => gagnant J1")
        return True
    if tour == 1:  # Si c'est au tour du joueur 1 ('O')
        pion_allie, pion_adverse = "O", "X"
        if test_fin_de_partie_bloque(grille, pion_allie,
                                     pion_adverse) == True:  # On teste que ce joueur n'est pas bloqué
            print("Le joueur 1 est bloqué")
            return True  # S'il est bloqué, alors la partie est terminée
    if tour == 2:  # Si c'est au tour du joueur 2 ('X')
        pion_allie, pion_adverse = "X", "O"
        if test_fin_de_partie_bloque(grille, pion_allie,
                                     pion_adverse) == True:  # On teste que ce joueur n'est pas bloqué
            print("Le joueur 2 est bloqué")
            return True  # S'il est bloqué, alors la partie est terminée
    return False


def choix_deplacement(grille, tour):
    print("Choisissez un type de déplacement \n", "0 pour un déplacement simple (sur des cases adjacentes) \n",
          "1 pour sauter par dessus un pion")  # \n revient à la ligne
    choix = None  # on met aucun type à choix pour rentrer dans la boucle
    while isinstance(choix, int) == False:  # tant que choix n'est pas un entier on redemande une valeur valide
        try:
            choix = int(input())
            while not (0 <= choix <= 1):  # si choix n'est pas compris entre 0 et 1
                print("Votre nombre n'est pas compris entre 0 et 1:")
                choix = int(input())
        except ValueError:
            print("Vous devez écrire un nombre entre 0 et 1")  # si choix n'est pas un entier on renvoie ce message
    if choix == 0:  # le joueur a choisit un déplacement simple
        if deplacement_simple(grille, tour) == False:  # si le déplacement n'est pas valide
            choix_deplacement(grille,
                              tour)  # on redemande un type de déplacement (au cas où le joueur s'est trompé de déplacement)
        else:
            tour_suivant = joueur_suivant(tour)  # si le déplacement a été effectué, on passe au tour suivant
            return tour_suivant
    if choix == 1:  # le joueur a choisit un déplacement avec saut
        if deplacement_saut(grille, tour) == False:  # si le déplacement n'est pas valide
            choix_deplacement(grille,
                              tour)  # on redemande un type de déplacement (au cas où le joueur s'est trompé de déplacement)
        else:
            tour_suivant = joueur_suivant(tour)  # si le déplacement a été effectué, on passe au tour suivant
            return tour_suivant

def tests_fonctions():
    grille_test_coordonnee = [" "] * 25
    # TEST COORDONNEES
    assert not est_dans_grille("A", 6, grille_test_coordonnee), "erreur hors ligne inferieure"
    assert not est_dans_grille("A", 0, grille_test_coordonnee), "erreur hors ligne superieure"
    assert not est_dans_grille("a", 1, grille_test_coordonnee), "erreur hors colonne inferieure"
    assert not est_dans_grille("F", 1, grille_test_coordonnee), "erreur hors colonne superieure"


#Fonction qui s'occupe de créer la sous-liste de toutes les valeurs possibles de déplacement pour un pion
def IAn_creation_liste_de_deplacements(grille, tour, coordonnee_pion):
    liste_deplacement=[]
    for ligne in range(int(len(grille) ** 0.5)):  # Pour ligne allant de 0 à 4
        for colonne in range(int(len(grille) ** 0.5)):  # Pour colonne allant de 0 à 4
            coordonnee_deplacement = str(ligne+1)+chr(colonne+65) #string prenant les valeurs ligne+1 et colonne+1 (car on va de 0 à 4 dans la boucle for in range)
            if test_deplacement_simple(coordonnee_pion, coordonnee_deplacement, tour)==True: #si un déplacement est possible
                liste_deplacement.append(coordonnee_deplacement) #on rajoute les coordonnées du déplacements dans une liste
            if test_deplacement_saut(coordonnee_pion, coordonnee_deplacement, tour)==True:
                liste_deplacement.append(coordonnee_deplacement)
    return liste_deplacement


#Fonction qui s'occupe de créer la liste de liste de toutes les valeurs possibles de déplacement pour chaque pions
def IAn_coordonnee_deplacement(grille, tour,pion_allie):
    liste_deplacement=[] #Liste de liste de toutes les valeurs possibles de déplacements pour chaque pions
    for ligne in range(int(len(grille) ** 0.5)):  # Pour ligne allant de 0 à 4
        for colonne in range(int(len(grille) ** 0.5)):  # Pour colonne allant de 0 à 4
            if grille[ligne * int(len(grille) ** 0.5) + colonne] == pion_allie: #si les coordonnees (ligne,colonne) correspondent à un pion allié
                coordonnee_pion = str(ligne+1)+chr(colonne+65) #string prenant les valeurs ligne+1 et colonne+1 (car on va de 0 à 3 dans la boucle for in range)
                liste_deplacement_pion=IAn_creation_liste_de_deplacements(grille, tour, coordonnee_pion) #sous-liste de toutes les valeurs possibles de déplacement pour un pion
                if len(liste_deplacement_pion)>0: #si un mouvement est possible avec le pion
                    liste_deplacement_pion.append(coordonnee_pion) #Je mets les coordonnées du pion à la fin (***)
                    liste_deplacement.append(liste_deplacement_pion) #J'ajoute les valeurs de liste_deplacement_pion dans liste_deplacement
    if len(liste_deplacement)!=0:
        nombre_aleatoire_liste = random.randint(0, len(liste_deplacement)-1)
        return liste_deplacement[nombre_aleatoire_liste]


#Fonction qui s'occupe de déplacer un pion en utilisant deux variables coordonnee_pion et coordonnee_deplacement
def IAn_deplacement(grille, tour):
    if tour == 1:  # Si c'est au tour du joueur 1 ('O')
        pion_allie= "O"
    if tour == 2:  # Si c'est au tour du joueur 2 ('X')
        pion_allie= "X"
    liste_coordonnees_deplacement=IAn_coordonnee_deplacement(grille, tour,pion_allie) #ensemble de coordonnées possibles de déplacement pour un pion + coordonnées du pion
    coordonnee_pion=liste_coordonnees_deplacement[-1] #dernière valeur de la liste qui correspond aux coordonnées du pion (voir ***)
    nombre_aleatoire_liste = random.randint(0, len(liste_coordonnees_deplacement) - 2) #va du début de la liste a l'avant dernière valeur (pour éviter les coordonnées du pion)
    coordonnee_deplacement=liste_coordonnees_deplacement[nombre_aleatoire_liste]
    # Affecte la valeur du pion dans la zone de la grille où on veut le déplacer
    grille[(int(coordonnee_deplacement[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_deplacement[1]) - 64 - 1)] = \
    grille[(int(coordonnee_pion[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 - 1)]
    # Supprime la valeur du pion initial dans la grille
    grille[(int(coordonnee_pion[0]) - 1) * int(len(grille) ** 0.5) + (ord(coordonnee_pion[1]) - 64 - 1)] = ' '
    tour_suivant = joueur_suivant(tour)  # si le déplacement a été effectué, on passe au tour suivant
    return tour_suivant

def choix_mode():
    print("Choisissez un mode de jeu \n", "0 pour le mode joueur contre joueur \n",
          "1 pour le mode IA naïve \n")  # \n revient à la ligne
    choix = None  # on met aucun type à choix pour rentrer dans la boucle
    while isinstance(choix, int) == False:  # tant que choix n'est pas un entier on redemande une valeur valide
        try:
            choix = int(input())
            while not (0 <= choix <= 1):  # si choix n'est pas compris entre 0 et 1
                print("Votre nombre n'est pas compris entre 0 et 1:")
                choix = int(input())
        except ValueError:
            print("Vous devez écrire un nombre entre 0 et 1")  # si choix n'est pas un entier on renvoie ce message
    return choix

#Lorsque l'on affiche un print, il est redirigé vers le canal de communication stdout
#Le but de cette classe est de bloquer ce canal de communication (***)
class Cache_print():
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w') #(***)

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

########################################################################################################################
#PROGRAMME PRINCIPAL#
########################################################################################################################

#Le tour du joueur est choisi en fonction de la grille et on l'affiche
choix_mode=choix_mode()
grille, tour = choix_grille()

if choix_mode==0: #MODE JOUEUR CONTRE JOUEUR
    while fin_de_partie(grille, tour) == False: #tant que la partie n'est pas terminée, la boucle s'exécute
        affichage_tour(tour)
        affichage_grille(grille)
        tests_fonctions()
        tour=choix_deplacement(grille, tour) #effectue le mouvement et passe au tour suivant
        print("Le tour est terminé")
    else:
        affichage_grille(grille)
        print("La partie est terminée")

if choix_mode==1: #MODE IAn (IA naïve)
    tour_joueur=tour #variable qui définit le tour du joueur
    while fin_de_partie(grille, tour) == False:
        if tour==tour_joueur:
            affichage_tour(tour)
            print("C'est à vous de jouer")
            affichage_grille(grille)
            tests_fonctions()
            tour=choix_deplacement(grille, tour) #effectue le mouvement et passe au tour suivant
            affichage_grille(grille)
            print("Le tour est terminé")
        elif tour!=tour_joueur:
            print("C'est à l'IA de jouer")
            tests_fonctions()
            with Cache_print(): #En utilisant la classe Cache_print, cela empêche à l'IA d'afficher les prints d'erreurs quand un mouvement n'est pas possible
                tour=IAn_deplacement(grille, tour) #effectue le mouvement et passe au tour suivant
            print("L'IA a deplacé un pion")
    affichage_grille(grille)
    print("La partie est terminée")

input("Appuyer sur une touche pour quitter...")
