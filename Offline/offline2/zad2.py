from zad2testy import runtests

def QuickSort(Tab,start,end):
    while start<end:
        a=start
        for b in range(start,end+1):
            if Tab[b][0]<=Tab[end][0]:
                Tab[a],Tab[b]=Tab[b],Tab[a]
                a+=1      
        if end-a<a-2-start:
            QuickSort(Tab,a,end)
            end=a-2
        else:
            QuickSort(Tab,start,a-2)
            start=a
    
#                   last 
# 0--------0        0 0
#   0----0          1 0
#     0-------0     2 2
#     0----------0  3 3
#     0----0        4 3
#       0-----0     5 3
#            0----0 6 6

def depth(L):
    n=len(L)
    QuickSort(L,0,n-1)
    counter=0
    j=1

    while j<n and L[0][1]>=L[j][0]:
        if L[j][1]<=L[0][1]:
            counter+=1
        j+=1
    max_counter=counter
    counter=0
    last=0
 
    for i in range(1,n):
        j=i+1
        if L[i][1]>L[last][1]:
            while j<n and L[i][1]>=L[j][0]:
                if L[j][1]<=L[i][1]:
                    counter+=1
                j+=1
    
            j=i-1
            while j>=0 and L[j][0]==L[i][0]:
                if L[j][1]<=L[i][1]:
                    counter+=1
                j-=1
        
            if counter>max_counter:
                max_counter=counter
            counter=0
            last=i

    return max_counter

runtests( depth ) 
