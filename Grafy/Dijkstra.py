import queue
def dijkstra(graph, start):

    distances = [float("inf") for _ in range(len(graph))]
    #visited = [False for _ in range(len(graph))]
    distances[start] = 0
    PQ = queue.PriorityQueue()
    PQ.put(( 0, start  ))

    while not PQ.empty(): 
        shortest_distance, shortest_index = PQ.get()

        for i in range(len(graph)):
            if graph[shortest_index][i] != 0 and distances[i] > distances[shortest_index] + graph[shortest_index][i]:
                distances[i] = distances[shortest_index] + graph[shortest_index][i]
                PQ.put(( distances[i], i ))

        #visited[shortest_index] = True
    return distances
    
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
print(dijkstra(G,3))