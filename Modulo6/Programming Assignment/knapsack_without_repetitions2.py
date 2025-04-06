def knapsack_wo_repetitions(W, weigths, values):

    n = len(weigths)

    dp = [[0 for _ in range(0,n+1)] for _ in range(0,W+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):

            exclude = dp[w][i-1]

            include = 0
            if weigths[i-1] <= w:
                include = dp[w - weigths[i-1]][i-1] + values[i-1]
            
            max_value = max(exclude,include)

            dp[w][i] = max_value
    
    return dp[W][n]

W = 10
weigths = [1,4,8]
values = [1,4,8]
print(knapsack_wo_repetitions(W, weigths, values))
