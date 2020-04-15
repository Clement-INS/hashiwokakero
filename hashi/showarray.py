import pygame

# Affichage de la map dans un écran avec des cases de 40 pixels et des cercles de 10 pixels de rayon
def showtable (mytable):
    # Initialise la librairie graphique pygame
    pygame.init()
    # Initialise la gestion des polices de caractères de pygame
    pygame.font.init()
    # Initialise les tuple de couleurs avec leur valeurs RGB
    background_colour = (255,255,255)
    green = (0,255,0)
    blue = (0,0,255)
    gray =(220,220,220)
    yellow = (255,255,224)
    orange = (255,165,0)
    red = (255,0,0)
    # Initialise le tuple de la taille de la fenetre
    nbCols = len(mytable[0])
    nbLines = len (mytable)
    (width, height) = (40*nbCols, 40*nbLines)
    # Initialise la fenetre
    screen = pygame.display.set_mode((width, height))
    # Donne un titre a la fenetre  
    pygame.display.set_caption('HashiWokakero')
    #Charge la police de caractere arial en taille 10
    font = pygame.font.Font('Arial.ttf', 12)
    # Rempli l'ecran avec la couleur de fond
    screen.fill(background_colour)
    # Tracer les lignes
    for iLine in range(nbLines):
        pygame.draw.line(screen, gray, (20+iLine*40,0), (20+iLine*40,40*nbCols),1)
        if iLine == 0:
            for iCol in range(nbCols):
                pygame.draw.line(screen, gray, (0,20+iCol*40), (40*nbLines,20+iCol*40),1)
                
    for iLine in range(nbLines):
        for iCol in range(nbCols):
            if (mytable[iLine][iCol][0] > 0):
                if mytable[iLine][iCol][1] < 0 :
                    curLine = iLine -1
                    while mytable[curLine][iCol][0] <= 0:
                        curLine = curLine - 1
                    xPoints = iCol*40+20
                    yOrig = iLine*40+20
                    yEnd = curLine*40+20
                    if mytable[iLine][iCol][1]== -1:
                        pygame.draw.line(screen, orange, (xPoints,yOrig),(xPoints,yEnd),2)
                    else:
                        pygame.draw.line(screen, red, (xPoints-5,yOrig),(xPoints-5,yEnd),2)
                        pygame.draw.line(screen, red, (xPoints+5,yOrig),(xPoints+5,yEnd),2)
            if (mytable[iLine][iCol][0] > 0):
                if mytable[iLine][iCol][3] < 0 :
                    curLine = iLine +1
                    while mytable[curLine][iCol][0] <= 0:
                        curLine = curLine + 1
                    xPoints = iCol*40+20
                    yOrig = iLine*40+20
                    yEnd = curLine*40+20
                    if mytable[iLine][iCol][3]== -1:
                        pygame.draw.line(screen, orange, (xPoints,yOrig),(xPoints,yEnd),2)
                    else:
                        pygame.draw.line(screen, red, (xPoints-5,yOrig),(xPoints-5,yEnd),2)
                        pygame.draw.line(screen, red, (xPoints+5,yOrig),(xPoints+5,yEnd),2)
            if (mytable[iLine][iCol][0] > 0):
                if mytable[iLine][iCol][2] < 0 :
                    curCol = iCol +1
                    while mytable[iLine][curCol][0] <= 0:
                        curCol = curCol + 1
                    yPoints = iLine*40+20
                    xOrig = iCol*40+20
                    xEnd = curCol*40+20
                    if mytable[iLine][iCol][2]== -1:
                        pygame.draw.line(screen, orange, (xOrig,yPoints),(xEnd,yPoints),2)
                    else:
                        pygame.draw.line(screen, red, (xOrig,yPoints+5),(xEnd,yPoints+5),2)
                        pygame.draw.line(screen, red, (xOrig,yPoints-5),(xEnd,yPoints-5),2)
            if (mytable[iLine][iCol][0] > 0):
                if mytable[iLine][iCol][4] < 0 :
                    curCol = iCol -1
                    while mytable[iLine][curCol][0] <= 0:
                        curCol = curCol - 1
                    yPoints = iLine*40+20
                    xOrig = iCol*40+20
                    xEnd = curCol*40+20
                    if mytable[iLine][iCol][4]== -1:
                        pygame.draw.line(screen, orange, (xOrig,yPoints),(xEnd,yPoints),2)
                    else:
                        pygame.draw.line(screen, red, (xOrig,yPoints+5),(xEnd,yPoints+5),2)
                        pygame.draw.line(screen, red, (xOrig,yPoints-5),(xEnd,yPoints-5),2)
    for iLine in range(nbLines):
        for iCol in range(nbCols):
            y = iLine*40+20
            x = iCol*40+20
            # Si valeur du table > 0 alors trace point (cercle + valeur dans le cercle)
            if (mytable[iLine][iCol][0] > 0):
                # Met la valeur de la cellule du tableau dans le texte
                text = font.render(str(mytable[iLine][iCol][0]), True, blue)
                textRect = text.get_rect()
                # Positionne le texte sur la grille
                textRect.center = (x,y)
                # Affiche un disque jaune pour le fond du point
                pygame.draw.circle(screen, yellow, (x, y), 12, 0)
                # Affiche le contour du point en bleu
                pygame.draw.circle(screen, blue, (x, y), 12, 1)
                # Affiche le texte
                screen.blit(text, textRect)
            #if (mytable[iLine][iCol][0] < 0):
            #    if (mytable[iLine][iCol][0] == -1):
            #        pygame.draw.rect(screen, orange, (15+j*40,15+40*i,10,10), 0)
            #    else:
            #        pygame.draw.rect(screen, red, (15+j*40,15+40*i,10,10), 0)
            
    # Affiche l'ecran
    pygame.display.flip()
    running = True
    # Attend que l'in ferme la fenetre pour sortir
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False