def knapsack_wo_repetitions_hash(W, weights, n, memo = None):

    if memo is None:
        memo = {}
    
    key = (W,n)
    if key in memo:
        return memo[key]

    if W <= 0 or n <= 0:
        return 0
    
    exclude = knapsack_wo_repetitions_hash(W, weights, n-1, memo)

    include = 0
    if weights[n-1] <= W:
        include = knapsack_wo_repetitions_hash(W - weights[n-1], weights, n-1, memo) + weights[n-1]

    max_value = max(include,exclude)

    memo[key] = max_value

    return max_value

W = 10
weigths = [1, 4, 8]
n = len(weigths)
print(knapsack_wo_repetitions_hash(W, weigths, n))