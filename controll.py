import pygame
import time
import reseau_neurone
from random import randint
from distances import calc_sit

def controll_keys(tour, labyrinthe, robber, policemen, version, situation, rand, ai, model):
    keys={"z": pygame.K_z, "q": pygame.K_q, "s": pygame.K_s, "d": pygame.K_d, 
    "e": pygame.K_e, "f": pygame.K_f,  "space": pygame.K_SPACE,
    "up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT}
    
    key_p = pygame.key.get_pressed()

    r_move = [False] * 5

    if ai:
        # creer donnees_entrees
        with torch.no_grad():
        predi = (model(donnees_entrees))
        lmv = [] # liste move prio
        while len(lmv) < 5:
            max = (-1) * sys.maxint - 1
            max_id = -1
            for x in range(5):
                if x not in lmv:
                    if predi[x] > max: 
                        max = predi[x]
                        max_id = x
            lmv.append(max_id)
        
    else if rand:
        lmv = []
        while len(lmv) < 5:
            i = randint(0,4)
            if not i in lmv: lmv.append(i)

    x,y = 0,0
    if tour == 0: x,y = robber
    else: x,y = policemen[tour - 1]

    hauteur, longueur = len(labyrinthe), len(labyrinthe[0])
    v = version
    played = False
    once = -1
    while ((ai or rand) and not played) && once != -1:
        once+=1

        r_move[lmv[once]] = True
        if once >= 1: r_move[lmv[once -1]] = False
        
        if key_p[keys["e"]]: v = 2
        elif key_p[keys["f"]]: v = 1

        if (key_p[keys["z"]] or key_p[keys["up"]] or r_move[0]) and y>0 and not labyrinthe[y-1][x][1]:
            y-=1
            played = True
        elif (key_p[keys["q"]] or key_p[keys["left"]] or r_move[1]) and x>0 and not labyrinthe[y][x-1][0]: 
            x-=1
            played = True
        elif (key_p[keys["s"]] or key_p[keys["down"]] or r_move[2]) and y<hauteur-1 and not labyrinthe[y][x][1]: 
            y+=1
            played = True
        elif (key_p[keys["d"]] or key_p[keys["right"]] or r_move[3]) and x<longueur-1 and not labyrinthe[y][x][0]: 
            x+=1
            played = True
        elif key_p[keys["space"]] or r_move[4]: played = True

        if tour == 0: robber = (x,y)
        else: policemen[tour-1] = (x,y)
        situation = calc_sit(labyrinthe, robber, policemen)

    if played: tour = (tour+1) % (len(policemen)+1)
    return tour, robber, policemen, True in key_p, v, situation
