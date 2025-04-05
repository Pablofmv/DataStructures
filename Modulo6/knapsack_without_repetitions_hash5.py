def knapsack_wo_repetitions_hash(W, weigths, values, n, memo = None):

    if memo is None:
        memo = {}

    key = (W,n)
    if key in memo:
        return memo[key]

    if W <= 0 or n <= 0:
        return 0
    
    exclude = knapsack_wo_repetitions_hash(W,weigths,values, n-1, memo)

    include = 0
    if weigths[n-1] <= W:
        include = knapsack_wo_repetitions_hash(W - weigths[n-1], weigths, values, n-1, memo) + values[n-1]
    
    max_value = max(include,exclude)

    memo[key] = max_value

    return max_value

weigths = [1,3]
values = [2,10]
W = 2
n = len(weigths)
print(knapsack_wo_repetitions_hash(W, weigths, values, n))