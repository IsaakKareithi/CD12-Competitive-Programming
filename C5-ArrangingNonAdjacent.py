#python program to count the no. of ways to
# arrange three types of balls succh that
# no 2 balls of same type are adjacent 

MAX = 100

# tABLE TO STORE results of subproblems
dp = [[[[-1] * 4 for i in range(MAX)]
                for j in range(MAX)]
                for k in range(MAX)];

# Retrun count for arrangements where last
# place ball is 'last'. 'last' is 0 for P,
# 1 for p and 2 for r 

def countWays(p, q, r, last):
    # if number of balls of any colour is less
    # than 0, the number of ways pf arrangement is 0
    if (p < 0 or q<0 or r<0):
        return 0;

    # If the last ball required is p and the number
    # of balls of p is 1 while number of balls of 
    # other colours is 0, the number is always 1

    if (p==1 and q==0 and r==0 and last==0):
        return 1;

    # Same case as above for r and s 
    if (p==0 and q==1 and r==0 and last==0):
        return 1;
    if (p==0 and q==0 and r==1 and last==0):
        return 1;

    #If this subrpoblem is reevaluated:
    if (dp[p][q][r][last] != -1):
        return dp[p][q][r][last];

    # If last ball reqquired is P and the number 
    # of ways is the sum of the number of ways to form
    # sequence with 'p-1' P balls, q Q balls 
    # and r R balls with ending with Q and R 
    if (last==0):
        dp[p][q][r][last] = (countWays(p-1, q, r, 1) + 
                             countWays(p-1, q, r, 2));

    # same as above case for q and r
    elif (last==1):
        dp[p][q][r][last] = (countWays(p, q-1, r, 0) + 
                             countWays(p, q-1, r, 2));

    else: #(last==2)
        dp[p][q][r][last] = (countWays(p, q, r-1, 0) + 
                             countWays(p, q, r-1, 1));

    return dp[p][q][r][last];

# Return count of required arrangements 
def countUtil(p, q, r):

    # Three cases arise
    # last required ball is type P
    # last required ball is type Q
    # last required ball is type R
    return (countWays(p, q, r, 0)+
            countWays(p, q, r, 1)+
            countWays(p, q, r, 2));

# Driver code 
p, q, r = 1, 1, 1;
print(countUtil(p, q, r));