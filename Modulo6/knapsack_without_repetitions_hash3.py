def knapsack_wo_repetitions_hash(W,weigths,values,n,memo=None):

    if W == 0 or n == 0:
        return 0
    
    if memo is None:
        memo = {}
    
    key = (W,n)
    if key in memo:
        return memo[key]
    
    exclude = knapsack_wo_repetitions_hash(W,weigths,values,n-1,memo)

    include = 0
    if weigths[n-1] <= W:
        include = knapsack_wo_repetitions_hash(W - weigths[n - 1],weigths,values,n-1,memo) + values[n-1]
    
    max_value = max(exclude,include)

    memo[key] = max_value

    return memo[key]

values = [100,120,60]
weigths = [20,30,10]
W = 50
n = len(values)
print(knapsack_wo_repetitions_hash(W,weigths,values,n,memo=None))


