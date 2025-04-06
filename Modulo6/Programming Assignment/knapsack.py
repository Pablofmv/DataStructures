from sys import stdin


def maximum_gold(capacity, weights):

    n = len(weights)

    dp = [[0 for _ in range(0, n+1)] for _ in range(0,capacity+1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):

            exclude = dp[w][i-1]

            include = 0
            if weights[i-1] <= w:
                include = dp[w-weights[i-1]][i-1] + weights[i-1]

            max_value = max(include, exclude)

            dp[w][i] = max_value

    return dp[capacity][n]


if __name__ == '__main__':
# Read first line: capacity and n
    line1 = stdin.readline().strip()
    input_capacity, n = map(int, line1.split())
    
    # Read second line: weights
    line2 = stdin.readline().strip()
    input_weights = list(map(int, line2.split()))
    
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))
