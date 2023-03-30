n=0
class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
def make_ll(tab):
    n=len(tab)
    first = None
    for i in range(n-1,-1,-1):
        new=Node(tab[i])
        new.next=first
        first=new
    return first
def show_ll(first):
    if first.val==None:
        first=first.next 
    temp=first
    ans=''
    while temp is not None:
        ans+='->'+str(temp.val)
        temp=temp.next 
        
    print(ans[2:])

def heapify(tab,i):
    global n
    i_max=i
    l=2*i+1
    p=2*i+2
    if tab[i]==None and n>1:
        tab[i],tab[n-1]=tab[n-1],tab[i]
        n-=1
        heapify(tab,0)
    else:
        if l<n and tab[i_max].val>tab[l].val:
            i_max=l
        if p<n and tab[i_max].val>tab[p].val:
            i_max=p
        if i_max!=i:
            tab[i],tab[i_max]=tab[i_max],tab[i]
            heapify(tab,i_max)

def build_heap(tab):
    global n
    n=len(tab)

    for i in range((n-2)//2,-1,-1):
        heapify(tab,i)

def MergeK(tab):
    build_heap(tab)

    sorted=tab[0]
   
    next=sorted

    while tab[0] != None:
        tab[0]=tab[0].next
        heapify(tab,0)
        next.next=tab[0]
        next=next.next
         
    return sorted

p1=make_ll([1,3,5,6,7])
p2=make_ll([2,3,4])
p3=make_ll([6,7,8,11])
p4=make_ll([1,3,6,9])
p5=make_ll([1,5,8,11])

tab=[p1,p2,p3,p4,p5]

p=MergeK(tab)
show_ll(p)