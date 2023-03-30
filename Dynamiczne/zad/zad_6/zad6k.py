from zad6ktesty import runtests 

def haslo ( S ):
    n = len(S)
    T = [0 for i in range(n)]
    T[0]=1
    if S[0]=='1' or (S[0] == '2' and S[1]<='6'):
        T[1] = 2
    else: T[1] = 1

    for i in range(2,n):
        T[i] = T[i-1]
        if ((S[i-1]=='1'and S[i]!='0') or (S[i-1] == '2' and '0'<S[i]<='6')):
            T[i] += T[i-2]
        if S[i]=='0':
            T[i] = T[i-2]
        if S[i]=='0' and (S[i-1]!='1' and S[i-1]!='2'):
            return 0

    return T[n-1]

runtests ( haslo )