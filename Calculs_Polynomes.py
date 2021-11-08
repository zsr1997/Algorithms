#DM2

import numpy as np

#Les tableaux pour tester
P1=[1,1,1,5]
print("P1:",P1)
Q1=[2,3,2]
print("Q1:",Q1)
P2=[0,1,2,3]
print("P2:",P2)
Q2=[1,0,0,3]
print("Q2:",Q2)
P3=[-1,-3,0,1,2,5]
print("P3",P3)
Q3=[-2,-5,1,0,7,10,20,50]
print("Q3:",Q3)
P4=[1,2,0,0]
print("P4:",P4)
Q4=[1,2]
print("Q4",Q4)

def sommePoly(P,Q):
    C=[0]*max(len(P),len(Q))                   #Matrice nulle,sa taille est la taille max de P et Q
    if len(P)>len(Q):                          #Au cas si taille de P > taille de Q
        n=len(P)-len(Q)                        #Ecart de la taille P et Q
        Q=Q+n*[0]                              #Remplir Q avec des 0 pour avoir la même taille de P
        for i in range(0,len(Q)):              #Parcourir le tableau de 0 à taille de Q -1
            C[i]=P[i]+Q[i]                     # Somme des élelments de P et de Q
    elif len(P)<len(Q):
        n2=len(Q)-len(P)
        P=P+n2*[0]
        for j in range(len(Q)):
            C[j]=P[j]+Q[j]
    else:
        for k in range(len(P)):
            C[k]=P[k]+Q[k]
    return C
L=sommePoly(P1,Q1)
print("la somme de P1 et Q1 est:",L)
L1=sommePoly(P2,Q2)
print("la somme de P2 et Q2 est:",L1)
L3=sommePoly(P3,Q3)
print("la somme de P3 et Q3 est:",L3)
def produitSca(P,a):
    C=[0]*len(P)
    for i in range(len(P)):
        C[i]=P[i]*a                             #Tous les élements de P multiplient a
    return C
L4=produitSca(P1,2)
print("le produit de P1 et scalaire 2 est:",L4)
L5=produitSca(P3,5)
print("le produit de P3 et scalaire 5 est:",L5)

def produitPoly(P, Q) :
  C=[0]*(len(Q)+len(P))
  for i in range(0,len(P)):
    for j in range(0,len(Q)):
      C[i+j]=C[i+j]+(P[i]*Q[j])          #Une liste contient les sommes de tous les élements de P et Q qui ont le même dégre
  return C
A=[1,0,2,3]
B=[0,2,4]
C=produitPoly(A,B)
print("le produit de polynome ",A,"et polynome",B,"est:",C)
C1=produitPoly(P1,Q1)
print("le produit de polynôme ",P1,"et polynome",Q1,"est:",C1)
def deg(P):
    i=0
    while i < len(P):                       #Quand i< la taille de P
        if(P[i] != 0):                      # Si la case i de P n'est pas égale à 0
           a = i
        i += 1
    return a

def egale(P,Q):
    if len(P)<len(Q):#Au cas si taille de P > taille de Q
        n1=len(Q)-len(P)#Ecart de la taille P et Q
        P=P+n1*[0]#Remplir P avec des 0 pour avoir la même taille de Q
        for i in range(len(P)):#Parcourir le tableau de 0 à taille de P -1
            if P[i] != Q[i]:# si le chiffre de la case i de P n'est pas égale à le chiffre de la case i de Q
                return False
        return True
    elif len(P)>len(Q):
        n2=len(P)-len(Q)
        Q=Q+n2*[0]
        for j in range(len(Q)):
            if Q[j] != P[j]:
                return False
        return True
    else:
        for k in range(len(P)):
            if Q[k] != P[k]:
                return False
        return True
L6=egale(P1,Q1)
print("Est-ce que P1=Q1?:",L6)
L7=egale(P4,Q4)
print("Est-ce que P4=Q4?:",L7)

def divisionrestePoly(P,Q):
    T=P
    if deg(T)>=deg(Q):             #si deg de P >= deg de Q , on a aussi len(P)>= len(Q)
        n=len(T)-len(Q)             #ecart de la taille P et Q
        Q=[0]*n+Q                  #remplir Q avec des 0 pour avoir la même taille de Q
        quotient=[]                #Créer un tableau vide pour quotient
        diviseur=float(Q[-1])      # Diviseur est le coefficient de la plus grand dégre de Q
    else:
        return 0,0  # Affiche 0 si P ne peut pas être divisé par Q
    for i in range(n+1):
        m=T[-1]/diviseur            # un mutille m est le coefficient de la plus grand dégre de P divise le diviseur qu'on vient de définir
        quotient=[m]+quotient       # Mettre les valeurs de m de gauche à droite dans le tableau quotient
        if m!= 0: # si la multiple n'est pas égale à 0
            for u in range(len(T)):
                T[u]=T[u]-m*Q[u]  # on soustraire le P et m*Q
        T.pop() # on supprime les démarches intermédiaire et on ne garde que le dernier résultat qui ne peut pas être divisé par Q qui est donc le reste
        Q.pop(0)# Enlèver la première case de Q(deg de Q moins 1 ) chaque fois
    return quotient,T

print("le quotient et le reste de la division du coefficient de polynome",[-4,3,0,2],"par le coefficient de polynome",[1,1],"est:",divisionrestePoly([-4,3,0,2],[1,1]))

P=[-4,3,0,2]
print("P:",P)
Q=[1,1]
print("Q:",Q)
Z1=divisionrestePoly(P,Q)
print("exemple1:Le quotient et la reste de la division de polynome P par Q est",Z1)
Z2=divisionrestePoly(P1,Q1)
print("exemple2:Le quotient et la reste de la division de polynome P1 par Q1 est ",Z2)
Z3=divisionrestePoly(P4,Q4)
print("exemple3:Le quotient et la reste de la division de polynome P4,par Q4 est",Z3)
Z4=divisionrestePoly(P3,Q3)
print("exemple4:Le quotient et la reste de la division de polynome P3, par Q3 est. Dans ce cas la P ne peut pas petre divisé par Q ,le résultat affiche 0,0 d'après mon algorithme",Z4)

#Or je n'ai pas fait comment votre énonce(j'ai mélangé l'algo divisionPoly et restePoly ensemble),Ainsi, le Polynôme P est changé après mon algo divisionrestePoly donc la fonction divisionTest ne se marche pas dans mon algo...

