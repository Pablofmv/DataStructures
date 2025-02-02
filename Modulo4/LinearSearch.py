def LinearSearch(A, low, high, key):
    if high < low:
        return 'NOT_FOUND'
    if A[low] == key:
        return low
    
    return LinearSearch(A,low+1,high,key)


def Fibonnaci(n):

    if n < 0:
        return - 1
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    return Fibonnaci(n-1) + Fibonnaci(n-2)

print(Fibonnaci(6))
print(LinearSearch([1,2,3,4,5],0,4,5))
