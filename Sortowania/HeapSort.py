#get index of parent 
def parent(i):
    return (i-1)//2

#get index of left child
def left(i):
    return 2*i+1

#get index of right child
def right(i):
    return 2*i+2

#heapify element on index i
#A is array, n is size of heap
def heapify(A,n,i):
    max_index=i
    l=left(i)
    r=right(i)
    if r<n and A[max_index]<A[r]:
        max_index=r
    if l<n and A[max_index]<A[l]:
        max_index=l
    if i!=max_index:
        A[i],A[max_index]=A[max_index],A[i]
        heapify(A,n,max_index)

#build array representation of heap
def buildHeap(A):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)

#sort array by creating array representaion of heap,
#then move the biggest element (root) to last index, then repair smaller heap
#last element in array is sorted, 
#so we loop that behaviour until array will be sorted
def HeapSort(A):
    n=len(A)
    buildHeap(A)

    for i in range(n-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heapify(A,i,0)
