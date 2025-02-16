def karatsuba_mult(A,B):
    n = len(A)

    if n == 1:
        return [A[0]*B[0]]
    
    R = [0] * (2 * n)

    half = n // 2

    left_part = karatsuba_mult(A[0:half],B[0:half])
    right_part = karatsuba_mult(A[half:],B[half:])

    A_sum = [A[i] + A[i+half] for i in range(0,half)]
    B_sum = [B[i] + B[i+half] for i in range(0,half)]

    cross_term = karatsuba_mult(A_sum,B_sum)

    for i in range(0,half):
        R[i] += left_part[i] 
        R[i+n] += right_part[i]

        R[i+half] += cross_term[i] - left_part[i] - right_part[i]

    return R

def karatsubamult(A,B):

    n = len(A)

    if n == 1:
        return [A[0] * B[0]]
    
    R = [0] * (n * 2)

    half = n // 2

    left_part = karatsubamult(A[0:half], B[0:half])
    right_part = karatsubamult(A[half:],B[half:])

    A_sum = [A[i] + A[i+half] for i in range(0,half)]
    B_sum = [B[i] + B[i+half] for i in range(0,half)]

    cross_term = karatsubamult(A_sum,B_sum)

    for i in range(0,half):
        R[i] += left_part[i]
        R[i+n] += right_part[i]
        
        R[i+half] += cross_term[i] - left_part[i] - right_part[i]

    return R



A = [1,2,3,4]
B = [4,3,2,1]

print(karatsubamult(A,B))
print(karatsuba_mult(A,B))