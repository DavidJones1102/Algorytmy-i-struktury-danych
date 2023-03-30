#Sortowanie n licz z przedziału [0,1] w rozkładzie jednostajnym
from InsertionSort import InsertionSort
def BucketSort(T,n):
    B=[[] for _ in range(n)]

    for el in T:
        index=int(el*(1/n)*100)
        B[index].append(el)
    for el in B:
        InsertionSort(B)
    
    k=0
    for i in range(n):
        for j in range(len(B[i])):
            T[k]=B[i][j]
            k+=1
    
#T=[0.1,0.03,0.21,0.99,0.77,0.44,0.55,0.88,0.66]
#
#BucketSort(T,10)
#print(T)