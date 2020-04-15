import random

#pour chaque pont, le transforme en double pont avec une probabilité égale à b

def ajout_ponts(mat,B,coord): 
    for k in range(len(coord)): #parcours l'ensemble des iles
        L = coord[k][0] #récupère les coordonnées
        C = coord[k][1]
        if mat[L][C][1] == -1:  #vérifie la présence d'un pont en haut
            val_pont = random.choices([-2,-1],[B,1-B])[0] #test si on double le pont
            mat[L][C][1] = val_pont #indique la valeur du pont
            #print("pont double ?",mat[L][C][1])
            L = L - 1
            while mat[L][C][0] != 1:    #remet les valeurs du pont à jour
                mat[L][C][0] = val_pont
                #print("val du pont",mat[L][C][0])
                L = L - 1
            mat[L][C][3] = val_pont
        L = coord[k][0] #réinitialise L
        if mat[L][C][2] == -1:  #même process pour les ponts à droite
            val_pont = random.choices([-2,-1],[B,1-B])[0]
            mat[L][C][2] = val_pont
            C = C + 1
            while mat[L][C][0] != 1:
                mat[L][C][0] = val_pont
                C = C + 1
            mat[L][C][4] = val_pont
    return mat

