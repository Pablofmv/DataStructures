def SelectionSort(A):
    n = len(A)

    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if A[min_index] > A[j]:
                min_index = j
        
        A[i], A[min_index] = A[min_index], A[i]
    
    return A


print(SelectionSort([7,6,5,4,3,2,1,8]))