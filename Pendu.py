# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:10:36 2020

@author: Axel François
"""
import csv
import random

def lectureDonnee(doc):
    valren = []
    with open(doc, newline='') as csvfile:
        document = csv.reader(csvfile)
        for row in document:
            valren.append(', '.join(row))
    return valren

ListeMot = lectureDonnee('Mot_Pendu.csv')
ListeLettre = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


Play = True


def fTour(pMot, pLettreEntrée, pDisplay, pListeLettreDonnée):
    pMot = list(pMot)
    pDisplay = list(pDisplay)
    for i in range(len(pMot)):
        if pMot[i] == pLettreEntrée:
            pDisplay[i] = pLettreEntrée
    pListeLettreDonnée.append(pLettreEntrée)
    pDisplay = ''.join(pDisplay)    
    return  pDisplay, pListeLettreDonnée



    

while Play == True:
    Mot = ListeMot[random.randint(0,len(ListeMot)-1)]
    ListeLettreEntrée = []
    Display = "_"*len(Mot)
    
    Display,ListeLettreEntrée = fTour(Mot, Mot[0], Display, ListeLettreEntrée)
    Display,ListeLettreEntrée = fTour(Mot, Mot[-1], Display, ListeLettreEntrée)
        
    
    
    
    
    
    
    
    
    Play = False