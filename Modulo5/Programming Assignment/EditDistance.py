def edit_distance(A,B):

    n = len(A)
    m = len(B)

    if n == 0:
        return m
    
    if m == 0:
        return n
    
    if A[n-1] == B[m-1]:
        return edit_distance(A[0:n-1],B[0:m-1])
    
    insertion = edit_distance(A,B[0:m-1]) + 1
    deletion = edit_distance(A[0:n-1],B) + 1
    sustitution = edit_distance(A[0:n-1],B[0:m-1]) + 1

    return min(insertion, deletion, sustitution)

A = "short"
B = "ports"

print(edit_distance(A,B))