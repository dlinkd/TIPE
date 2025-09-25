import pygame
import time
from random import random, shuffle

def deplacement(labyrinthe, robber, police):
    keys={"z": pygame.K_z, "q": pygame.K_q, "s": pygame.K_s, "d": pygame.K_d}
    key_p = pygame.key.get_pressed()

    rx,ry = robber
    px,py = police


    hauteur, longueur = len(labyrinthe), len(labyrinthe[0])

    if True in key_p:
        if key_p[keys["z"]] and ry>0 and not labyrinthe[ry-1][rx][1]: ry-=1
        elif key_p[keys["q"]] and rx>0 and not labyrinthe[ry][rx-1][0]: rx-=1
        elif key_p[keys["s"]] and ry<hauteur-1 and not labyrinthe[ry][rx][1]: ry+=1
        elif key_p[keys["d"]] and rx<longueur-1 and not labyrinthe[ry][rx][0]: rx+=1
    return (rx,ry), (px,py), True in key_p

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
    rob, pol, pause = deplacement(labyrinthe, rob, pol) 

    drawgrille(screen, labyrinthe, offset)
    drawpeople(screen, labyrinthe, rob[0], rob[1], offset, "black") # robber
    drawpeople(screen, labyrinthe, pol[0], pol[1], offset, "blue") # police
    if pause: time.sleep(0.2)
    return rob, pol

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            self.parent[yr] = xr
            return True
        return False

def rendre_connexe(labyrinthe):
    hauteur = len(labyrinthe)
    longueur = len(labyrinthe[0])
    total_cells = hauteur * longueur
    uf = UnionFind(total_cells)

    # recup cases déjà connectées
    for y in range(hauteur):
        for x in range(longueur):
            cell_id = y * longueur + x
            if not labyrinthe[y][x][0] and x + 1 < longueur: # pas de mur EST
                voisin_id = y * longueur + (x + 1)
                uf.union(cell_id, voisin_id)
            if not labyrinthe[y][x][1] and y + 1 < hauteur:  # pas de mur SUD
                voisin_id = (y + 1) * longueur + x
                uf.union(cell_id, voisin_id)

    # murs séparants les composantestape 1 : union des cellules déjà connectées (murs absents)
    murs_potentiels = []
    for y in range(hauteur):
        for x in range(longueur):
            cell_id = y * longueur + x
            if x + 1 < longueur and labyrinthe[y][x][0]:  # mur EST
                voisin_id = y * longueur + (x + 1)
                if uf.find(cell_id) != uf.find(voisin_id):
                    murs_potentiels.append((cell_id, voisin_id, (y, x, 0)))
            if y + 1 < hauteur and labyrinthe[y][x][1]:  # mur SUD
                voisin_id = (y + 1) * longueur + x
                if uf.find(cell_id) != uf.find(voisin_id):
                    murs_potentiels.append((cell_id, voisin_id, (y, x, 1)))

    # mélanger les murs possibles pour équilibrer vertical/horizontal
    shuffle(murs_potentiels)

    # retirer les murs jusqu’à ce que tout soit connecté
    for cell_a, cell_b, (y, x, direction) in murs_potentiels:
        if uf.union(cell_a, cell_b):
            labyrinthe[y][x][direction] = False  # casser le mur
            if len(set(uf.find(i) for i in range(total_cells))) == 1:
                break

    return labyrinthe

def run(screen, labyrinthe):
    rob, pol = (0,0), (len(labyrinthe[0])-1, len(labyrinthe)-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        rob, pol = drawwhatever(screen, labyrinthe, rob, pol)
        pygame.display.update()
    pygame.quit()

def init():
    print("Veuillez choisir les paramètres du labyrinthe")
    pardef = input("Paramètre par défaut? (o/n)\n") == "o"
    hauteur = 25 if pardef else int(input("Hauteur ?\n"))
    longueur = 31 if pardef else int(input("Longueur ?\n"))
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
    
    if parfait: labyrinthe = rendre_connexe(labyrinthe)

    run(screen, labyrinthe)

init()