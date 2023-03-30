def RemoveDuplicates(T):
# 1 2 2 3 4 4 5 5 5 
#       i      
#     j       
 
    j=1
    for i in range(1,len(T)):
        if T[i-1]!=T[i]:
            T[j]=T[i]
            j+=1
    return j
#T=[1,2,2,3,3,4,5,5,5,6,7,8,8,8,8,9]
#
#n=RemoveDuplicates(T)
#print(T,n)
