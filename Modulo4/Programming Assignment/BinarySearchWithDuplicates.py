def binary_search_duplicate(A,low,high,key):

    if not A:
        return -1
    
    if high < low:
        return low - 1
    
    mid = low + (high -low)//2

    if A[mid] == key:
        return mid
    elif key < A[mid]:
        return binary_search_duplicate(A,low,mid-1,key)
    else:
        return binary_search_duplicate(A,mid+1,high,key)

def binary_search_duplicate2(A,low,high,key):

    if not A:
        return -1
    
    if high < low:
        return low -1
    
    mid = low + (high -low) // 2

    if A[mid] == key:
        return mid
    elif key < A[mid]:
        return binary_search_duplicate2(A,low,mid -1,key)
    else:
        return binary_search_duplicate2(A,mid+1,high,key)
    
def binary_search_duplicate3(A,low,high,key):

    if not A:
        return -1
    
    if high < low:
        return low - 1
    
    mid = low + (high - low)//2

    if A[mid] == key:
        return mid
    elif key < A[mid]:
        return binary_search_duplicate3(A,low, mid-1,key)
    else:
        return binary_search_duplicate3(A,mid+1,high,key)

def binary_search_duplicate4(A,low,high,key):

    if not A:
        return -1
    
    if high < low:
        return low - 1
    
    mid = low + (high - low) // 2

    if A[mid] == key:
        return mid
    elif key < A[mid]:
        return binary_search_duplicate4(A,low,mid -1,key)
    else:
        return binary_search_duplicate4(A,mid+1,high,key)

def binary_search_duplicate5(A,low,high,key):

    if not A:
        return -1
    
    if high < low:
        return -1
    
    mid = low + (high - low) // 2

    if A[mid] == key:

        if mid == 0 or A[mid-1]<key:
            return mid
        else:
            return binary_search_duplicate5(A,low,mid-1,key)
        
    elif key < A[mid]:
        return binary_search_duplicate5(A,low,mid-1,key)
    else:
        return binary_search_duplicate5(A,mid+1,high,key)
    
def binary_search_duplicates6(A,low,high,key):

    if not A:
        return -1
    
    if high < low:
        return -1
    
    mid = low + (high - low) // 2

    if A[mid] == key:

        if mid ==0 or A[mid -1] < key:
            return mid
        else:
            return binary_search_duplicates6(A,low,mid-1,key)
    
    elif key < A[mid]:
        return binary_search_duplicates6(A,low,mid-1,key)
    else:
        return binary_search_duplicates6(A,mid +1,high,key)
    
def binary_search_duplicates7(A,key):
    
    def binary_search_duplicates8(A,low,high,key):
        if high < low:
            return -1
    
        mid = low + (high -low) // 2

        if A[mid] == key:
            if mid == 0 or A[mid-1]<key:
                return mid
            else:
                return binary_search_duplicates8(A,low,mid-1,key)
        
        elif key < A[mid]:
            return binary_search_duplicates8(A,low,mid-1,key)
        else:
            return binary_search_duplicates8(A,mid+1,high,key)
    
    if not A:
        return -1
    
    return binary_search_duplicates8(A,0,len(A)-1,key)

def binary_search_duplicates9(A,key):
    def binary_search_duplicates10(A,low,high,key):

        if high < low:
            return -1

        mid = low + (high -low) // 2

        if A[mid] == key:

            if mid == 0 or A[mid -1] < key:
                return mid
            else:
                return binary_search_duplicates10(A,low,mid-1,key)
        elif key < A[mid]:
            return binary_search_duplicates10(A,low,mid-1,key)
        else:
            return binary_search_duplicates10(A,mid+1,high,key)
    
    if not A:
        return -1
    
    return binary_search_duplicates10(A,0,len(A)-1,key)


    
    
A = [1,3,3,5,7]
print(binary_search_duplicates9(A,5))

    