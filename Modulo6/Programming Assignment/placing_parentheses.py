def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(d, ops, m, M, i ,j):

    if i == j:
        m[i][j], M[i][j] = d[i], d[i]

    min_val = float("inf")
    max_val = float("-inf")
    
    for k in range(i,j):

        min_left, max_left = m[i][k], M[i][k]
        min_right, max_right = m[k+1][j], M[k+1][j]

        op = ops[k]

        a = evaluate(min_left, min_right, op)
        b = evaluate(min_left, max_right, op)
        c = evaluate(max_left, min_right, op)
        d = evaluate(max_left, max_right, op)

        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)

    return min_val, max_val

def maximum_value(dataset):
    # write your code here
    items = list(dataset)
    n = len(items)
    d = []
    ops = []

    for i in range(0,n):
        if i % 2 == 0:
            d.append(items[i])
        else:
            ops.append(items[i])
    
    d = list(map(int,d))

    n = len(d)

    if n != len(ops) + 1:
        return "Error"
    
    m = [[0 for _ in range(0,n)] for _ in range(0,n)]
    M = [[0 for _ in range(0,n)] for _ in range(0,n)]

    for i in range(0,n):
        m[i][i] = d[i]
        M[i][i] = d[i]

    for s in range(1,n):
        for i in range(0,n-s):
            j = i + s

            m[i][j], M[i][j]= min_and_max(d, ops, m, M, i, j)
            

    return M[0][n-1]


if __name__ == "__main__":
    print(maximum_value(input()))
