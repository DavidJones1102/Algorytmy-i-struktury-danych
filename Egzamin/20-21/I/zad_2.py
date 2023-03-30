from zad2testy import runtests
from queue import PriorityQueue

def robot( L, A, B ):

    nx = len(L[0]) #x
    ny = len(L) #y
    PQ = PriorityQueue()

    t = [ [[[float('inf') for vel in range(3)] for dir in range(4)] for x in range(nx)] for y in range(ny)]

    steps = [ ('o',1), ('o',-1), ('d',0), ('d',1), ('d',2) ]
    # kierunek 0-prawo 1-dół 2-lewo 3-góra
    # prędkość 1-60,2-40,3-30
    # obrót 45
    t[A[0]][A[1]][0][0] = 0
    # time, vertex, velocity, direction
    PQ.put( (0, A, 0 + 4*1 ) )

    while not PQ.empty():

        curr,P,to_calc = PQ.get()
        v = to_calc//4
        d = to_calc%4

        for step in steps:
            dir_after = (d+step[1])%4
            if step[0] =='o' and t[P[1]][P[0]][ dir_after ][0] > curr + 45:
                t[P[1]][P[0]][ (d+step[1])%4 ][0] = curr + 45
                PQ.put( (curr+45, P, dir_after+ 1*4) )
            
            elif step[0] == 'd':
                if d == 0 and P[0]+1 < nx and L[P[1]][P[0]+1] == ' ' :
                    if v == 1 and t[P[1]][P[0] + 1][ d ][1] > curr + 60:
                        t[P[1]][P[0] + 1][ d ][1] = curr + 60
                        PQ.put( (curr+60, (P[0]+1,P[1]), 2*4+ d) )

                    elif v == 2 and t[P[1]][P[0] + 1][ d ][2] > curr + 40:
                        t[P[1]][P[0] + 1][ d ][1] = curr + 40
                        PQ.put( (curr+40, (P[0]+1,P[1]), 3*4+ d) )

                    elif v == 3 and t[P[1]][P[0] + 1][ d ][2] > curr + 30:
                        t[P[1]][P[0] + 1][ d ][1] = curr + 30
                        PQ.put( (curr+30, (P[0]+1,P[1]), 3*4+ d) )
            
                elif d == 1 and P[1]+1 < ny and L[P[1]+1][P[0]] == ' ' :
                    if v == 1 and t[P[1]+1][P[0]][ d ][1] > curr + 60:
                        t[P[1]+1][P[0]][ d ][1] = curr + 60
                        PQ.put( (curr+60, (P[0],P[1]+1), 2*4+ d) )

                    elif v == 2 and t[P[1]+1][P[0]][ d ][2] > curr + 40:
                        t[P[1]+1][P[0]][ d ][1] = curr + 40
                        PQ.put( (curr+40, (P[0],P[1]+1), 3*4+ d) )

                    elif v == 3 and t[P[1]+1][P[0]][ d ][2] > curr + 30:
                        t[P[1]+1][P[0]][ d ][1] = curr + 30
                        PQ.put( (curr+30, (P[0],P[1]+1), 3*4+ d) )

                elif d == 2 and P[0]-1 >= 0 and L[P[1]][P[0]-1] == ' ' :
                    if v == 1 and t[P[1]][P[0] - 1][ d ][1] > curr + 60:
                        t[P[1]][P[0] - 1][ d ][1] = curr + 60
                        PQ.put( (curr+60, (P[0]-1,P[1]), 2*4+ d) )

                    elif v == 2 and t[P[1]][P[0] - 1][ d ][2] > curr + 40:
                        t[P[1]][P[0] - 1][ d ][1] = curr + 40
                        PQ.put( (curr+40, (P[0]-1,P[1]), 3*4+ d) )

                    elif v == 3 and t[P[1]][P[0] + 1][ d ][2] > curr + 30:
                        t[P[1]][P[0] - 1][ d ][1] = curr + 30
                        PQ.put( (curr+30, (P[0]-1,P[1]), 3*4+ d) )

                elif d == 3 and P[1]-1 >= 0 and L[P[1]-1][P[0]] == ' ' :
                    if v == 1 and t[P[1]-1][P[0]][ d ][1] > curr + 60:
                        t[P[1]-1][P[0]][ d ][1] = curr + 60
                        PQ.put( (curr+60, (P[0],P[1]-1), 2*4+ d) )

                    elif v == 2 and t[P[1]-1][P[0]][ d ][2] > curr + 40:
                        t[P[1]-1][P[0]][ d ][1] = curr + 40
                        PQ.put( (curr+40, (P[0],P[1]-1), 3*4+ d))

                    elif v == 3 and t[P[1]-1][P[0]][ d ][2] > curr + 30:
                        t[P[1]-1][P[0]][ d ][1] = curr + 30
                        PQ.put( (curr+30, (P[0],P[1]-1), 3*4+ d) )


 
    ans = min ( min(t[B[1]][B[0]][0]), min(t[B[1]][B[0]][1]), min(t[B[1]][B[0]][2]), min(t[B[1]][B[0]][3]) )
    if ans == float('inf'):
        return None
    return ans


runtests( robot )
