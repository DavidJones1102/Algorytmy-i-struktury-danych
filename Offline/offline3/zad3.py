from zad3testy import runtests
#Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały
#wygenerowane z pewnego rozkładu losowego. Rozkład ten mamy zadany jako k przedziałów
#[a1, b1],[a2, b2], . . . ,[ak, bk] takich, że i-ty przedział jest wybierany z 
#prawdopodobieństwem ci, a liczba z przedziału (x ∈ [ai, bi]) jest losowana 
#zgodnie z rozkładem jednostajnym. Przedziały mogą na siebie nachodzić. Liczby ai, bi 
#są liczbami naturalnymi ze zbioru {1, . . . , N}.
#Proszę zaimplementować funkcję SortTab(T, P) sortująca podaną tablicę i zwracająca 
#posortowaną tablicę jako wynik. Pierwszy argument to tablica do posortowania a drugi 
#to opis przedziałów w postaci:
#P = [(a_1,b_1,c_1), (a_2,b_2,c_2), ..., (a_k,b_k,c_k)]}.
#Na przykład dla wejścia:
#T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
#P = [(1, 5, 0.75) , (4, 8, 0.25)]
#po wywołaniu SortTab(T,P) tablica zwrócona w wyniku powinna mieć postaci:
#T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]
def QuickSort(Tab,start,end):
    while start<end:
        a=start
        for b in range(start,end+1):
            if Tab[b]<=Tab[end]:
                Tab[a],Tab[b]=Tab[b],Tab[a]
                a+=1
            
        if end-a<a-2-start:
            QuickSort(Tab,a,end)
            end=a-2
        else:
            QuickSort(Tab,start,a-2)
            start=a
def SortTab(T,P):
    n=len(T)
    if n>10:
        l=10
    else: l=1
    a_min=P[0][1]

    for a,b,p in P:
        if a<a_min:
            a_min=a

    Buckets = [[] for _ in range(n//l)]    
    for el in T:
        Buckets[int(el/l-a_min/l)].append(el)
    for B in Buckets:
        QuickSort(B,0,len(B)-1)
    
    k=0
    for i in range(n//l):
        for j in range(len(Buckets[i])):
            T[k]=Buckets[i][j]
            k+=1


    return  T

runtests( SortTab )