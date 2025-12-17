import pygame
import time
from distances import calc_sit
def controll_keys(labyrinthe, robber, police, version, situation):
    keys={"z": pygame.K_z, "q": pygame.K_q, "s": pygame.K_s, "d": pygame.K_d, 
    "e": pygame.K_e, "f": pygame.K_f, 
    "up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT}
    key_p = pygame.key.get_pressed()

    rx,ry = robber
    px,py = police


    hauteur, longueur = len(labyrinthe), len(labyrinthe[0])
    v = version
    if True in key_p:
        if key_p[keys["e"]]: v = 2
        elif key_p[keys["f"]]: v = 1

        # robber
        if key_p[keys["z"]] and ry>0 and not labyrinthe[ry-1][rx][1]: ry-=1
        elif key_p[keys["q"]] and rx>0 and not labyrinthe[ry][rx-1][0]: rx-=1
        elif key_p[keys["s"]] and ry<hauteur-1 and not labyrinthe[ry][rx][1]: ry+=1
        elif key_p[keys["d"]] and rx<longueur-1 and not labyrinthe[ry][rx][0]: rx+=1

        # police
        if key_p[keys["up"]] and py>0 and not labyrinthe[py-1][px][1]: py-=1
        elif key_p[keys["left"]] and px>0 and not labyrinthe[py][px-1][0]: px-=1
        elif key_p[keys["down"]] and py<hauteur-1 and not labyrinthe[py][px][1]: py+=1
        elif key_p[keys["right"]] and px<longueur-1 and not labyrinthe[py][px][0]: px+=1

        situation = calc_sit(labyrinthe, (rx,ry), (px,py))

    return (rx,ry), (px,py), True in key_p, v, situation