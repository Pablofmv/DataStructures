def knapsack_wo_repetions(W,weights,values):
    n = len(weights)

    dp = [[0 for _ in range(0,n+1)] for _ in range(0,W+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):

            dp[w][i] = dp[w][i-1]

            if weights[i - 1] <= w:
                dp[w][i] = max(dp[w][i],dp[w-weights[i - 1]][i-1] + values[i-1])

    return dp[W][n]

weights = [1,2]
values = [2,3]
W = 3

print(knapsack_wo_repetions(W,weights,values))