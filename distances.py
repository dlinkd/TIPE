from collections import deque

def distances_labyrinthe(lab, source):
    h = len(lab)
    w = len(lab[0])
    sx, sy = source

    dist = [[-1 for _ in range(w)] for _ in range(h)]
    dist[sy][sx] = 0

    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()
        d = dist[y][x]

        # Est
        if x + 1 < w and not lab[y][x][0] and dist[y][x + 1] == -1:
            dist[y][x + 1] = d + 1
            q.append((x + 1, y))

        # Ouest
        if x - 1 >= 0 and not lab[y][x - 1][0] and dist[y][x - 1] == -1:
            dist[y][x - 1] = d + 1
            q.append((x - 1, y))

        # Sud
        if y + 1 < h and not lab[y][x][1] and dist[y + 1][x] == -1:
            dist[y + 1][x] = d + 1
            q.append((x, y + 1))

        # Nord
        if y - 1 >= 0 and not lab[y - 1][x][1] and dist[y - 1][x] == -1:
            dist[y - 1][x] = d + 1
            q.append((x, y - 1))

    return dist

def min_mat(l_mat):
    mat = []
    for y in range(len(l_mat[0])):
        mat.append([])
        for x in range(len(l_mat[0][0])):
            m = 1000000
            for i in range(len(l_mat)):
                if l_mat[i][y][x] < m: m = l_mat[i][y][x]
            mat[y].append(m)
    return mat
            

def calc_sit(labyrinthe, robber, policemen):
    dist_R = distances_labyrinthe(labyrinthe, robber)
    dist_P = []
    for p in policemen:
        dist_P.append(distances_labyrinthe(labyrinthe, p))

    dist_P = min_mat(dist_P)
    for y in range(len(labyrinthe)):
        for x in range(len(labyrinthe[0])):
            if dist_R[y][x] >= 0 and dist_R[y][x] < dist_P[y][x]: dist_R[y][x] = True
            else: dist_R[y][x] = False
        dist_R[y].append(False)
    dist_R.append([False]*(len(labyrinthe[0])+1))
    return dist_R