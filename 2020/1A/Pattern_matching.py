t=int(input())

def solve(T):
    N=int(input())
    pre=[]
    suf=[]
    word=''
    for i in range(N):
        w=input().split("*")
        pre.append(w[0])
        suf.append(w[-1])
        word+=''.join(w[1:-1])
    p=max(pre,key=lambda x: len(x))
    s=max(suf,key=lambda x: len(x))
    word=p+word+s
    sol=word
    for i in pre:
        if word.startswith(i)==False:
            sol="*"
            print("Case #{}: {}".format(T,sol))
            return
    for i in suf:
        if word.endswith(i)==False:
            sol="*"
            print("Case #{}: {}".format(T,sol))
            return
    print("Case #{}: {}".format(T,sol))

for test_case in range(1,t+1):
    solve(test_case)