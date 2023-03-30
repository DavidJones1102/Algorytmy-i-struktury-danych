# l - rod length
# C[i] - price of element of lenght i 
L = 5
C = [0,4,5,7,13,14]

# f(l) - max profit from lenght - l
# f(l) - max(f(l-k)+C[k])
# 0<k<=l
def print_sol(P):
    i = len(P)-1
    while(i != 0):
        print(i - P[i])        
        i = P[i]

def max_profit(C, L):
    F = [0 for _ in range(L+1)]
    P = [0 for _ in range(L+1)]
    for l in range(1,L+1):
        max_p = 0
        max_i = 0
        for k in range(1,l+1):
            if max_p < F[l-k] + C[k]:
                max_p =  F[l-k] + C[k]
                max_i = k
        P[l] = l-max_i
        F[l] = max_p
    print_sol(P)
    return F[L]
max_p = max_profit(C,L)
