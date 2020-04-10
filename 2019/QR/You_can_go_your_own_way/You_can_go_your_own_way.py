t=int(input())

for i in range(t):
    N=int(input())
    path=input()
    inv_path=''
    for j in path:
        if j=='E':
            inv_path+='S'
        else:
            inv_path+='E'
    print(f"Case #{i+1}: {inv_path}")