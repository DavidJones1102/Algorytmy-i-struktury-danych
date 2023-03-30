from random import randint

def partition(Tab,start,end):
        a=start-1
        for b in range(start,end+1):
            if Tab[b]<=Tab[end]:
                a+=1
                Tab[a],Tab[b]=Tab[b],Tab[a]
            
        return a
#253
#

def QuickSort(Tab,start,end):
    while start<end:
        q=partition(Tab,start,end)
            
        if end-q<q-start:
            QuickSort(Tab,q+1,end)
            end=q-1
        else:
            QuickSort(Tab,start,q-1)
            start=q+1
T=[randint(0,1000) for _ in range(100)] 
print(T)
QuickSort(T,0,len(T)-1)
print(T)

