## Importations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# 2 lignes pour le csv, impossible de travailler à deux sur la même ligne, commentaire à déplacer

tableau = pd.read_csv(r"C:\Users\perso\Documents\GitHub\Projet_TD_EIVP\EIVP_KM.csv", sep = ";")
#tableau = pd.read_csv(r"EIVP_KM.csv", sep = ";")


## Courbe

indice = input("donner l'indice du capteur (entre 1 et 6) :")
mycolomn = input('donner le nom de la colonne (temp, noise, humidity, co2, lum) :')


liste = tableau.loc[(tableau["id"]== int(indice)) , [mycolomn]]

liste = liste.values.tolist()

print(liste)

plt.plot(tableau.loc[(tableau["id"]== int(indice)),'sent_at'],liste)
plt.show()



## Fonctions statistiques

def min(liste):
	if len(liste)==1 or len(liste)==0:
		return 0
	a = liste[0]
	for i in range(1,len(liste)):
		if a >liste[i][0]:
			a = liste[i][0]
	return a

def max(liste):
	if len(liste)==1 or len(liste)==0:
		return 0
	a = liste[0]
	for i in range(1,len(liste))==0:
		if a < liste[i][0]:
			a = liste[i][0]
	return a


def moyenne(liste):
	if len(liste)== 0 or len(liste)==1:
		return 0
	a = 0
	for i in range(1,len(liste)):
		a = a+liste[i][0]
	return a/len(liste)


def variance(liste):
	a=0
	if len(liste)== 0 or len(liste)==1:
		return 0
	for i in range(1,len(liste)):
		a = a + (liste[i][0]-moyenne(liste))**2
	return a/len(liste)

def ecartType(liste):
	return np.sqrt(variance(liste))


def quicksort(liste):
	if L==[]:
		return L
	else :
		To=L[0]
		Tinf=[]
		Tsup=[]
		for x in L[1:]:
			if x<=To:
				Tinf.append(x)
			else:
				Tsup.append(x)
	return quicksort(Tinf)+[To]+quicksort(Tsup)

def medianne(liste):
	L = quicksort(liste)
	return L[len(liste)/2]

def humidex(temperature,humidity):
	humidex = temperature + (5/9)*(6.112*(10*(7.5*(temperature/(237.7+temperature))))*(humidity/100)-10)
	return humidex



## Recherche des anomalies

#anomalies = valeur manquantes, seuil de normalité, étude stat autour de la moyenne

def manquantes(liste):
	pos=[]
	for i in range(0,len(liste)):
		if liste[i]==[]:
			pos.append(i)
		elif liste[i][0]==0 and liste[i+1][0]==0:
			pos.append(i)
			pos.append(i+1)
	return pos

def anomalieStat(liste):
	pos = []
	m = moyenne(liste)
	e = ecartType(liste)
	for i in range(len(liste)):
		if liste[i][0] > m + 2*e:
			pos.append(i)
	return pos


def anomalies(liste):
	pos = manquantes(liste) + anomalieStat(liste)
	if pos == []:
		return "pas d'anomalies détectées"
	else :
		return 'anomalies détectées', pos