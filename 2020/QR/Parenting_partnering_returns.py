from math import inf
t=int(input())

def solve(T):
    N=int(input())
    sol=["Q"]*N
    S=[]
    E=[]
    for i in range(N):
        s,e=list(map(int,input().split()))
        S.append(s)
        E.append(e)
    c_busy_until=0
    j_busy_until=0
    for i in range(N):
        f=min(S)
        ind=S.index(f)
        if c_busy_until<=f:
            sol[ind]="C"
            c_busy_until=E[ind]
            S[ind]=inf
            E[ind]=inf

        elif j_busy_until<=f:
            sol[ind]="J"
            j_busy_until=E[ind]
            S[ind]=inf
            E[ind]=inf
        else:
            break
    if "Q" in sol:
        sol="IMPOSSIBLE"
    print("Case #{}: {}".format(T,''.join(sol)))

for i in range(1,t+1):
    solve(i)