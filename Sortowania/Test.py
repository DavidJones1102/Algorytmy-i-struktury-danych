from random import randint
import time
from HeapSort import HeapSort
from InsertionSort import InsertionSort
from QuickSort import QuickSort
from MergeSort import MergeSort
        
T=[randint(0,1000) for _ in range(7)]
T1=T.copy()

t0=time.time()
InsertionSort(T)
t1=time.time()-t0
print(t1)

t0=time.time()
QuickSort(T1,0,len(T1)-1)
t1=time.time()-t0


#t0=time.time()
#InsertionSort(T2)
#t1=time.time()-t0
print(t1)
 

