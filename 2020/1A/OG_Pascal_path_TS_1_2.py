t=int(input())

def solve(T):
    N=int(input())
    if N==1:
        print("Case #{}:".format(T))
        print("1 1")
        return 
    if N==2:
        print("Case #{}:".format(T))
        print("1 1")
        print("2 2")
        return 
    if N==3:
        print("Case #{}:".format(T))
        print("1 1")
        print("2 1")
        print("2 2")
        return 
    else:
        # In other case, I will start quitting the 1 I must put because I start in 1 1
        print("Case #{}:".format(T))
        print("1 1")
        N-=1
        i=2
        # And the process I will follow is to get the closest value of m such that 
        # the difference between the sum from 1 to m and n is the lowest, and then 
        # just add 1's until achieve N. 
        while N!=0:
            # So we add i-1 if N is greater than it
            if N>i-1:
                N-=i-1
                # And print the second element in the (i-1)-th floor (that is i-1)
                print(str(i)+" 2")
                i+=1
            else:
                break
        # If the value of i-1 is greater than N, then we just walk in the border
        if N!=0:
            while N!=0:
                # And this will just quit 1 by 1 until get N==0
                N-=1
                print(str(i-1)+" 1")
                i+=1
        return 

for test_Case in range(1,t+1):
    solve(test_Case)