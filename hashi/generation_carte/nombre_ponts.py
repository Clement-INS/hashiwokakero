def numero_ile(mat,coord):

    #met le bon numéro sur l'ile

    for i in range(len(coord)): #parcours des iles
        L = coord[i][0] #recupere les coordonnées  
        C = coord[i][1]
        mat[L][C][0] = 0    #intialise la case
        for k in range(1,5):
            mat[L][C][0] = mat[L][C][0] - mat[L][C][k]  #pour chaque direction ajoute le nombre de pont