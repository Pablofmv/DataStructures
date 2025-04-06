def apply_op(a, b, op):

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == 'x':
        return a * b
    else:
        return "Wrong operation."
    

def min_and_max(i,j,m,M,d,ops):

    if i == j:
        return d[i], d[i]
    
    min_value = float("inf")
    max_value = float("-inf")

    for k in range(i,j):

        left_min, left_max = m[i][k], M[i][k]
        right_min, right_max = m[k+1][j], M[k+1][j]

        op = ops[k]

        a = apply_op(left_min, right_min, op)
        b = apply_op(left_min, right_max, op)
        c = apply_op(left_max, right_min, op)
        d = apply_op(left_max, right_max, op)

        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    
    return min_value, max_value


def maximize_expression(d,ops):

    n = len(d)

    if n != len(ops) + 1:
        return "number of operations + 1 must be equal to quantity of numbers"
    
    m = [[0 for _ in range(0,n)] for _ in range(0,n)]
    M = [[0 for _ in range(0,n)] for _ in range(0,n)]

    for i in range(0,n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    
    for s in range(1,n):
        for i in range(0,n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i,j,m,M,d,ops)
    
    return M[0][n-1]

d = [1, 2, 3]
ops = ["+","x"]

print(maximize_expression(d,ops))

    