#Funkcja przyjmuje tablice 
#i sortuje ją przez wstawianie 
def InsertionSort(T):
    n=len(T)
    j=1
    while j<n:
        i=j-1
        key=T[j]
        while i>=0 and key<T[i]: 
            T[i+1]=T[i]
            i-=1
        T[i+1]=key
        j+=1
    

if __name__=="__main__":
    T=[5,23,2,3,6,1]
    print(T)
    InsertionSort(T)
    print(T)
    

