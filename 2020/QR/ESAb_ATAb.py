from math import inf
t,b=list(map(int,input().split()))
flag=0
def inverse(t):
    V=t
    for i in range(len(t)):
        if V[i]=="0":
            V[i]="2"
        if V[i]=="1":
            V[i]="0"
        if V[i]=="2":
            V[i]="1"
    return V

def solve(T,B):
    bits=["X"]*B
    # First step
    for i in range(5):
        print(i+1)
        s=input()
        bits[i]=s
    for i in range(5):
        print(B-i)
        s=input()
        bits[B-i-1]=s
    # To define one of these:    
    reverse_indicator=inf
    inverse_indicator=inf
    # And with a small iteration is possible
    for i in range(5):
        if bits[i]==bits[B-i-1]:
            inverse_indicator=i
            break
    for i in range(5):
        if bits[i]!=bits[B-i-1]:
            reverse_indicator=i
            break
    
    while "X" in bits:
        t=0
        if reverse_indicator<inf:
            print(reverse_indicator+1)
            t+=1
            Lr=input()
            if Lr!=bits[reverse_indicator]:
                # There was a reverse or a switch, but not both.                
                if inverse_indicator==inf:
                    # Since the info obtained until now is unaffected by which action we do, we can just switch
                    bits=bits[::-1]
                else:
                    print(inverse_indicator+1)
                    Li=input()
                    t+=1
                    if Li!=bits[inverse_indicator]:
                        # This will mean there was a switch
                        bits=inverse(bits)
                    else:
                        bits=bits[::-1]
            else:
                # There is no certainty that there was a change or could have done both.
                if inverse_indicator<inf:
                    print(inverse_indicator+1)
                    Li=input()
                    t+=1
                    
                    if Li!=bits[inverse_indicator]:
                        bits=bits[::-1]
                        bits=inverse(bits)
        else:
            # print("VALUES R,I:.....",reverse_indicator,inverse_indicator)
            # If there is no reverse_indicator, this means we MUST HAVE an inverse_indicator
            print(inverse_indicator+1)
            t+=1
            
            Li=input()
            if Li!=bits[inverse_indicator]:
                # This totally means that there was a switch
                bits=inverse(bits)
        if t%2==0:
            while t!=10 and 'X' in bits:
                nb=bits.index('X')
                print(nb+1)
                s1=input()
                bits[nb]=s1
                print(B-nb)
                sm1=input()
                bits[B-nb-1]=sm1
                if reverse_indicator==inf:
                    if s1!=sm1:
                        reverse_indicator=nb
                if inverse_indicator==inf:
                    if s1==sm1:
                        inverse_indicator=nb
                t+=2
                
        else:
            print(B)
            a=input()
            t+=1
            while t!=10 and 'X' in bits:
                nb=bits.index('X')
                print(nb+1)
                s1=input()
                bits[nb]=s1
                print(B-nb)
                sm1=input()
                bits[B-nb-1]=sm1
                if reverse_indicator==inf:
                    if s1!=sm1:
                        reverse_indicator=nb
                if inverse_indicator==inf:
                    if s1==sm1:
                        inverse_indicator=nb
                t+=2
                
    print(''.join(bits))
    ans=input()
    if ans=="Y":
        return
    else:
        flag=1
        return

for i in range(1,t+1):
    solve(i,b)
    if flag==1:
        break