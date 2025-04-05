def knapsack_without_repetitions_has(W,weights,values,n,memo = None):

    if W ==0 or n ==0:
        return 0

    if memo is None:
        memo = {}

    key = (W,n)
    if key in memo:
        return memo[key]
    
    exclude = knapsack_without_repetitions_has(W,weights,values, n-1,memo)

    include = 0
    if weights[n-1] <= W:
        include = knapsack_without_repetitions_has(W - weights[n-1],weights, values, n-1, memo) + values[n-1]
    
    max_value = max(exclude, include)

    memo[key] = max_value

    return max_value


values = [100,120,60]
weigths = [20,30,10]
W = 50
n = len(values)
print(knapsack_without_repetitions_has(W,weigths,values,n,memo=None))
    
