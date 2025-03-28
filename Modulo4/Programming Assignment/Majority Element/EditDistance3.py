def edit_distance(A,B):

    n = len(A)
    m = len(B)

    if n == 0:
        return m
    if m ==0:
        return n
    
    if A[n-1] == B[m-1]:
        return edit_distance(A[:n-1],B[:m-1])
    
    insert = 1 + edit_distance(A,B[:m-1])
    delete = 1 + edit_distance(A[:n-1],B)
    substitution = 1 + edit_distance(A[:n-1],B[:m-1])

    return min(insert,delete,substitution)

A = "short"
B = "ports"

print(edit_distance(A,B))
