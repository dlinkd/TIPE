from random import random, shuffle

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