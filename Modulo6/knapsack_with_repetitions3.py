def knapsack_with_repetitions(W,weights,values):
    n = len(weights)

    max_values = [0] * (W +1)

    for w in range(0,W+1):
        for i in range(0,n):
            if weights[i] <= w:
                value = max_values[w - weights[i]] + values[i]

                if value > max_values[w]:
                    max_values[w] = value

    return max_values[W]

W = 3
weights = [1,2]
values = [2,3]
print(knapsack_with_repetitions(W,weights,values))