def MergeSort(Tab):
    if len(Tab)>1:
        mid=len(Tab)//2
        L=Tab[:mid]
        R=Tab[mid:]

        MergeSort(L)
        MergeSort(R)

        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]>R[j]:
                Tab[k]=R[j]
                j+=1
            else:
                Tab[k]=L[i]
                i+=1
            k+=1
        
        while i<len(L):
            Tab[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            Tab[k]=R[j]
            j+=1
            k+=1