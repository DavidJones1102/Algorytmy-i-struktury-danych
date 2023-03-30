import collections
def DFS( G ):
    n = len(G)
    Q = collections.deque()
    visited = [ False for i in range(n) ]
     
    for i in range(n):
        if not visited[i]:
            Q.append(i)
            visited[i] = True
        while Q:
            v = Q.pop()
            print(v)
            for u in G[v]:
                if not visited[u]:
                    Q.append(u)
                    visited[u] = True




