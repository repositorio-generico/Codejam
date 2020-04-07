# Since time before the problem had to be opened and then solved
# The first thing is to read the file.

G="sol.txt"
ans=open(G,'w')
R=[]
with open(r'A-large-practice.in','rt') as file:
	for line in file:
		R.append([int(i) for i in line.split()])
t=R.pop(0)[0]
print(t)
for T in range(1,t+1):
    l=R.pop(0)[0]
    X=R.pop(0)
    Y=R.pop(0)
    X.sort()
    Y.sort()
    s=0
    for i in range(l):
        s+=X[i]*(Y[::-1][i])
    ans.write("Case #{}: {}".format(T,s))
    ans.write('\n')
ans.close()