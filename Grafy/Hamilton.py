import collections

def Hamilton( G ):

    n = len(G)
    Q = collections.deque([0])
    visited = [  False for i in range(n) ]

    path = [0]
    visited[0] = True

    while Q:
        v = Q.pop()
        if v != None:
                         
            path.append(v)  
            visited[v]  = True
            if len(path) == n and v in G[0]:
                return path

            for u in G[v]:
                if not visited[u]:
                    Q.append(None)
                    Q.append(u)
        # Pop None znaczy, że wracamy w scieżce
        else:
            u = path.pop()
            visited[u] = False

    return None