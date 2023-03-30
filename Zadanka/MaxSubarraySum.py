#I assume that parameters are correct
def Find_max_crossing_subarray(T,low,mid,high):
    left_sum=0
    left_index=mid
    sum=0
    for i in range(mid-1,low-1,-1):
        sum+=T[i]
        if sum>left_sum:
            left_index=i
            left_sum=sum
    
    right_sum=0
    right_index=mid
    sum=0
    for i in range(mid+1,high+1):
        sum+=T[i]
        if sum>right_sum:
            right_index=i
            right_sum=sum
    return left_index,right_index,right_sum+left_sum+T[mid]

def Find_max_subarray(T,low,high):
    if low==high:
        return low,high,T[low]
    
    mid=(low+high)//2
    left_low,left_high,left_sum=Find_max_subarray(T,low,mid)
    right_low,right_high,right_sum=Find_max_subarray(T,mid+1,high)
    cross_low,cross_high,cross_sum=Find_max_crossing_subarray(T,low,mid,high)
    if left_sum>right_sum and left_sum>cross_sum:
        return left_low,left_high,left_sum
    elif left_sum<right_sum and right_sum>cross_sum:
        return right_low,right_high,right_sum
    else:
        return cross_low,cross_high,cross_sum

def F_m_s(T):
    right_index=0
    left_index=0
    sum=T[0]
    max_sum=sum
    for i in range(1,len(T)):
        sum+=T[i]
        if sum>max_sum:
            max_sum=sum
            right_index=i
    for i in range(right_index):
        sum-=T[i]
        if sum>max_sum:
            max_sum=sum
            left_index=i+1
    return left_index,right_index,max_sum
t=[1,-2,3,4,5,6]
print(Find_max_subarray(t,0,len(t)-1))
print(F_m_s(t))
