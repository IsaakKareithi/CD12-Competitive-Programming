# python program to find number of ways
# To make stable tower of given heights

def possibleWays(n, m, k):
    dp = [[0 for i in range(10)]
          for j in range(10)]
    presum = [[0 for i in range(10)]
              for j in range(10)]
    
    # initializing the 0th row to 0 
    for i in range(1, n+1):
        dp[0][i] = 0
        presum[0][i] = 1

    # initializing 0th column to 0
    for i in range(0, m+1):
        dp[i][0] = 1
        presum[i][0] = 1

    # for each from 1 to m 
    for i in range(1, m+1):
        #for each column from 1 to n
        for j in range(1, n+1):
            # intializing dp[i][j] to 
            # presum of (i-1, j)
            dp[i][j] = presum[i-1][j]
            if j > k:
                dp[i][j] -= presum[i-1][j-k-1]

        for j in range(1, n+1):
            presum[i][j] = dp[i][j] + presum[i][j-1]

    return dp[m][n]

# Driver code
n, m, k = 3, 3, 2   

print('Number of ways is: ',possibleWays(n, m, k))
