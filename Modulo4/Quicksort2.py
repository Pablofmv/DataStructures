def partition(arr,l,r):

    x = arr[l]
    j = l

    for i in range(l+1,r+1):
        if arr[i] <= x:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[l],arr[j] = arr[j], arr[l]

    return j    

def quick_sort(arr,l,r):
    if l >= r:
        return
    
    m = partition(arr,l,r)

    quick_sort(arr,l,m-1)
    quick_sort(arr,m+1,r)

    return arr

A = [6, 2, 8, 4, 0]
l = 0
r =len(A) - 1

print(quick_sort(A,l,r))
