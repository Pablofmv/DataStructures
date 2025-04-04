def apply_op(a, b, op):

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == 'x':
        return a * b
    else:
        return "Wrong op"

def min_and_max(i, j, m, M, d, ops):

    if i == j:
        return d[i], d[i]
    
    min_val = float("inf")
    max_val = float("-inf")

    for k in range(i,j):

        op = ops[k]

        left_min, left_max = m[i][k], M[i][k]
        right_min, right_max = m[k+1][j], M[k+1][j]

        a = apply_op(left_min, right_min, op)
        b = apply_op(left_min, right_max, op)
        c = apply_op(left_max, right_min, op)
        d = apply_op(left_max, right_max, op)

        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)

    return min_val, max_val


def maximize_expression(d, ops):

    n = len(d)

    if n != len(ops) + 1:
        return "total numbers should be equal to operation numbers + 1"
    
    m = [[0 for _ in range(0,n)] for _ in range(0, n)]
    M = [[0 for _ in range(0,n)] for _ in range(0, n)]

    for i in range(0,n):
        m[i][i] = d[i]
        M[i][i] = d[i]

    for s in range(1,n):
        for i in range(0,n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, m, M, d, ops)

    return M[0][n-1]

d = [10, 2, 5]
ops = ['+', "x"]
print(maximize_expression(d, ops))

