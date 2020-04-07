from itertools import combinations as c
from itertools import permutations as p 

t=int(input())
T=dict()
sols=dict()
sols["aa"]="ab ba"
sols["aaa"]="abc cab bca"
sols["abc"]="abc cba bac"
sols["aaaa"]="abdc cabd dcab bdca"
sols["aabb"]="abcd badc cdba dcab"
sols["abcc"]="acdb cbad bdca dabc"
sols["abcd"]="adbc cbda dacb bcad"
sols["aaaaa"]="abcde eabcd deabc cdeab bcdea"
sols["aaabb"]="abcde eabcd bdaec cedba dceab"
sols["aaabc"]="acbde daceb ebacd cdeba bedac"
sols["aabbc"]="abcde daecb cdbea ecabd bedac"
sols["aabcd"]="adcbe caedb debac ebdca bcaed"
sols["abcde"]="aedbc cbead daceb ecbda bdace"
cal="abcde"
def givesol(n,m,T):   # n el tamano matriz, m valor buscado
    flag=0
    S=[s for s in sols.keys() if len(s)==n]
    for s in S:
        k=len(set(s))
        for i in c(range(1,n+1),k):
            for j in p(i):
                x=s
                for v in range(k):
                    x=x.replace(cal[v],str(j[v]))
                if m==eval('+'.join(x)):
                    flag=1
                    break 
            if flag==1:
                break
        if flag==1:
            break
    if flag==0:
        sol="IMPOSSIBLE"
    else:
        sol="POSSIBLE"
    print("Case #{}: {}".format(T,sol))
    if sol=="POSSIBLE":
        t=sols[s]
        for v in range(k):
            t=t.replace(cal[v],str(j[v]))
        rest=list(set(range(1,n+1)).difference(j))
        for v in range(len(rest)):
            t=t.replace(cal[k:][v],str(rest[v]))
        for r in t.split():
            print(" ".join(r))


def solve(T):
    N,K=list(map(int,input().split()))
    givesol(N,K,T)
    

for i in range(1,t+1):
    solve(i)