# I will need to obtain all possible combinations and permutations
# of the keys in my sols dict to obtain each possible sum of size n.
from itertools import combinations as c
from itertools import permutations as p 

t=int(input()) #Receive as input the number of test cases.
T=dict()
sols=dict() # Dictionary to add all the possible structures of the matrices
# These lines are basically matrices done by hand that solve the problem 
# in the base case exchanging each letter into an specific value.
# Notice that the keys are the traces of their respective matrix.
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
# This function returns the matrix we want
# n is the size of the matrix
# m the desired value we want to obtain
# T is the test case
def givesol(n,m,T):   
    # pointer to finish evaluation
    flag=0
    # Here I list the keys of the matrices with the size we want. 
    S=[s for s in sols.keys() if len(s)==n]
    # Now we iterate over all the possible solutions.
    for s in S:
        # I get only the letters in the key without repetitions
        k=len(set(s))
        # Now for each combination of k elements from 1 to n
        for i in c(range(1,n+1),k):
            # I will get all permutations from those numbers
            for j in p(i):
                # (Just saved the key I will use in this iteration)
                x=s
                # And I will iterate over those k elements with this loop
                for v in range(k):
                    # And exchange the letters with numbers
                    x=x.replace(cal[v],str(j[v]))
                # to get the sum of those numbers and see if is equal to m
                if m==eval('+'.join(x)):
                    # If it is, I can stop all my iterations with my flag
                    flag=1
                    break 
            # The flag will break the process in case I got an answer
            if flag==1:
                break
        # Same here
        if flag==1:
            break
    # If after all the possible permutations and sums isn't possible
    if flag==0:
        # The solution will be set as IMPOSSIBLE
        sol="IMPOSSIBLE"
    else:
        # Else... well, POSSIBLE
        sol="POSSIBLE"
    # We print the sol variable
    print("Case #{}: {}".format(T,sol))
    # And after the first line, if sol==POSSIBLE we must print the matrix
    if sol=="POSSIBLE":
        # This will be achieved by getting the matrix from the sols dictionary
        t=sols[s]
        # And we will change first the letters in the key in order to keep the 
        # trace with the desired trace
        for v in range(k):
            # Since we didn't change the last permutation (j), so we only have to 
            # change the letters
            t=t.replace(cal[v],str(j[v]))
        # Now we list the numbers that weren't used in the key to continue the filling
        # of the matrix
        rest=list(set(range(1,n+1)).difference(j))
        # So we do the iteration of these elements.
        for v in range(len(rest)):
            t=t.replace(cal[k:][v],str(rest[v]))
        # Now we split the string t, because is a string divided by spaces
        for r in t.split():
            # Finally we join everything between spaces and print it.
            print(" ".join(r))

# This is the main solution
def solve(T):
    # We receive the size of the matrix we want and the value we want it to have
    N,K=list(map(int,input().split()))
    # Now we run a function to create the matrix.
    givesol(N,K,T)
    

for i in range(1,t+1):
    solve(i)

# This solution is extremely large, so I wont explain it with an example.