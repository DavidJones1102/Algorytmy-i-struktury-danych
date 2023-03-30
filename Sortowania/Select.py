def partition(Tab,start,end):
        a=start-1
        for b in range(start,end+1):
            if Tab[b]<=Tab[end]:
                a+=1
                Tab[a],Tab[b]=Tab[b],Tab[a]
            
        return a

def select(A,l,k,r):
    if l==r: return A[l]

    q=partition(A,l,r)
    if q==k: return A[q]
    elif q<k: return select(A,q+1,k,r)
    else: return select(A,l,k,q-1)
def selectI(A,l,k,r):
    
    while l<=r:
        q=partition(A,l,r)
        if q==k: return A[q]
        elif q<k: l=q+1
        else: r=q-1
#A=[9,4,6,1,5,2,8,7,3,0]
#print(selectI(A,0,0,9))
A=['ala','a','aa','ula','ua','z']
A.sort()
print(A)
