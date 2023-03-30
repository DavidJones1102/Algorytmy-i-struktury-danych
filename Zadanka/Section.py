

def partition(A,l,r):
    a=l-1
    pivot=A[r]
    for i in range(l,r+1):
        if A[i]<=pivot:
            a+=1
            A[a],A[i]=A[i],A[a]
    return a
def select(A,k):
    l,r=0,len(A)-1
    while l<=r:
        q=partition(A,l,r)

        if q==k: return A[q]
        elif q<k: l=q+1
        else: r=q-1 
def Section(T,p,q):
    New = [0 for i in range(q-p+1)]
    p=select(T,p)
    q=select(T,q)
A=[1,4,2,3]
print(select(A,2))
