def FindLeader(A):
    n=len(A)
    counter=1
    curr=A[0]
    for i in range(1,n):
        if counter==0:
            curr=A[i]
            counter=1
        else:
            if curr==A[i]:
                counter+=1
            else:
                counter-=1
                
    if counter==0: return -1
    c=0
    for el in A:
        if el==curr:
            c+=1
    if c>n/2: return curr
    else: return -1  

A=[1,1,1,2,2,2,2,2,2,2,1,3,4]
print(FindLeader(A))