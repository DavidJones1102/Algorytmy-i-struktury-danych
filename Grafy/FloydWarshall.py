def FW(G):
    n = len(G)
    D = [[ float('inf') if j!=i and G[j][i] == 0 else G[j][i] for i in range(n) ] for j in range(n)]

    for i in range(n):
        for v in range(n):
            for u in range(n):
                D[v][u] = min( D[v][u], D[v][i] + D[i][u] )
    return D

G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
D = FW(G)
for i in range(len(D)):
    print(D[i])