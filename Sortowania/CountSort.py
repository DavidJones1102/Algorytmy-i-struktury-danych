#sortowanie liczb z przedziału [a,b]
#(x - a) / (b - a) * n
#[a, b)
#x - to twoje t[i]
def CountSort(Tab,a,b):
    n=len(Tab)
    diff=b-a+1
    A=[0 for _ in range(diff+1)]
    Sorted=[0 for _ in range(n)]
    for i in range(n):
        val=Tab[i]
        A[val-a]+=1
    for i in range(1,diff+1):
        A[i]+=A[i-1]

    for i in range(n):
        val=Tab[i]
        index=A[val-a]-1
        Sorted[index]=Tab[i]
        A[val-a]-=1
    Tab = Sorted

#t=[5,6,8,9,9,7,10]
#
#CountSort(t,5,10)
#print(t)