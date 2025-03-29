def edit_distance(A,B):

    n = len(A)
    m = len(B)

    dp = [[0 for _ in range(0,m+1)] for _ in range(0,n+1)]

    for i in range(0,n+1):
        dp[i][0] = i
    
    for j in range(0,m+1):
        dp[0][j] = j

    for i in range(1,n+1):
        for j in range(1,m+1):
            insertion = dp[i][j-1] + 1
            deletion = dp[i-1][j] + 1

            if A[i-1] == B[j-1]:
                match = dp[i-1][j-1]
            else:
                match = dp[i-1][j-1] + 1
            
            dp[i][j] = min(insertion, deletion, match)
    
    return dp[n][m]

A = "Cat"
B = "Cate"

print(edit_distance(A,B))