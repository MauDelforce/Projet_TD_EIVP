## Importations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


#utilise impout pour date de debut et date de fin

tableau = pd.read_csv(r"C:\Users\perso\Documents\GitHub\Projet_TD_EIVP\EIVP_KM.csv", sep = ";")

#print(tableau)
#saved_column = tableau.column_name


mycolomns = ['temp','humidity']
print(tableau[mycolomns])

# plt.plot(tableau['sent_at'],tableau['noise'])
# plt.show()

def min(liste):
	if len(liste)==1 or len(liste)==0:
		return 0
	a = liste[0]
	for i in range(1,len(liste)):
		if a >liste[i]:
			a = liste[i]
	return a

def max(liste):
	if len(liste)==1 or len(liste)==0:
		return 0
	a = liste[0]
	for i in range(1,len(liste))==0:
		if a < liste[i]:
			a = liste[i]
	return a


def moyennet(liste):
	if len(liste)== 0 or len(liste)==1:
		return 0
	a = 0
	for i in range(1,len(liste)):
		a+=liste(i)
	return a/len(liste)

