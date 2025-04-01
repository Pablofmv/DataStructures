def knapsak(W, weights, values, n,memo = None):

    if memo is None:
        memo = {}
    
    key = (W,n)
    if key in memo:
        return memo[key]
    
    if W <= 0 or n <= 0:
        return 0
    
    not_take = knapsak(W,weights,values,n-1,memo)

    take =0
    if weights[n-1] <= W:
        take = knapsak(W - weights[n-1], weights, values, n-1, memo) + values[n-1]

    max_value = max(take,not_take)

    memo[key] = max_value

    return max_value

values = [60, 100, 120]
weights = [10,20,30]
W = 50
n = len(values)

print(knapsak(W, weights, values, n))

