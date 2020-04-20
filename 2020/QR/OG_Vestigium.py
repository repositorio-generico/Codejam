t=int(input()) # We read the number of cases.

def solve(T):
    N=int(input()) # We read the size of the matrix.
    t=0            # Here we save the trace
    r=0            # Number of rows with repeated elements
    c=0            # And number of columns with repeated elements
    M=[]           # Here we will save the matrix.
    for i in range(N):  # The loop for each line of the input case.
        # We make the input (a string of numbers joined by blankspaces) a list of numbers 
        l=list(map(int,input().split())) 
        # We append that line into the matrix in the proper position it must have
        M.append(l)
        # The trace can be seen as the sum of all the i-th elements of the i-th rows.
        t+=l[i]
        # If we make the line a set, the repeated elements will be deleted, so if we "set-ify" the list, 
        # and its length changes, it will mean there are repeated elements 
        if len(set(l))!=N:
            # And if it happens, we add 1 to our number of rows with repeated elements.
            r+=1
    # Now we must do a second check to count the number of columns with repeated elements.
    for i in range(N):
        # Here we should have used a set to optimize addition into S, but I didn't think that in the moment.
        # The idea is to add the elements of the column into S and each time we check an element of M, we 
        # verify if that element is in the column.
        S=[]
        # So we start the loop
        for j in range(N): 
            # If the element we're going to add to S is already in S
            if M[j][i] in S:
                # We add 1 to our column with repeated elements
                c+=1    
                # And we don't need to check more for that column
                break
            else:
                # If it isn't in S, we just add it and continue to the next element in the column.
                S.append(M[j][i])
    # And that's all
    print("Case #{}: {} {} {}".format(T,t,r,c))
for i in range(1,t+1):
    solve(i)

# Example:
# 3
# 1 2 3
# 3 2 2
# 2 1 1

# N=3
# t,r,c=0,0,0               ... Just to avoid so many lines.
# M=[]
# for i in range(3):
#   (i=0)
#   l=list(map(int,'1 2 3'.split()))= list(map(int,['1','2','3']))=list(<generator..>)=[1,2,3] (remember map returns a generator)
#   M.append([1,2,3])         ... M=[[1,2,3]]
#   t+=l[0]=1                 ... t=1
#   if len(set([1,2,3]))!=3   ... here the list doesn't have repeated elements, so has length 3 and is false this part.
#   REPEATING LOOP...(i=1)
#   l=list(map(int,'3 2 2'.split()))= ... [3,2,2]
#   M.append([3,2,2])         ... M=[[1,2,3],[3,2,2]]
#   t+=l[1]=2                 ... t=3
#   if len(set([3,2,2]))!=3   ... here set([3,2,2])=set([3,2]), so this has length 2 and we have to pass through here.
#       r+=1                  ... Updating the number of rows with repeated elements (r=1)
#   REPEATING LOOP...(i=2)
#   l=list(map(int,'2 1 1'.split()))= ... [2,1,1]
#   M.append([2,1,1])         ... M=[[1,2,3],[3,2,2],[2,1,1]]
#   t+=l[2]=1                 ... t=4
#   if len(set([2,1,1]))!=3   ... here set([2,1,1])=set([2,1]), so this has length 2 and we have to pass through here.
#       r+=1                  ... Updating the number of rows with repeated elements (r=2)
#   FINISH LOOP
#   for i in range(3):
#       S=[]
#       for j in range(3):
#           if M[0][0] in S   ... False, since S is empty.
#           else:
#               S.append(M[0][0])= S.append(1) ... Here S=[1]
#       REPEATING LOOP...(j=1)
#           if M[1][0] in S   ... This is 2 in [1], and is False, so continue
#           else:
#               S.append(M[1][0])= S.append(1) ... Here S=[1,2]
#       REPEATING LOOP...(j=2)
#           if M[2][0] in S   ... This is 3 in [1,2], and is False, so continue
#           else:
#               S.append(M[2][0])= S.append(1) ... Here S=[1,2,3]
#       FINISH LOOP
#   REPEATING LOOP...(i=1)
#       S=[]
#       for j in range(3):
#           if M[0][1] in S   ... False, since S is empty.
#           else:
#               S.append(M[0][1])= S.append(2) ... Here S=[2]
#       REPEATING LOOP...(j=1)
#           if M[1][1] in S   ... This is 2 in [2], and is True
#               c+=1          ... We add 1 to our number of columns with repeated numbers (c=1)
#               break         ... We break this loop since we found what we wanted to know.
#       FINISH LOOP
#   REPEATING LOOP...(i=2)
#       S=[]
#       for j in range(3):
#           if M[0][2] in S   ... False, since S is empty.
#           else:
#               S.append(M[0][2])= S.append(3) ... Here S=[3]
#       REPEATING LOOP...(j=1)
#           if M[1][2] in S   ... This is 2 in [3], and is False, so continue
#           else:
#               S.append(M[1][2])= S.append(2) ... Here S=[3,2]
#       REPEATING LOOP...(j=2)
#           if M[2][1] in S   ... This is 1 in [3,2], and is False
#           else:
#               S.append([2][1])= S.append(1) ... Jere S=[3,2,1]
#       FINISH LOOP
#   After finishing everything, we have the values we need: t=4, r=2, c=1
