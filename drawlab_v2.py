import pygame
import time
import create_lab as cl
import drawlab_v1 as l1
from controll import controll_keys
from random import random, shuffle

def drawgrille(screen, labyrinthe, offset):
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
            if(not labyrinthe[y][x][1]): # lignes verticales
                pygame.draw.line(screen, start_pos= (offset + (arreteL+radiusR)*x, offset + (arreteH+radiusR)*y), end_pos= (offset + (arreteL+radiusR)*x, offset + (arreteH+radiusR)*(y+1) - radiusR), color="black", width=5)
                if y<hauteur-1: pygame.draw.circle(screen, radius=0.5*radiusR, width=1, center=(offset + (arreteL+radiusR)*x - 0.5*radiusR, offset + (arreteH+radiusR)*y - 0.5*radiusR), color="black")            
                if y<hauteur-1: pygame.draw.circle(screen, radius=0.5*radiusR, width=1, center=(offset + (arreteL+radiusR)*x - 0.5*radiusR, offset + (arreteH+radiusR)*(y+1) - 0.5*radiusR), color="black")            
            
            if(not labyrinthe[y][x][0]): # lignes horizontales
                pygame.draw.line(screen, start_pos= (offset + (arreteL+radiusR)*x, offset + (arreteH+radiusR)*y - radiusR), end_pos= (offset + (arreteL+radiusR)*(x+1) - radiusR, offset + (arreteH+radiusR)*y - radiusR), color="black", width=5)
                if x<longueur-1: pygame.draw.circle(screen, radius=0.5*radiusR, width=1, center=(offset + (arreteL+radiusR)*x - 0.5*radiusR, offset + (arreteH+radiusR)*y - 0.5*radiusR), color="black")            
                if x<longueur-1: pygame.draw.circle(screen, radius=0.5*radiusR, width=1, center=(offset + (arreteL+radiusR)*(x+1) - 0.5*radiusR, offset + (arreteH+radiusR)*y - 0.5*radiusR), color="black")            

def drawpeople(screen, labyrinthe, x,y, offset, couleur):
    hauteur, longueur = len(labyrinthe), len(labyrinthe[0])
    windowL = 1600
    windowH = 1000
    radiusR = 20
    arreteL = 50
    arreteH = 50
    pygame.draw.circle(screen, color=couleur, radius=0.5*radiusR, center=(offset + (arreteL+radiusR)*(x) - 0.5*radiusR, offset + (arreteH+radiusR)*(y) - 0.5*radiusR))

def drawwhatever (screen, labyrinthe, rob, pol, pause):
    offset = 100
    screen.fill((200,200,200))

    drawgrille(screen, labyrinthe, offset)
    drawpeople(screen, labyrinthe, rob[0], rob[1], offset, "black") # robber
    drawpeople(screen, labyrinthe, pol[0], pol[1], offset, "blue") # police
    if pause: time.sleep(0.2)
    return rob, pol

