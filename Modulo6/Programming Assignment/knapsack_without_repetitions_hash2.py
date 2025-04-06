def knapsak_wo_repetitions_hash(W, weights, values, n, memo=None):

    if memo is None:
        memo = {}
    
    if W <= 0 or n == 0:
        return 0
    
    if W in memo:
        return memo[W]
    
    exclude = knapsak_wo_repetitions_hash(W, weights, values, n-1, memo)

    include = 0 
    if weights[n-1] <= W:
        include = knapsak_wo_repetitions_hash(W - weights[n-1], weights, values, n-1, memo) + values[n-1]

    max_value = max(exclude,include)

    return max_value

W = 10
weights = [1, 4,8]
values = [1, 4, 8]
n = len(weights)
print(knapsak_wo_repetitions_hash(W, weights, values, n, memo=None))
