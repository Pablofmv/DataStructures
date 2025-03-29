def knapsack_with_repetitions(W,weights,values):
    n = len(weights)

    value = [0] * (W + 1)

    for w in range(1,W+1):
        for i in range(0,n):
            if weights[i] <= w:
                weight_value = value[w - weights[i]] + values[i]
                if weight_value > value[w]:
                    value[w] = weight_value
        
    return value[W]

weights = [1, 2]
values = [2,3]
W = 3
print(knapsack_with_repetitions(W,weights,values))


        
