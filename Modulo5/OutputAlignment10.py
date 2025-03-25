def edit_distance(A,B):

    n = len(A)
    m = len(B)

    D = [[0 for _ in range(0,m+1)] for _ in range(0,n+1)]

    for i in range(0,n+1):
        D[i][0] = i

    for j in range(0,m+1):
        D[0][j] = j

    for i in range(1,n+1):
        for j in range(1,m+1):

            insertion = D[i][j-1] +1
            deletion = D[i-1][j-1] + 1

            if A[i-1] == B[i-1]:
                match = D[i-1][j-1]
            else:
                match = D[i-1][j-1] + 1
            
            D[i][j] = min(insertion, deletion, match)
    
    return D



def output_alignment(i,j,A,B,D):

    if i == 0 and j == 0:
        return
    if i > 0 and D[i][j] == D[i-1][j] +1:
        output_alignment(i-1,j,A,B,D)
        print(f"{A[i-1]}\n-")
    elif j > 0 and D[i][j] == D[i][j-1] +1:
        output_alignment(i,j-1,A,B,D)
        print(f"-\n{B[j-1]}")
    else:
        output_alignment(i-1,j-1,A,B,D)
        print(f"{A[i-1]}\n{B[j-1]}")

A = "cat"
B = "cate"
D = edit_distance(A,B)
print(output_alignment(len(A),len(B),A,B,D))
