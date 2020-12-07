# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:10:36 2020

@author: Axel François
"""

#-------------------------Import----------------------------------------------#

import random
from Fonctions import *


#-------------------------Initialisations-------------------------------------#

Winstreak = 0
Play = True
ListeMot = lectureDonnee('Mot_Pendu.csv')


#-------------------------Boucle principale-----------------------------------#

while Play == True:
    """Initialisation de la partie"""    
    Mot = random.choice(ListeMot)  #Choisi le mot
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
        print("Bravo, vous avez gagné ! Le mot était {}.".format(Mot),end =' ')
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