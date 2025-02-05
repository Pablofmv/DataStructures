def MultPolu(A,B,n):
    product = [0] * (2 * n - 1)
    n = len(A)

    for i in range(0,n):
        for j in range(0,n):
            product[i + j] = product[i + j] + A[i] * B[j]    

    return product

print(MultPolu([3,4],[1,2],2))