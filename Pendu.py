# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:10:36 2020

@author: Axel François
"""

#-------------------------Import----------------------------------------------#
import csv
import random


#-------------------------Fonctions-------------------------------------------#

def lectureDonnee(doc):
    """Cette fonction lit un document csv doc et retourne son contenue sous 
    forme de liste"""
    
    valren = []
    with open(doc, newline='') as csvfile:
        document = csv.reader(csvfile)
        for row in document:
            valren.append(', '.join(row))
    return valren


def fAjouteur(pMot, pLettreEntrée, pDisplay, pListeLettreDonnée,pVie):
    """Cette fonction vérifie si pLettreEntrée est dans pMot, et si c'est le 
    cas elle modifie pDisplay pour rajouter la lettre. Elle ajoute ensuite 
    cette lettre a pListeLettreDonnée. La fonction a pour paramètre pMot (str),
    pLettreEntrée (str de taille 1), pDisplay (str de même taille que pMot), 
    pListeLettreDonnée (liste) et pVie (int). La fonction retourne pDisplay 
    (str), pListeLettreDonnée (liste), et pVie (int)"""
    
    if pLettreEntrée not in pMot:
        pListeLettreDonnée.append(pLettreEntrée)
        return pDisplay, pListeLettreDonnée,pVie-1
    
    pMot = list(pMot)
    pDisplay = list(pDisplay)
    for i in range(len(pMot)):
        if pMot[i] == pLettreEntrée:
            pDisplay[i] = pLettreEntrée
    pListeLettreDonnée.append(pLettreEntrée)
    pDisplay = ''.join(pDisplay)    
    
    return  pDisplay, pListeLettreDonnée, pVie


def fAfficher(pVie):
    """Cette fonction print le pendu associé à la valeur pVie. La fonction a
    pour paramètre pVie (int)"""
    
    if pVie == 8:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    
    elif pVie == 7:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("---------")
    
    elif pVie == 6:
        print("")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("---------")
    
    elif pVie == 5:
        print("______")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("---------")
    
    elif pVie == 4:
        print("______")
        print("|/   |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("---------")
    
    elif pVie == 3:
        print("______")
        print("|/   |")
        print("|    O")
        print("|")
        print("|")
        print("|")
        print("---------")
    
    elif pVie == 2:
        print("______")
        print("|/   |")
        print("|    O")
        print("|    |")
        print("|")
        print("|")
        print("---------")
    
    elif pVie == 1:
        print("______")
        print("|/   |")
        print("|    O")
        print("|   /|\ ")
        print("|")
        print("|")
        print("---------")
    
    elif pVie == 0:
        print("______")
        print("|/   |")
        print("|    O")
        print("|   /|\ ")
        print("|   / \ ")
        print("|")
        print("---------")


def fTour(pMot, pDisplay, pListeLettreDonnée,pVie):
    """Cette fonction s'occupe de chaque tour de jeu. Elle appelle la fonction 
    pour afficher le pendu, puis vérifie que le joueur ait encore des vies.
    Elle affiche les lettres trouvées, la liste des lettres proposées, puis
    propose d'entrer une nouvelle lettre. Elle vérifie que la lettre n'a pas
    déjà été proposée  puis fait appel à la fonction fAjouteur pour faire
    l'ajout. La fonction a pour paramètre pMot (str), pDisplay (str, même
    taille que pMot), pListeLettreDonnée (liste) et pVie (int). Elle retourne
    la valeur de Game (booléen, condition de sortie), pVie (int) et pDisplay 
    (str)"""
    
    ListeLettre = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
                   'P','Q','R','S','T','U','V','W','X','Y','Z']
    
    fAfficher(pVie)
    
    if pVie == 0:    
        return False,pVie,pDisplay
        
    print(" ".join(pDisplay))
    print("Liste des lettres déjà proposée :", pListeLettreDonnée)
    print("\nEntrez votre lettre")
    NouvelleLettre = str(input()).upper()
    
    if NouvelleLettre not in ListeLettre:
        print("Pas une lettre ou plusieurs caractères, recommencez")
        return True,pVie,pDisplay
    
    if NouvelleLettre not in pListeLettreDonnée:
        pDisplay, pListeLettreDonnée,pVie = fAjouteur(pMot, NouvelleLettre, 
                                                      pDisplay, 
                                                      pListeLettreDonnée,pVie)
    else:
        print("La lettre a déjà été proposée")
    
    if pDisplay == pMot:    
        return False,pVie,pDisplay
    else:
        return True,pVie,pDisplay


#-------------------------Initialisations-------------------------------------#

Winstreak = 0
Play = True
ListeMot = lectureDonnee('Mot_Pendu.csv')


#-------------------------Boucle principale-----------------------------------#

while Play == True:
    """Initialisation de la partie"""    
    Mot = ListeMot[random.randint(0,len(ListeMot)-1)]   #Choisi le mot
    ListeLettreEntrée = []
    Display = "_"*len(Mot)
    Game = True
    Vie = 8
    Display,ListeLettreEntrée,Vie = fAjouteur(Mot, Mot[0], Display, 
                                              ListeLettreEntrée, Vie)
    #Pour avoir la première lettre
    
    while Game == True:
        """Partie en cours"""
        Game,Vie,Display = fTour(Mot, Display, ListeLettreEntrée, Vie)
        
    """Fin de partie"""    
    if Vie == 0:
        print("Oh non, vous avez perdu. Le mot était", Mot)
        Winstreak = 0
    else:
        Winstreak +=1
        print("Bravo, vous avez gagné ! Le mot était {}.".format(Mot), end ='')
        print("Votre série de victoire est de {}.".format(Winstreak))
                
    """Rejouer"""    
    print("Voulez vous rejouer ? [y/n]")
    PlayAgain = input()
    while PlayAgain != 'y' and PlayAgain != 'n':
        print("Vous n'avez pas répondu correctement. ",end = '')
        print("Voulez vous rejouer ? [y/n]")
        PlayAgain = input()
    if PlayAgain == 'n':
        Play = False

        
#-------------------------Batch de test---------------------------------------#
"""
A chaque fois, toutes les bonnes lettres puis aléatoires
Mot = "Myrmecologiste"
Mot = "Machin"
Mot = "Test1111" #casse le jeu, normal
Testé avec +20 mots du document
"""