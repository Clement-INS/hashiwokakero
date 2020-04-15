import random, numpy

#etape 1 de la creation de grille en suivant la methode du fichier https://arxiv.org/pdf/1905.00973.pdf
#consiste à placer une ile au hasard puis la relier à une autre ile placée aléatoirement dans une des 4 directions possible et à une distance aléatoire
#ce processus ce fait n-1 fois de manière récursive
#je représente dans la carte dans un tableau en 3 dimensions C(colonne ou y), L(ligne ou x) et z, la matrice z=0
#représente la carte, les 1 sont des iles, les -1 des ponts et les 0 rien.
#les matrices z=1,2,3,4 représente la présence d'un pont dans une certaine direction, par exemple un -1 aux coordonnées (1,1,1) veut dire qu'il y a un pont en haut de l'ile placéee en (1,1,0)
#un -1 en (3,5,4) veut qu'il y a un pont à gauche de l'ile en (3,5,0)

def crea_grille (Size,n):
    magrille = numpy.zeros((Size,Size,5),numpy.int)  #création du tableau en le remplissant de 0
    C = random.randint(0,Size-1)    #choix de coordonées aléatoire pour la première ile
    L = random.randint(0,Size-1)
    #print(magrille)
    magrille[L][C][0] = 1    #placement de la première ile
    coord = [[L,C]] #liste des coordonnées des iles
    #print(magrille)
    i=0
    rate = False
    while i < (n-1) and rate == False:  #boucle pour la création des iles restantes soit n-1, rate permet de sortir d'une boucle inf
        i = i+1
        L_old = L
        C_old = C   #on retient la position de la derniere ile créée
        #print ("C1 =",C,"L1 =",L)
        rate = True
        nbTry = 0
        while rate == True and nbTry < 30: #boucle pour la création de la prochaine ile
            nbTry = nbTry +1
            dir = random.randint(1,4)   #determine la direction de la prochaine ile(1=nord, 2=est, 3=sud, 4=ouest)
            #print ("dir =",dir)
            if dir == 1 and L_old > 0:
                L = random.randint(0,L_old-1) #détermine la position de la prochaine ile
                C = C_old
                rate = False
                for k in range(L,L_old): #on verifie qu'il n'y est pas d'ile ou de pont entre la nouvelle ile et l'ancienne, si oui on recommence la boucle
                    if magrille[k][C][0] == 1 or magrille[k][C][0] == -1:
                        rate = True
                if rate == False:
                    magrille[L][C][0] = 1   #placement de la nouvelle ile
                    magrille[L][C][3] = -1  #indique la présence d'un pont en bas de l'ile en (L,C)
                    magrille[L_old][C_old][1] = -1  #indique la présence d'un pont en bas de l'ile en (L_old,C_old)
                    coord = coord+[[L,C]]   #on rajoute les coordonnées de la nouvelle ile dans la liste
                    for k in range(L+1,L_old):
                        magrille[k][C][0] = -1
            #on refait le meme process pour dir = 2/3/4
            elif dir == 2 and C_old < Size-1:
                L = L_old
                C = random.randint(C_old+1,Size-1)
                rate = False
                for k in range(C_old+1,C+1):
                    if magrille[L][k][0] == 1 or magrille[L][k][0] == -1:
                        rate = True
                if rate == False:
                    magrille[L][C][0] = 1
                    magrille[L][C][4] = -1
                    magrille[L_old][C_old][2] = -1
                    coord = coord+[[L,C]]
                    for k in range(C_old+1,C):
                        magrille[L][k][0] = -1
            elif dir == 3 and L_old < Size-1:
                L = random.randint(L_old+1,Size-1)
                C = C_old
                rate = False
                for k in range(L_old+1,L+1):
                    if magrille[k][C][0] == 1 or magrille[k][C][0] == -1:
                        rate = True
                if rate == False:
                    magrille[L][C][0] = 1
                    magrille[L][C][1] = -1
                    magrille[L_old][C_old][3] = -1
                    coord = coord+[[L,C]]
                    for k in range(L_old+1,L):
                        magrille[k][C][0] = -1
            elif dir == 4 and C_old > 0:
                L = L_old
                C = random.randint(0,C_old-1)
                rate = False
                for k in range(C,C_old):
                    if magrille[L][k][0] == 1 or magrille[L][k][0] == -1:
                        rate = True
                if rate == False:
                    magrille[L][C][0] = 1
                    magrille[L][C][2] = -1
                    magrille[L_old][C_old][4] = -1
                    coord = coord+[[L,C]]
                    for k in range(C+1,C_old):
                        magrille[L][k][0] = -1
            #print ("C =",C,L =",L)
    return magrille, coord