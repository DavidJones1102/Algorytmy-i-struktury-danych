#Szymon Głomski
#Algorytm dla małych k sortuje liste, sortowaniem przez wybieranie
#ze złożonością Θ(nk), dla większych k sortuje liste przez scalanie
#ze złożonością Θ(nlogn)
from zad1testy import Node, runtests

#def Scal(p1,p2):
#    if p1 is None:
#        return p2
#    elif p2 is None:
#        return p1
#        
#    if p1.val>p2.val:
#        f=p2
#        p2=p2.next
#    else: 
#        f=p1
#        p1=p1.next
#    t=f
#    while p1 is not None and p2 is not None:
#        if p1.val>p2.val:
#            t.next=p2
#            t=t.next
#            p2=p2.next
#        else:
#            t.next=p1
#            t=t.next
#            p1=p1.next
#     
#    if p1!=None:
#        t.next=p1
#    elif p2!=None:
#        t.next=p2
#    return f
#
#def FindMiddle(p):
#    if p==None or p.next==None:
#        return p
#    slow=p
#    fast=p
#    while fast.next is not None and fast.next.next is not None:
#        fast=fast.next.next
#        slow=slow.next
#    return slow
#
#def MergeSort(p):
#    if p.next is None:
#        return p
#    mid = FindMiddle(p)
#    mid_next=mid.next
#    mid.next = None
#    left=MergeSort(p)
#    right=MergeSort(mid_next)
#    
#    result=Scal(left,right)
#    return result
#
#def SortH(p,k):
#    if k>10:
#        p=MergeSort(p)
#        return p
#    temp=p
#    n=None
#    while temp is not None:
#        min=temp
#        n=temp.next
#
#        for _ in range(k):
#            if n is None: break
#            if min.val>n.val:
#                min=n
#            n=n.next
#        min.val,temp.val=temp.val,min.val
#        temp=temp.next
#    return p
def heapify(T,n,i):
    max_index=i
    l=2*i+1
    p=2*i+2

    if l<n and T[max_index].val>T[l].val:
        max_index=l
    if p<n and T[max_index].val>T[p].val:
        max_index=p
    if max_index!=i:
        T[max_index],T[i]=T[i],T[max_index]
        heapify(T,n,max_index)
def build_heap(T,n):
    for i in range((n-2)//2,-1,-1):
        heapify(T,n,i)

def SortH(p,k):
    tab=[None for _ in range(k+1)]
 
    for i in range(k+1):
        tab[i]=p
        
        if p.next==None:
            k=i
            break
        p=p.next

    build_heap(tab,k+1)
    new=tab[0]
    sorted=new
    print(sorted.val)
    while p is not None:
        tab[0]=p
        heapify(tab,k+1,0)
        new.next=tab[0]
        new=new.next
        p=p.next

    for i in range(k,0,-1):
        tab[0]=tab[i]
        heapify(tab,i,0)
        new.next=tab[0]
        new=new.next
    new.next=None
    return sorted

runtests( SortH ) 

