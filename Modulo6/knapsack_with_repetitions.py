def knapsack_with_repetitions(W,weights,values):
    n = len(weights)

    value = [0] * (W + 1)

    for w in range(0,W+1):
        for i in range(0,n):
            if weights[i] <= w:
                val = value[w - weights[i]] + values[i]

                if val > value[w]:
                    value[w] = val

    return value[W]

weights = [5,1]
values = [10,1]
W = 6
print(knapsack_with_repetitions(W,weights,values))