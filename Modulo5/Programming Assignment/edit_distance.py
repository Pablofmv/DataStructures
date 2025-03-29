def edit_distance(first_string, second_string):

    n = len(first_string)
    m = len(second_string)
    
    dp = [[0 for _ in range(0,m+1)] for _ in range(0,n+1)]
    
    for i in range(0,n+1):
        dp[i][0] = i
    
    for j in range(0,m+1):
        dp[0][j] = j
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            deletion = dp[i-1][j] + 1
            insertion = dp[i][j-1] + 1

            if first_string[i-1] == second_string[j-1]:
                match = dp[i-1][j-1]
            else:
                match = dp[i-1][j-1] + 1
            
            dp[i][j] = min(deletion,insertion,match)
    
    return dp[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
