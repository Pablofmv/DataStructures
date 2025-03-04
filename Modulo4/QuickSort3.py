def partition(A,l,r):
    
    x = A[l]
    j = l

    for i in range(l+1,r+1):
        if A[i] <= x:
            j += 1
            A[i], A[j] = A[j], A[i]
        
    
    A[l], A[j] = A[j], A[l]

    return j  

def quick_sort(A,l,r):

    if l >= r:
        return

    m = partition(A,l,r)

    quick_sort(A,l,m-1)
    quick_sort(A,m+1,r)

    return A

A = [6,2,8,4,0]
l = 0
r = len(A)

print(quick_sort(A,l,r-1))







