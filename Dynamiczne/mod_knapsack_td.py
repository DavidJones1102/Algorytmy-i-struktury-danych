W=[1,2,3,4,5]
P=[3,4,1,4,4]
w,p = 5,5
#12
##########################
#####################
#########################
###############
def rek(F,W,P,cw,cp,i):
    if i==len(P)-1:
        if cp <=0:
            F[i][cw] = 1
            return 1
        else:
            F[i][cw] = 0 
            return 0
    if F[i][cw]!=-1: return F[i][cw]


    F[i][cw] = rek(F,W,P,cw,cp,i+1)
    if W[i]<=cw and cp-P[i]<=0:
        F[i][cw] += 1 + rek(F,W,P,cw-W[i],cp-P[i],i+1)
    elif W[i]<=cw: F[i][cw] +=rek(F,W,P,cw-W[i],cp-P[i],i+1)

    return F[i][cw]
def mk(W,P,w,p):
    n = len(W)

    F = [[-1 for g in range(w+1)]for i in range(n)]
    F[0][w] = rek(F,W,P,w,p,0)
    return F[0][w]
print(mk(W,P,w,p))
