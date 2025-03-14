def counting_sort(arr):

    M = max(arr)

    Count = [0] * (M + 1)

    for num in arr:
        Count[num] += 1
    
    Pos = [0] * (M + 1)
    Pos[0] = 0

    for i in range(1,M+1):
        Pos[i] = Pos[i-1] + Count[i-1]
    
    sorted_array = [0] * len(arr)

    for num in arr:
        sorted_array[Pos[num]] = num
        Pos[num] += 1
    
    return sorted_array

A = [0,0,0,0,1,0]
print(counting_sort(A))


