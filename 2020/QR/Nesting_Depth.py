t=int(input())

def solve(T):
    S=input()
    t=""
    p_right=0
    for i in range(len(S)):
        s=int(S[i])
        if s<p_right:
            t+=")"*(p_right-s)
            p_right=s
        if s>p_right:
            t+="("*(s-p_right)
            p_right=s
        t+=S[i]
    t+=")"*p_right
    print("Case #{}: {}".format(T,t))

for i in range(1,t+1):
    solve(i)