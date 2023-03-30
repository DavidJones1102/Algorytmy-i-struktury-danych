import collections
def DFS(G):
    n = len(G)
    visited = [False for i in range(n)]
    time = [None for i in range(n)]
    stack = collections.deque()
    t = 1
    for i in range(n):
        if not visited[i]:
            DFSVisit(stack, G, visited, i)
    return stack

def DFSVisit(stack, G, visited, v):
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            DFSVisit(stack, G, visited, u)
    stack.append(v) 

def reverse(G):
    n = len(G)
    new = [[] for i in range(n)]
    for i in range(n):
        for u in G[i]:
            new[u].append(i)
    return new
def DFSVisit2(G, visited, v):
    a = ['a','b','c','d','e','f','g','h','i','j','k']
    visited[v] = True
    print(a[v],end=' ')
    for u in G[v]:
        if not visited[u]:
            DFSVisit2(G, visited, u)
def SCC(G):
    stack = DFS(G)
    reversed = reverse(G)
    scg = []
    visited = [False for i in range(len(G))]
    while stack:
        u = stack.pop()
        if not visited[u]:
            DFSVisit2(reversed,visited,u)
            print('')

        



if __name__ == "__main__":
    G = [
        [1],
        [2,4],
        [0,9],
        [4,6],
        [5],
        [3],
        [5],
        [9],
        [3,7],
        [10],
        [5,8]        
    ]
    SCC(G)
    