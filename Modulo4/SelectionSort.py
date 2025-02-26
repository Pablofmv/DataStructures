def SelectionSort(A):
    n = len(A)

    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if A[min_index] > A[j]:
                min_index = j
        
        A[i], A[min_index] = A[min_index], A[i]
    
    return A

def selection_sort(arr):

    n = len(arr)

    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index] , arr[i]
    
    return arr

def select_sort(arr):

    n = len(arr)

    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr



print(select_sort([7,6,5,4,3,2,1,8]))
print(selection_sort([7,6,5,4,3,2,1,8]))
print(SelectionSort([7,6,5,4,3,2,1,8]))