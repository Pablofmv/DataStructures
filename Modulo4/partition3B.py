import random

def partition3(A,l,r):

    x = A[l]
    m1 = l
    m2 = l

    for i in range(l+1,r+1):

        if A[i] < x:
            m1 += 1
            m2 += 1
            A[i], A[m1] = A[m1], A[i]
            if m1 != m2:
                A[i], A[m2] = A[m2], A[i]

        elif A[i] == x:
            m2 += 1
            A[i], A[m2] = A[m2], A[i]
    
    A[l], A[m1] = A[m1], A[l]

    return m1, m2


def random_quick_sort(A,l,r):

    if l >= r:
        return 
    
    k = random.randint(l,r)
    A[l], A[k] = A[k], A[l]

    m1, m2 = partition3(A,l,r)

    random_quick_sort(A,l,m1-1)
    random_quick_sort(A,m2+1,r)

    return A

A = [4,2,4,1]
print(random_quick_sort(A,0,len(A)-1))