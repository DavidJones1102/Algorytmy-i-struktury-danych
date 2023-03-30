from zad1testy import runtests
from queue import PriorityQueue

def chaos_index( T ):
    PQ = PriorityQueue()
    n = len( T )

    for i in range( n ):
        PQ.put( (T[i],i) )

    k = 0
    index = 0
    while not PQ.empty():
        v,i = PQ.get()
        k = max(k, abs(i-index))
        index+=1
        
    return k


runtests( chaos_index )
