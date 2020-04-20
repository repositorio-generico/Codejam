t=int(input()) # We receive the number of cases we will solve.

def solve(T): # Main function that solves the problem.
    S=input() # We receive the chain of numbers that we need to put the brackets.
    t=""      # Here we will build our new chain.
    '''
     I add p_right to know which is the number of 
     left ('s I have at the moment to know if the next 
     number will be able to be inside of this bracket or I will 
     need to close some of them to stay in it level.

     For example, if I have 131, the way I build will be (1((3))1),
     so when I'm at 13, I will be (1((3, and I will have to close two
     brackets to let the next 1.
    '''
    p_right=0 
    # Now I'm ready to check the string
    for i in range(len(S)):
        # I get the string and parse it into an int
        s=int(S[i])
        # If the number is smaller than my number of open brackets,
        if s<p_right: 
            # I need to close p_right-s left brackets to add it.
            t+=")"*(p_right-s) 
            # But my number of OPEN brackets will be the actual number I added
            p_right=s 
        # In the other case if the number is bigger than my number of open brackets  
        if s>p_right: 
            # I will have to open s-p_right brackets and add them to the string.
            t+="("*(s-p_right) 
            # And my new number of open brackets will be the last number I added
            p_right=s
        # After adding the number of brackets needed, I add the number. 
        t+=S[i] 
    #Finally, when I finish checking all the inputed string I will close the rest of open brackets. 
    t+=")"*p_right 
    # And finish printing.
    print("Case #{}: {}".format(T,t)) 

for i in range(1,t+1):
    solve(i)

# Example for case 2020:
# S='2020' (here clearly len(S)=4)
# t=''
# p_right=0

# for i in range(4):
#   s=int(S[0])=int('2')=2
#   if s<p_right (2<0):    ... 2<0 is False, so continue
#   if s>p_right (2>0):
#       t+='('*(2-0)       ... Here t=''+'(('='(('
#       p_right=2
#   t+=S[0]='2'            ... Here t='(('+'2'= '((2'

# Now i=1
#   s=int(S[1])=int('0')=0
#   if 0<2:
#       t+=')'*(2-0)       ... Here t='((2'+'))'= '((2))'
#       p_right=0
#   if 0>2:                ... False, so continue 
#   t+=S[1]='0'            ... Here t='((2))'+'0'= '((2))0'

# Now i=2
#   s=int(S[2])=int('2')=2
#   if s<p_right (2<0):    ... 2<0 is False, so continue
#   if s>p_right (2>0):
#       t+='('*(2-0)       ... Here t='((2))0'+'(('='((2))0(('
#       p_right=2
#   t+=S[0]='2'            ... Here t='((2))0(('+'2'= '((2))0((2'

# Now i=3
#   s=int(S[3])=int('0')=0
#   if s<p_right (0<2):
#       t+=')'*(2-0)       ... Here t='((2))0((2'+'))'= '((2))0((2))'
#       p_right=0
#   if s>p_right (0>2):    ... False 
#   t+=S[1]='0'            ... Here t='((2))'+'0'= '((2))0((2))0'

# The loop ends and we have the solution.
