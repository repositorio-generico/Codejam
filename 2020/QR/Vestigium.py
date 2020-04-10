t=int(input())

def solve(T):
    N=int(input())
    t=0
    r=0
    c=0
    M=[]
    for i in range(N):
        l=list(map(int,input().split()))
        M.append(l)
        t+=l[i]
        if len(set(l))!=N:
            r+=1
    for i in range(N):
        S=[]
        for j in range(N):
            if M[j][i] in S:
                c+=1    
                break
            else:
                S.append(M[j][i])
    print("Case #{}: {} {} {}".format(T,t,r,c))
for i in range(1,t+1):
    solve(i)