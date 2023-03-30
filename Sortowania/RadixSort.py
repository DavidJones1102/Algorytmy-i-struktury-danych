from traceback import print_stack


def leng(n):
    l=0
    while n>0:
        n//=10
        l+=1
    return l

def CountSort(Tab,p):
    n=len(Tab)
    A=[0 for _ in range(10)]
    Sorted=[0 for _ in range(n)]
    for i in range(n):
        val=(Tab[i]//(10**p))%10
        A[val]+=1
    for i in range(1,10):
        A[i]+=A[i-1]
    
    for i in range(n-1,-1,-1):
        val=(Tab[i]//(10**p))%10
        index=A[val]-1
        Sorted[index]=Tab[i]
        A[val]-=1
    for i in range(n):
        Tab[i]=Sorted[i]

def RadixSort(T):
    l=leng(max(T))
    
    for i in range(l):
        CountSort(T,i)
def RadixSortString(T):
    
    T=[ (el,len(el)) for el in T]
    print(T)
 


#T=[111,233,43242,22,4124,112,121,211]
#RadixSort(T)
#
#print(T)