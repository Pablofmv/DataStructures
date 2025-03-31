def knapsack_wo_repetition(W,weights,values):

    n = len(weights)
    value = [[0 for _ in range(0,n+1)] for _ in range(0,W+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            value[w][i] = value[w][i-1]
            if weights[i-1] <= w:
                value[w][i] = max(value[w][i],value[w - weights[i-1]][i-1] + values[i-1])
    
    return value[W][n]

W = 5
weights = [1,4,5]
values = [1,4,5]

print(knapsack_wo_repetition(W,weights,values))