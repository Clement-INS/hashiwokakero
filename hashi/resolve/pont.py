#fonction permettant de créer un pont entre deux points donnés,
#enlève également 1 aux deux iles liées pour pouvoir les considérer comme des plus petites iles par la suite.

def crea_pont(point_A, point_B, grille):
    Ligne_A = point_A[0]
    Colonne_A = point_A[1]
    Ligne_B = point_B[0]
    Colonne_B = point_B[1]
    #construction pont de bas en haut
    if Ligne_A - Ligne_B > 0:
        for i in range(Ligne_B + 1, Ligne_A):
            grille[i][Colonne_A][0] = grille[i][Colonne_A][0] - 1
        grille[Ligne_A][Colonne_A][0] = grille[Ligne_A][Colonne_A][0] - 1
        grille[Ligne_A][Colonne_A][1] = grille[Ligne_A][Colonne_A][1] - 1
        grille[Ligne_B][Colonne_B][0] = grille[Ligne_B][Colonne_B][0] - 1
        grille[Ligne_B][Colonne_B][3] = grille[Ligne_B][Colonne_B][3] - 1
    #construction pont de haut en bas
    if Ligne_A - Ligne_B < 0:
        for i in range(Ligne_A + 1, Ligne_B):
            grille[i][Colonne_A][0] = grille[i][Colonne_A][0] - 1
        grille[Ligne_A][Colonne_A][0] = grille[Ligne_A][Colonne_A][0] - 1
        grille[Ligne_A][Colonne_A][3] = grille[Ligne_A][Colonne_A][3] - 1
        grille[Ligne_B][Colonne_B][0] = grille[Ligne_B][Colonne_B][0] - 1
        grille[Ligne_B][Colonne_B][1] = grille[Ligne_B][Colonne_B][1] - 1
    #construction pont vers la gauche
    if Colonne_A - Colonne_B > 0:
        for i in range(Colonne_B + 1, Colonne_A):
            grille[Ligne_A][i][0] = grille[Ligne_A][i][0] - 1
        grille[Ligne_A][Colonne_A][0] = grille[Ligne_A][Colonne_A][0] - 1
        grille[Ligne_A][Colonne_A][4] = grille[Ligne_A][Colonne_A][4] - 1
        grille[Ligne_B][Colonne_B][0] = grille[Ligne_B][Colonne_B][0] - 1
        grille[Ligne_B][Colonne_B][2] = grille[Ligne_B][Colonne_B][2] - 1
    #construction pont vers la droite
    if Colonne_A - Colonne_B < 0:
        for i in range(Colonne_A + 1, Colonne_B):
            grille[Ligne_A][i][0] = grille[Ligne_A][i][0] - 1
        grille[Ligne_A][Colonne_A][0] = grille[Ligne_A][Colonne_A][0] - 1
        grille[Ligne_A][Colonne_A][2] = grille[Ligne_A][Colonne_A][2] - 1
        grille[Ligne_B][Colonne_B][0] = grille[Ligne_B][Colonne_B][0] - 1
        grille[Ligne_B][Colonne_B][4] = grille[Ligne_B][Colonne_B][4] - 1

################################################################################
#fonction qui cherche la présence des voisins d'un point
#renvoie le nombre de voisins puis la position de tous les voisins avec leur numéro sur l'ile, si le voisin n'existe pas, retourne [0,0,0]

def voisins(Point, grille):
    L = Point[0]
    C = Point[1]
    Voisin_Haut = [0,0,0]
    #les deux premiers numéros correspondent aux coordonnées, le troisième correspond au numéro sur l'ile
    Voisin_Droit = [0,0,0]
    Voisin_Bas = [0,0,0]
    Voisin_Gauche = [0,0,0]
    nb_voisin = 0
    L_aux = L
    C_aux = C
    #cherche un voisin en haut
    if grille[L][C][1] > -2:
        possible = True
        trouve = False
        while possible and not trouve:
            L_aux = L_aux - 1
            if L_aux < 0:
                possible = False
            else:
                if grille[L_aux][C_aux][0] < 0:
                    possible = False
                elif grille[L_aux][C_aux][0] == 0:
                    for i in range(1,5):
                        if grille[L_aux][C_aux][i] != 0:
                            possible = False
                else:
                    trouve = True
        #si trouvé ajoute 1 au nombre de voisins et rentre les coordonnées
        if possible:
            nb_voisin = nb_voisin + 1
            Voisin_Haut = [L_aux, C_aux, grille[L_aux][C_aux][0]]
    L_aux = L
    C_aux = C
    #cherche un voisin à droite
    if grille[L][C][2] > -2:
        possible = True
        trouve = False
        while possible and not trouve: 
            C_aux = C_aux + 1
            if C_aux == len(grille[0]):
                possible = False
            else:
                if grille[L_aux][C_aux][0] < 0:
                    possible = False
                elif grille[L_aux][C_aux][0] == 0:
                    for i in range(1,5):
                        if grille[L_aux][C_aux][i] != 0:
                            possible = False
                else:
                    trouve = True
        #si trouvé ajoute 1 au nombre de voisins et rentre les coordonnées
        if possible:
            nb_voisin = nb_voisin + 1
            Voisin_Droit = [L_aux, C_aux, grille[L_aux][C_aux][0]]
    L_aux = L
    C_aux = C
    #cherche un voisin en bas
    if grille[L][C][3] > -2:
        possible = True
        trouve = False
        while possible and not trouve: 
            L_aux = L_aux + 1
            if L_aux == len(grille):
                possible = False
            else:
                if grille[L_aux][C_aux][0] < 0:
                    possible = False
                elif grille[L_aux][C_aux][0] == 0:
                    for i in range(1,5):
                        if grille[L_aux][C_aux][i] != 0:
                            possible = False
                else:
                    trouve = True
        #si trouvé ajoute 1 au nombre de voisins et rentre les coordonnées
        if possible:
            nb_voisin = nb_voisin + 1
            Voisin_Bas = [L_aux, C_aux, grille[L_aux][C_aux][0]]
    L_aux = L
    C_aux = C
    #cherche un voisin à gauche
    if grille[L][C][4] > -2:
        possible = True
        trouve = False
        while possible and not trouve: 
            C_aux = C_aux - 1
            if C_aux < 0:
                possible = False
            else:
                if grille[L_aux][C_aux][0] < 0:
                    possible = False
                elif grille[L_aux][C_aux][0] == 0:
                    for i in range(1,5):
                        if grille[L_aux][C_aux][i] != 0:
                            possible = False
                else:
                    trouve = True
        #si trouvé ajoute 1 au nombre de voisins et rentre les coordonnées
        if possible:
            nb_voisin = nb_voisin + 1
            Voisin_Gauche = [L_aux, C_aux, grille[L_aux][C_aux][0]]
        return nb_voisin, Voisin_Haut, Voisin_Droit, Voisin_Bas, Voisin_Gauche
    
###############################################################################################
#Creer un pont avec les deux voisins si l'ile en argument est un 3 avec deux voisins
            
def cas_3_deux_voisins(point, grille):
    L = point[0]
    C = point[1]
    nb_voisins, voisin_haut, voisin_droit, voisin_bas, voisin_gauche = voisins(point, grille)
    if grille[L][C][0] == 3 and nb_voisins == 2:
        if voisin_haut[2] != 0:
            crea_pont(point, voisin_haut, grille)
        if voisin_droit[2] != 0:
            crea_pont(point, voisin_droit, grille)
        if voisin_bas[2] != 0:
            crea_pont(point, voisin_bas, grille)
        if voisin_gauche[2] != 0:
            crea_pont(point, voisin_gauche, grille)

#########################################################################################
#Creer un double pont avec les deux voisins si l'ile est un quatre est a que deux voisins

def cas_4_deux_voisins(point,grille):
    L = point[0]
    C = point[1]
    nb_voisins, voisin_haut, voisin_droit, voisin_bas, voisin_gauche = voisins(point, grille)
    if grille[L][C][0] == 4 and nb_voisins == 2:
        if voisin_haut[2] != 0:
            crea_pont(point, voisin_haut, grille)
            crea_pont(point, voisin_haut, grille)
        if voisin_droit[2] != 0:
            crea_pont(point, voisin_droit, grille)
            crea_pont(point, voisin_droit, grille)
        if voisin_bas[2] != 0:
            crea_pont(point, voisin_bas, grille)
            crea_pont(point, voisin_bas, grille)
        if voisin_gauche[2] != 0:
            crea_pont(point, voisin_gauche, grille)
            crea_pont(point, voisin_gauche, grille)

#########################################################################################
#Creer un double pont avec les deux voisins si l'ile est un quatre est a que deux voisins