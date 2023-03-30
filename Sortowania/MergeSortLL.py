#Merge 2 sorted lists into 1 sorted list
from heapq import merge


def Merge(p1,p2):
    if p1 is None:
        return p2
    elif p2 is None:
        return p1
        
    if p1.val>p2.val:
        f=p2
        p2=p2.next
    else: 
        f=p1
        p1=p1.next
    t=f
    while p1 is not None and p2 is not None:
        if p1.val>p2.val:
            t.next=p2
            t=t.next
            p2=p2.next
        else:
            t.next=p1
            t=t.next
            p1=p1.next
     
    if p1!=None:
        t.next=p1
    elif p2!=None:
        t.next=p2
    return f

#Get middle element of list
def GetMiddle(p):
    if p==None or p.next==None:
        return p
    slow=p
    fast=p
    while fast.next is not None and fast.next.next is not None:
        fast=fast.next.next
        slow=slow.next
    return slow

#Sort array by dividing it on 2 smaller arrays
#then sort smaller array and merge it into 1 sorted list
def MergeSort(p):
    if p.next is None:
        return p
    mid = GetMiddle(p)
    mid_next=mid.next
    mid.next = None
    left=MergeSort(p)
    right=MergeSort(mid_next)
    
    result=Merge(left,right)
    return result

def MergeSortNaturalSeries(p):
    heads=[]
    heads.append(p)
    curr=p

    while curr is not None:
        if curr.val<=curr.next.val:
            curr=curr.next
        else:
            temp=curr
            curr=curr.next
            heads.append(curr)
            temp.next=None
    
    while len(heads)>1:
        heads[0]=merge(heads[0],heads[1])
        del heads[1]
    return heads[0]
