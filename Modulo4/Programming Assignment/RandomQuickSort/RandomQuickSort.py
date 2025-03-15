def partition3(arr,l,r):

    x = arr[0]
    m1 = l
    m2 = l

    for i in range(l+1,r+1):

        if arr[i] < x:
            m1 += 1
            m2 += 1
            arr[i], arr[m1] = arr[m1], arr[i]

            if m1 != m2:
                arr[i], arr[m2] = arr[m2], arr[i]

        elif arr[i] == x:
            m2 += 1
            arr[i], arr[m2] = arr[m2], arr[i]
    
    arr[l], arr[m1] = arr[m1], arr[l]

    return m1, m2

    

def random_quick_sort(arr,l,r):

    if r < l:
        return 
    
    m1, m2 = partition3(arr,l,r)

    partition3(arr,l,m1-1)
    partition3(arr,m2+1,r)

    return arr

arr = [2,3,9,2,2]
print(random_quick_sort(arr,0,len(arr)-1))