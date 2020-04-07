import numpy as np
t=int(input())
def solve(T):
    H_div=[] # Number of @ for each horizontal line.
    V_div=[] # Number of @ for each vertical line.
    T_chips=0
    table=[]
    R,C,H,V=list(map(int,input().split()))
    for ntv in range(R):
        line=list(input())
        T_chips+=line.count('@')
        table.append(line)
    table=np.array(table)
    if T_chips%(H+1)*(V+1)!=0:
        print("Case #{}: {}".format(T,"IMPOSSIBLE"))
        return 0
    else:
        if T_chips==0:
            print("Case #{}: POSSIBLE".format(T))
            return 0
        h_chips=T_chips//(H+1)
        v_chips=T_chips//(V+1)
        sec_chips=T_chips//((H+1)*(V+1))
        h_cuts=[]
        v_cuts=[]
        pointer=0
        for i in range(R):
            if np.count_nonzero(table[pointer:i,:]=='@')==h_chips:
                h_cuts.append(i)
                pointer=i
            if len(h_cuts)==H:
                break
        pointer=0
        for i in range(C):
            if np.count_nonzero(table[:,pointer:i]=='@')==v_chips:
                v_cuts.append(i)
                pointer=i
            if len(v_cuts)==V:
                break
        if len(h_cuts)!=H or len(v_cuts)!=V:
            print("Case #{}: {}".format(T,"IMPOSSIBLE"))
            return 0    
        else:
            h_cuts.append(R)
            v_cuts.append(C)
            h_p=0
            for i in h_cuts:
                v_p=0
                for j in v_cuts:
                    if np.count_nonzero(table[h_p:i,v_p:j]=='@')!=sec_chips:
                        print("Case #{}: {}".format(T,"IMPOSSIBLE"))
                        return 0
                    v_p=j
                h_p=i
        print("Case #{}: {}".format(T,"POSSIBLE"))
        return 

            

#    print("Case #{}: {}".format(T,sol))

for i in range(1,t+1):
    solve(i)