import random

#créer des ponts entre deux iles reliables avec une probabilité a

def crea_new_pont(mat,a,coord):
    for k in range(len(coord)): #parcours l'ensemble des iles
            L_old = coord[k][0] #recupere les coordonnées de l'ile
            C_old = coord[k][1]
            if C_old > 0 and mat[L_old][C_old][4] == 0: #test pour la création d'un pont à gauche, on vérifie qu'il n'y en ait pas déjà
                C = C_old-1
                creation = (random.random() < a)    #boolean pour savoir si on créer ou pas avec la proba a
                place_pont = True
                while place_pont and mat[L_old][C][0] != 1: #verification de la possibilité de mettre un pont
                    if C == 0 or mat[L_old][C][0] == -1:  
                        place_pont = False
                    else:
                        C = C-1
                if creation and place_pont: #si tout est bon, on créer le nouveau pont
                    mat[L_old][C][2] = -1   #indique la présence du nouveau pont à droite
                    mat[L_old][C_old][4] = -1 #indique la présence du nouveau pont à gauche
                    for k in range(C+1,C_old):  #création du pont
                        mat[L_old][k][0] = -1
            if L_old > 0 and mat[L_old][C_old][1] == 0:   #même process pour un pont en haut
                L = L_old-1
                creation = (random.random() < a)
                place_pont = True
                while place_pont and mat[L][C_old][0] != 1:
                    if L == 0 or mat[L][C_old][0] == -1:
                        place_pont = False
                    else:
                        L = L-1
                if creation and place_pont:
                    mat[L][C_old][3] = -1
                    mat[L_old][C_old][1] = -1
                    for k in range(L+1,L_old):
                        mat[k][C_old][0] = -1
    return mat