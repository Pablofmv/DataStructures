def mult2(A,B,n,aI,bI):
    if n == 1:
        return [A[aI]*B[bI]]
    
    R = [0] * (2 * n)

    half = n // 2

    left_part = mult2(A,B,half, aI, bI)
    right_part = mult2(A,B,half,aI+half, bI+half)
    cross1 = mult2(A,B,half,aI, bI+half)
    cross2 = mult2(A,B,half,aI+half,bI)

    for i in range(0,half):
        R[i] = left_part[i]
        R[i + n] = right_part[i]
        R[i + half] += cross1[i] + cross2[i]
    
    return R


def mult2B(A,B,n,aI,bI):

    if n == 1:
        return [A[aI]*B[bI]]
    
    R = [0] * (2 * n)

    half = n // 2

    left_part = mult2B(A,B,half,aI,bI)
    right_part =mult2B(A,B,half,aI+half,bI+half)
    cross1 = mult2B(A,B,half,aI,bI+half)
    cross2 = mult2B(A,B,half,aI+half,bI)

    for i in range(0,half):
        R[i] = left_part[i]
        R[i+n] = right_part[i]
        R[i+half] = cross1[i] + cross2[i]
    
    return R
    

A = [1,2]
B = [3,4]
n = len(A)
print(mult2B(A,B,n,0,0))

A = [1,2]
B = [3,4]
n=len(A)


print(mult2(A,B,n,0,0))
