def partition(T,l,r):
    n=len(T)
    pivot=T[r//n][r%n]
    a=l
    for i in range(l,r+1):
        if T[i//n][i%n]<=pivot:
            T[a//n][a%n],T[i//n][i%n]=T[i//n][i%n],T[a//n][a%n]
            a+=1
    return a-1

def select(T,index,l,r):
    n=len(T)
    if l==r: return T[l//n][l%n]
    if l<r:
        q=partition(T,l,r)
        if q==index: return T[q//n][q%n]
        elif q<index: return select(T,index,q+1,r)
        else: return select(T,index,l,q-1)
    
def Median(T):
    n=len(T)
    a=(n*n-n)//2
    b=a+n-1

    a=select(T,a,0,n*n-1)
    b=select(T,b,0,n*n-1)
    New=[[None for i in range(n)] for j in range(n) ]
    p=[0,0]
    l=[1,0]
    h=[0,1]
    for i in range(n*n):
        if T[i//n][i%n]<a:
            New[l[0]][l[1]]=T[i//n][i%n]
            if l[1]+1<l[0]: l[1]+=1
            else: 
                l[0]+=1
                l[1]=0

        elif T[i//n][i%n]>b:
            New[h[0]][h[1]]=T[i//n][i%n]
            if h[1]+1<n: h[1]+=1
            else: 
                h[0]+=1
                h[1]=h[0]+1
        else:
            New[p[0]][p[1]]=T[i//n][i%n]
            p[0]+=1
            p[1]+=1        


    return New
T=[[2,3,5],[7,11,13],[17,19,23]]
T=Median(T)

print(T[0])
print(T[1])
print(T[2])


