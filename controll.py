import pygame
import time
import torch
import numpy
import reseau_neurone
from random import randint
from distances import calc_sit

def creer_input_data(lab, ra, v, pol):
    # Pour 2 policiers uniquement
    converted = []
    n,m = len(lab), len(lab[0])
    p1 = pol[0]
    p2 = pol[1]
    for i in range(n):
        for j in range(m):
            converted.append((0 if lab[i][j][0] or j == m-1 else 1) 
                            + ((0 if lab[i][j][1] or u == n-1 else 2))
                            + ((0 if (i,j) == v else 4))
                            + ((0 if (i,j) == p1 else 8))
                            + ((0 if (i,j) == p2 else 16))
                            + ((0 if ra[i][j] else 32)))
    return converted

def controll_keys(tour, lab, v, pol, version, ra, rand, ai, model):
    keys={"z": pygame.K_z, "q": pygame.K_q, "s": pygame.K_s, "d": pygame.K_d, 
    "e": pygame.K_e, "f": pygame.K_f,  "space": pygame.K_SPACE,
    "up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT}
    
    key_p = pygame.key.get_pressed()
    r_move = [False] * 5

    current_data = None
    if ai:
        current_data = creer_input_data(lab, ra, v, pol)
        current_data.append(tour)
        # IL RESTE PEUT-ËTRE À CONVERTIR LA LISTE EN TORSEUR
        temp = Numpy.array(current_data)
        temp = torch.IntTensor(temp)
        with torch.no_grad():
            predi = (model(temp))
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
    elif rand:
        lmv = []
        while len(lmv) < 5:
            i = randint(0,4)
            if not i in lmv: lmv.append(i)

    x,y = 0,0
    if tour == 0: x,y = v
    else: x,y = pol[tour - 1]

    hauteur, longueur = len(lab), len(lab[0])
    v = version
    played = False
    once = -1
    
    coup_choisi = None
    while ((ai or rand) and not played) and once != -1:
        once+=1

        r_move[lmv[once]] = True
        if once >= 1: r_move[lmv[once -1]] = False
        
        if key_p[keys["e"]]: v = 2
        elif key_p[keys["f"]]: v = 1

        if (key_p[keys["z"]] or key_p[keys["up"]] or r_move[0]) and y>0 and not lab[y-1][x][1]:
            y-=1
            played = True
        elif (key_p[keys["q"]] or key_p[keys["left"]] or r_move[1]) and x>0 and not lab[y][x-1][0]: 
            x-=1
            played = True
        elif (key_p[keys["s"]] or key_p[keys["down"]] or r_move[2]) and y<hauteur-1 and not lab[y][x][1]: 
            y+=1
            played = True
        elif (key_p[keys["d"]] or key_p[keys["right"]] or r_move[3]) and x<longueur-1 and not lab[y][x][0]: 
            x+=1
            played = True
        elif key_p[keys["space"]] or r_move[4]: played = True

        if tour == 0: v = (x,y)
        else: pol[tour-1] = (x,y)
        ra = calc_sit(lab, v, pol)

        if played and ai:
            coup_choisi = r_move[lmv[once]]

    if played: tour = (tour+1) % (len(pol)+1)
    return tour, v, pol, True in key_p, v, ra, (current_data, coup_choisi)
