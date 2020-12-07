# -*- coding: utf-8 -*-
"""
Created on Mon Dec 7 13:30:51 2020

@author: Axel François

to do : rendre ça beau et débuguer la winstreak

En vrai, j'ai honte de rendre ce programme, il est tellement mal codé et 
necessite au moins 3 heures de travail de plus
"""

#-------------------------Import----------------------------------------------#

from tkinter import Tk, Label, StringVar, Entry, Button, Canvas, PhotoImage
from Fonctions import lectureDonnee, fAjouteur
import random
import string


#-------------------------Fonctions-------------------------------------------#

def fTour():
    """Cette fonction s'occupe de chaque tour de jeu et est appellée par le
    bouton valider"""
    global Mot, Display, ListeLettreEntrée, Vie, Winstreak  #Les globals c'est moche mais pas le choix
    
    SetLettre = set(string.ascii_uppercase)

    NouvelleLettre = str(Saisie.get()).upper()  #Recupère la lettre
    
    if Vie == 0 or Display == Mot:    #Bloque le programme si le joueur n'a plus de vie ou le mot est trouvé
        return
    
    if NouvelleLettre not in SetLettre: #Bloque le programme si la chaine de carractère mis en entrée n'est pas une lettre
        return
    
    if NouvelleLettre not in ListeLettreEntrée:
        if NouvelleLettre not in Mot:
            Vie -= 1
            ListeLettreEntrée.append(NouvelleLettre)
        else:
            Display, ListeLettreEntrée,Vie = fAjouteur(Mot, NouvelleLettre, 
                                                          Display, 
                                                          ListeLettreEntrée,Vie)
    """Update des afficheurs"""
    TexteLettreListe.config(text = ListeLettreEntrée)   
    TexteMotADecouvrir.config(text = " ".join(Display))
    TexteNombreVie.config(text = ListeLettreEntrée)
    TexteWinstreak.config(text =str('Winstreak : '+str(Winstreak)))
    TexteNombreVie.config(text = str('Vie : '+str(Vie)))
    
    """Update des images"""
    if Vie == 8:
        item = CanvasPhoto.create_image(150, 150, image =photo1)
    elif Vie == 7:
        item = CanvasPhoto.create_image(150, 150, image =photo2)
    
    elif Vie == 6:
        item = CanvasPhoto.create_image(150, 150, image =photo3)
    
    elif Vie == 5:
        item = CanvasPhoto.create_image(150, 150, image =photo4)
    
    elif Vie == 4:
        item = CanvasPhoto.create_image(150, 150, image =photo5)
    
    elif Vie == 3:
        item = CanvasPhoto.create_image(150, 150, image =photo6)
    
    elif Vie == 2:
        item = CanvasPhoto.create_image(150, 150, image =photo7)
    
    elif Vie == 1:
        item = CanvasPhoto.create_image(150, 150, image =photo8)
    
    elif Vie == 0:
        item = CanvasPhoto.create_image(150, 150, image =photo9)
        TexteMotADecouvrir.config(text = " ".join(Mot))
        Winstreak = 0
   
    if Display == Mot:
       Winstreak += 1
   
def fRejouer():
    """Cette fonction s'occupe d'initialiser et de réinitialiser le programme"""
    global Mot, Display, ListeLettreEntrée, Vie, Winstreak  
    Mot = random.choice(ListeMot)  #Choisi le mot
    ListeLettreEntrée = []
    
    try:    #C'est moche mais ça permet de détecter s'il s'agit de l'initialisation ou d'un rejouer
        Display
    except NameError:
        Display = "_"*len(Mot)
    else:
        Display = "_"*len(Mot)
        Display,ListeLettreEntrée,Vie = fAjouteur(Mot, Mot[0], Display, 
                                                  ListeLettreEntrée, Vie)   #ça aussi c'est pas beau...
        TexteLettreListe.config(text = ListeLettreEntrée)
        TexteMotADecouvrir.config(text = " ".join(Display))
        
    Vie = 8
    #Pour avoir la première lettre
    Display,ListeLettreEntrée,Vie = fAjouteur(Mot, Mot[0], Display, 
                                                  ListeLettreEntrée, Vie)  
    


#-------------------------Initialisations-------------------------------------#
Winstreak = 0
ListeMot = lectureDonnee('Mot_Pendu.csv')


#-------------------------Boucle principale-----------------------------------#

fRejouer()

"""Partie en cours"""
FenetrePendu = Tk()
boutonQuitter = Button(FenetrePendu, bg='lightgrey', text = 'Quitter', fg = 'red', command = FenetrePendu.destroy)
boutonRejouer = Button(FenetrePendu, bg='lightgrey', text = 'Rejouer', command = fRejouer)
boutonProposer = Button(FenetrePendu, bg='lightgrey', text = 'Proposer', command = fTour)

      
#création de widgets 'Label' et 'Entry' :
TexteMotADecouvrir = Label(FenetrePendu, text =" ".join(Display))
TexteProposition = Label(FenetrePendu, text ='Entrez une lettre : ')
TexteLettre = Label(FenetrePendu, text ='Lettres déjà données :')
TexteLettreListe = Label(FenetrePendu, text = ListeLettreEntrée)
TexteWinstreak = Label(FenetrePendu, text =str('Winstreak : '+str(Winstreak)))
TexteNombreVie = Label(FenetrePendu, text = str('Vie : '+str(Vie)))
Saisie= StringVar()
BarreSaisie = Entry(FenetrePendu, textvariable = Saisie)


    
# création du widget 'Canvas'et importation des images :
CanvasPhoto = Canvas(FenetrePendu, width =300, height =300, bg ='white')
photo1 = PhotoImage(file ='Images/bonhomme1.gif')
photo2 = PhotoImage(file ='Images/bonhomme2.gif')
photo3 = PhotoImage(file ='Images/bonhomme3.gif')
photo4 = PhotoImage(file ='Images/bonhomme4.gif')
photo5 = PhotoImage(file ='Images/bonhomme5.gif')
photo6 = PhotoImage(file ='Images/bonhomme6.gif')
photo7 = PhotoImage(file ='Images/bonhomme7.gif')
photo8 = PhotoImage(file ='Images/bonhomme8.gif')
photo9 = PhotoImage(file ='Images/bonhomme9.gif')
  
item = CanvasPhoto.create_image(150, 150, image =photo1)
       
# Mise en page à l'aide de la méthode 'grid' :
TexteMotADecouvrir.grid(row =1, column =2)
TexteProposition.grid(row =2, column =1)
TexteLettre.grid(row =3, column =1)
TexteLettreListe.grid(row =3, column =2)
TexteWinstreak.grid(row =4, column =2)
TexteNombreVie.grid(row =4, column =4)
BarreSaisie.grid(row =2, column =2,)
CanvasPhoto.grid(row =1, column =4, rowspan =3, padx =10, pady =5)

boutonQuitter.grid(row =5, column =2)
boutonProposer.grid(row =2, column =3)
boutonRejouer.grid(row =5, column =1)
  

FenetrePendu.title("Jeu du Pendu")
FenetrePendu.mainloop()

#-------------------------Batch de test---------------------------------------#
"""
A chaque fois, toutes les bonnes lettres puis aléatoires
Mêmes éléments que pour le console :
Mot = "Myrmecologiste"
Mot = "Machin"
Mot = "Test1111" #casse le jeu, normal
Testé avec +20 mots du document

-> le winstreak marche pas
"""