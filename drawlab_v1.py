import pygame
from random import random, shuffle
from controll import controll_keys

def drawgrille(screen, labyrinthe, offset):
    hauteur, longueur = len(labyrinthe), len(labyrinthe[0])

    tailleH = 600/(hauteur+1)
    tailleL = 1000/(longueur+1)
    
    pygame.draw.line(screen, start_pos= (offset, offset), end_pos= (offset + tailleL*longueur, offset), color="black", width=5)
    pygame.draw.line(screen, start_pos= (offset, offset), end_pos= (offset, offset+tailleH*hauteur), color="black", width=5)

    for y in range(hauteur):
        for x in range(longueur):
            if(labyrinthe[y][x][0]): 
                pygame.draw.line(screen, start_pos= (offset + tailleL*(x+1), offset + tailleH*y), end_pos= (offset + tailleL*(x+1), offset + tailleH*(y+1)), color="black", width=5)
            if(labyrinthe[y][x][1]): 
                pygame.draw.line(screen, start_pos= (offset + tailleL*x, offset + tailleH*(y+1)), end_pos= (offset + tailleL*(x+1), offset + tailleH*(y+1)), color="black", width=5)

def drawpeople(screen, labyrinthe, x,y, offset, couleur):
    hauteur, longueur = len(labyrinthe), len(labyrinthe[0])
    tailleH = 600/(hauteur+1)
    tailleL = 1000/(longueur+1)
    pygame.draw.ellipse(screen, color=couleur, rect=((offset+tailleL/8) + tailleL*x, (offset+tailleH/8) + tailleH*y, tailleL*0.65, tailleH*0.65))

def drawwhatever (screen, labyrinthe, rob, pol):
    offset = 100
    screen.fill((200,200,200))

    drawgrille(screen, labyrinthe, offset)
    drawpeople(screen, labyrinthe, rob[0], rob[1], offset, "black") # robber
    drawpeople(screen, labyrinthe, pol[0], pol[1], offset, "blue") # police
    return rob, pol