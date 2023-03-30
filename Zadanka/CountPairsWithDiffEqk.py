#Count all distinct pairs with difference equal to k
def partition(T,start,end):
    a=start
    pivot=T[end]
    for i in range(start,end+1):
        if T[i]<=pivot:
            T[i],T[a]=T[a],T[i]
            a+=1
    return a-1
def QuickSort(T,start,end):

    while start<end:
        q=partition(T,start,end)
        if end-q<q-start:
            QuickSort(T,q+1,end)
            end=q-1
        else:
            QuickSort(T,start,q-1)
            start=q+1
def RemoveDuplicates(T):
    j=1
    for i in range(1,len(T)):
        if T[i-1]!=T[i]:
            T[j]=T[i]
            j+=1
    return j
def BinarySearch(T,start,end,el):
    if start<=end:
        mid= start+(end-start)//2
        if T[mid]==el: return mid
        elif T[mid]>el: return BinarySearch(T,start,mid-1,el)
        else: return BinarySearch(T,mid+1,end,el)
    return -1

def CountPairsK(A,k):
    c=0
    QuickSort(A,0,len(A)-1)
    n=RemoveDuplicates(A)

    for i in range(n):
        if BinarySearch(A,i,n-1,A[i]+k)!=-1: c+=1
    return c
#print(CountPairsK([7,11,3,7,3,9,5],4))