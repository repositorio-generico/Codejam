#This reduce is to use in chinese_remainder
from functools import reduce

# This functions we copied from a link in medium.com . 
def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod/n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod

def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return int(x1)

# We have 2 9 5 7 11 13 17

t,n,m=list(map(int,input().split()))
# The chinese remainder theorem here is applied over relative primes.
primes=[2,9,5,7,11,13,17]

def solve(T):
    mods=[]
    for i in range(7):
        # I just need to print the same prime number to get the remainder 
        # of the number of gophers to apply the theorem so I build the string 
        # I will send
        p=(str(primes[i])+" ")*18
        # And then print it.
        print(p)
        # Then I get the list or remainders
        m=list(map(int,input().split()))
        # and add it to my list of residues
        mods.append(sum(m)%primes[i])
    # after everything I just apply the theorem and finish
    sol=chinese_remainder(primes,mods)
    sol=int(sol)
    print(sol)
    ans=input()
    # The solution is correct, but I add this in case I failed in something
    if ans=='-1':
        return -1
    else:
        return 1
for i in range(1,t+1):
    m=solve(i)
    if m==-1:
        break 