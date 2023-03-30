def BinarySearch(A,el):
    l=0
    p=len(A)-1
    while l<=p:
        mid=l+(p-l)//2
        if el==A[mid]: return mid
        elif el>A[mid]: l=mid+1
        else: p=mid-1
    return -1
def BinarySearchR(T,start,end,el):
    if start<=end:
        mid= start+(end-start)//2
        if T[mid]==el: return mid
        elif T[mid]>el: return BinarySearchR(T,start,mid-1,el)
        else: return BinarySearchR(T,mid+1,end,el)
    return -1

#A=[1,4,7,9,11,15,18]
#i=BinarySearchR(A,0,6,15)
#print(i)
