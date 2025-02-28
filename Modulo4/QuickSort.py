def partition(A,l,r):

    x = A[l]
    j = l

    for i in range(j+1,r+1):
        if A[i] <= x:
            j += 1
            A[j], A[i] = A[i], A[j]
        
    A[l],A[j] = A[j], A[l]
    
    return j



def quicksort(A, l,r):
    if l >= r:
        return
    
    m = partition(A,l,r)
    quicksort(A,l,m-1)
    quicksort(A,m+1,r)
    return A

A = [6,2,8,4,0]
l = 0
r = len(A) - 1
print(quicksort(A,l,r))