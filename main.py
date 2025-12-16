import pygame
import create_lab as cl
import drawlab_v1 as l1
import drawlab_v2 as l2
from controll import controll_keys
from random import random, shuffle

def run(screen, labyrinthe):
    version = 2
    rob, pol = (0,0), (len(labyrinthe[0])-1, len(labyrinthe)-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        rob, pol, pause, version = controll_keys(labyrinthe, rob, pol, version) 
        if version == 2: l2.drawwhatever(screen, labyrinthe, rob, pol, pause)
        else: l1.drawwhatever(screen, labyrinthe, rob, pol, pause)
        pygame.display.update()
    pygame.quit()

def init():
    print("Veuillez choisir les paramètres du labyrinthe")
    pardef = input("Paramètre par défaut? (o/n)\n") == "o"
    hauteur = 14 if pardef else int(input("Hauteur ?\n"))
    longueur = 20 if pardef else int(input("Longueur ?\n"))
    probamur = 0.9 if pardef else float(input("Pourcentage mur ? (entre 0.0 et 1.0)\n"))
    parfait = True if pardef else input("Labyrinthe parfait (o/n)\n") == "o"
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # EST: 0, SUD: 1
    labyrinthe = []
    for y in range(hauteur):
        labyrinthe.append([])
        for x in range(longueur):
            labyrinthe[y].append([])
            for i in range(2):
                labyrinthe[y][x].append((y==hauteur-1 and i==1) or (x==longueur-1 and i==0) or (random()<probamur))
    
    if parfait: labyrinthe = cl.rendre_connexe(labyrinthe)
    run(screen, labyrinthe)

init()