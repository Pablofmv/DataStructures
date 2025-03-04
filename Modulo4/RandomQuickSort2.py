import random

def partition(A,l,r):

    x = A[l]
    j = l

    for i in range(l+1,r+1):
        if A[i] <= x:
            j += 1
            A[j],A[i] = A[i],A[j]
    
    A[l], A[j] = A[j], A[l]

    return j


def random_quick_sort(A,l,r):

    if l >= r:
        return
    
    k = random.randint(l,r)
    A[l],A[k] = A[k],A[l]

    m = partition(A,l,r)

    random_quick_sort(A,l,m-1)
    random_quick_sort(A,m+1,r)

    return A

A = [10,7,8,9,1,5]
l = 0
r = len(A) - 1

print(random_quick_sort(A,l,r))