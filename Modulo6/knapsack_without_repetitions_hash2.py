def knapsack_wo_repetitions_hash(W,weights,values,n,memo=None):

    if W <= 0 or n <= 0:
        return 0

    if memo is None:
        memo = {}
    
    key = (W,n)
    if key in memo:
        return memo[key]
    
    not_take = knapsack_wo_repetitions_hash(W,weights,values,n-1,memo)

    take = 0
    if weights[n-1] <= W:
        take = knapsack_wo_repetitions_hash(W - weights[n-1],weights,values,n-1,memo) + values[n-1]
    
    max_value = max(not_take, take)

    memo[key] = max_value

    return max_value

values = [60,100,120]
weigths = [10,20,30]
W = 50
n = len(values)

print(knapsack_wo_repetitions_hash(W, weigths, values,n))


