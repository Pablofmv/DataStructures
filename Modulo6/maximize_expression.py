def apply_op(a, b, op):

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == 'x':
        return a * b
    else:
        return "Error"
    
def MinAndMax(i,j,d,ops,m,M):

    if i == j:
        return d[i], d[i]
    
    min_val = float("inf")
    max_val = float("-inf")


    for k in range(i,j):
        left_min, left_max = m[i][k], M[i][k]

        right_min, right_max = m[k+1][j], M[k+1][j]

        op = ops[k]

        a = apply_op(left_max, right_max, op)
        b = apply_op(left_max, right_min, op)
        c = apply_op(left_min, right_max, op)
        d = apply_op(left_min, right_min, op)

        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)

    return min_val, max_val

def maximize_expression(d, ops):

    n = len(d)

    if n != len(ops) + 1:
        return "Number of operators must be one less than number of numbers."
    
    m = [[0 for _ in range(0, n)] for _ in range(0,n)]
    M = [[0 for _ in range(0, n)] for _ in range(0,n)]

    for i in range(0, n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    
    for s in range(1,n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, d, ops, m ,M)    
    
    return M[0][n-1]

d = [5,8,7,4,8,9]
ops = ['-','+','x','-','+']
print(maximize_expression(d, ops))
    
