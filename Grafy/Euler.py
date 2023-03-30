def DFSVisit(Euler, G, v):
    alfa = ['a','b','c','d','e','f','g']
     
    while G[v]:
        u = G[v][0]
        G[v].remove(u)
        G[u].remove(v)
    
        DFSVisit(Euler, G, u)
    Euler.insert(0,alfa[v])
    
def DFS(G):
    n = len(G)
    Euler = []
    DFSVisit(Euler, G, 0)
    return Euler

if __name__ == "__main__":
    G = [
        [1,2], # a 0
        [0,2,3,5],   # b 1
        [0,1,3,5],      # c 2
        [1,2,4,5],      # d 3 
        [3,5],   # e 4
        [1,2,3,4],     # f 5
    ]
    print(DFS(G))
    

