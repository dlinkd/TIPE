import pygame
import create_lab as cl
import drawlab_v1 as l1
from controll import controll_keys
from random import random, shuffle

def drawgrille(screen, labyrinthe, offset, situation):
    """
    Dessine la grille
    - screen: Surface pygame où est dessiné la grille
    - labyrinthe: le labyrinthe sous forme de matrice
    - offset: entier correspondant au décalage graphique par rapport à la gauche et au haut de l'écran
    - situation: matrice de booléen indiquant à chaque case si le voleur est plus proche
    """

    hauteur, longueur = len(labyrinthe), len(labyrinthe[0])
    windowL = 1600
    windowH = 1000

    radiusR = 20
    arreteL = 50
    arreteH = 50

    # rond de l'origine
    pygame.draw.circle(screen, radius=0.5*radiusR, width=1, center=(offset - 0.5*radiusR, offset - 0.5*radiusR), color="black")            

    for y in range(hauteur):
        for x in range(longueur):
            c1 = "red" if situation[y][x] else "black"
            c2 = "red" if situation[y+1][x] else "black"
            c3 = "red" if situation[y][x+1] else "black"

            if(not labyrinthe[y][x][1]): # lignes verticales
                pygame.draw.line(screen, start_pos= (offset + (arreteL+radiusR)*x, offset + (arreteH+radiusR)*y), end_pos= (offset + (arreteL+radiusR)*x, offset + (arreteH+radiusR)*(y+1) - radiusR), color=c2, width=5)
                pygame.draw.circle(screen, radius=0.5*radiusR, width=1, center=(offset + (arreteL+radiusR)*x - 0.5*radiusR, offset + (arreteH+radiusR)*y - 0.5*radiusR), color=c1)            
                if y<hauteur-1: pygame.draw.circle(screen, radius=0.5*radiusR, width=1, center=(offset + (arreteL+radiusR)*x - 0.5*radiusR, offset + (arreteH+radiusR)*(y+1) - 0.5*radiusR), color=c2)            
            
            if(not labyrinthe[y][x][0]): # lignes horizontales
                pygame.draw.line(screen, start_pos= (offset + (arreteL+radiusR)*x, offset + (arreteH+radiusR)*y - radiusR), end_pos= (offset + (arreteL+radiusR)*(x+1) - radiusR, offset + (arreteH+radiusR)*y - radiusR), color=c3, width=5)
                pygame.draw.circle(screen, radius=0.5*radiusR, width=1, center=(offset + (arreteL+radiusR)*x - 0.5*radiusR, offset + (arreteH+radiusR)*y - 0.5*radiusR), color=c1)            
                if x<longueur-1: pygame.draw.circle(screen, radius=0.5*radiusR, width=1, center=(offset + (arreteL+radiusR)*(x+1) - 0.5*radiusR, offset + (arreteH+radiusR)*y - 0.5*radiusR), color=c3)            

def drawpeople(screen, labyrinthe, x,y, offset, couleur):
    hauteur, longueur = len(labyrinthe), len(labyrinthe[0])
    windowL = 1600
    windowH = 1000
    radiusR = 20
    arreteL = 50
    arreteH = 50
    pygame.draw.circle(screen, color=couleur, radius=0.5*radiusR, center=(offset + (arreteL+radiusR)*(x) - 0.5*radiusR, offset + (arreteH+radiusR)*(y) - 0.5*radiusR))

def drawwhatever (screen, labyrinthe, rob, pol, situation):
    offset = 100
    screen.fill((200,200,200))

    drawgrille(screen, labyrinthe, offset, situation)
    drawpeople(screen, labyrinthe, rob[0], rob[1], offset, "black") # robber
    drawpeople(screen, labyrinthe, pol[0], pol[1], offset, "blue") # police
    return rob, pol

