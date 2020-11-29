# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:10:36 2020

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

Test = lectureDonnee('Mot_Pendu.csv')
print(Test)
print(isinstance(Test[0],str))