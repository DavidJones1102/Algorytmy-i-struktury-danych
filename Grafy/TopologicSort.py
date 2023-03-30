def DFSVisit(sorted, visited, G, v):
    alfa = ['a','b','c','d','e','f','g']
    visited[v] = True
     
    for u in G[v]:
        if not visited[u]:
            DFSVisit(sorted, visited, G, u)
    sorted.insert(0,alfa[v])
    
def DFS(G):
    n = len(G)
    visited = [False for i in range(n)]
    sorted = []
    for i in range(n):
        if not visited[i]:
            DFSVisit(sorted, visited, G, i)
    return sorted

if __name__ == "__main__":
    G = [
        [1,2,5],
        [2,4],
        [],
        [],
        [3,6],
        [4],
        []
    ]
    print(DFS(G))
    

