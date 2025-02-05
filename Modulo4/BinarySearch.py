def BinarySearch(A,low,high,key):

    if not A:
        return -1
    
    if high < low:
        return low - 1
    mid = low + (high - low) // 2

    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return BinarySearch(A,low,mid - 1,key)
    else:
        return BinarySearch(A,mid +1, high,key)

def BinarySearch(A,low,high,key):

    if not A:
        return -1
    
    if high < low:
        return low - 1
    
    mid = low + (high - low) // 2

    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return BinarySearch(A,low,mid - 1,key)
    else:
        return BinarySearch(A,mid +1,high,key)


def BinarySearch2(A, low, high, key):

    if not A:
        return -1
    
    if high < low:
        return low - 1

    
    mid = low + (high - low) // 2

    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return BinarySearch(A,low,mid - 1,key)
    else:
        return BinarySearch(A,mid + 1,high,key)


def BinarySearchIt(A,low,high,key):
    while low <= high:
        mid = low + (high - low) // 2

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1
        
print(BinarySearchIt([1,2,3,4],0,3,4))
print(BinarySearch2([1,2,3,4],0,3,4))