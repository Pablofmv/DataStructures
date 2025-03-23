def edit_distance(A,B):
    n = len(A)
    m = len(B)

    D = [[_ for _ in range(0,m+1)] for _ in range(0,n+1)]

    for i in range(0,n+1):
        D[i][0] = i
    
    for j in range(0,m+1):
        D[0][j] = i
    
    for i in range(0,n+1):
        for j in range(0,m+1):
            
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            if A[i-1] == B[j-1]:
                match = D[i-1][j-1]
            else:
                match = D[i-1][j-1] + 1
    
            D[i][j] = min(insertion, deletion, match)

    return D

A = 'kitten'
B = 'sitting'

print(edit_distance(A,B))