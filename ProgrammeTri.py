# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:14:57 2020

@author: Axel François
"""
import csv

def lectureDonnee(doc):
    valren = []
    with open(doc, newline='') as csvfile:
        document = csv.reader(csvfile)
        for row in document:
            valren.append(', '.join(row))
    return valren

ListeMot = lectureDonnee('Mot_Pendu_Brut.csv')
ListeLettre = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#ListeMot.sort()

Lettre = []
for i in range(len(max(ListeMot, key=len))):
    Lettre.append([])

for item in ListeMot:
    Lettre[len(item)-1].append(item)
    

for liste in Lettre:
    liste.sort()
    
valren = []
for i in range(len(Lettre)-4):
    valren = valren + Lettre[i+4]



with open('Mot_Pendu.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(valren)):
        writer.writerow([str(valren[i])])