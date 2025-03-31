def knapsack_w_repetitions(W,weigths,values):

    n = len(weigths)

    max_values = [0] * (W + 1)

    for w in range(1,W+1):
        for i in range(1,n+1):

            if weights[i-1] <= w:
                value = max_values[w-weights[i-1]] + values[i-1]

                if value > max_values[w]:
                    max_values[w] = value
    
    return  max_values[W]


W = 3
weights = [1,2]
values = [2,3]
print(knapsack_w_repetitions(W,weights,values))