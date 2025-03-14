def count_sort(arr):

    M = max(arr)

    Count = [0] * (M + 1)

    for num in arr:
        Count[num] += 1

    Pos = [0] * (M + 1)
    Pos[1] = 1

    for j in range(2,M+1):
        Pos[j-1] = Pos[j] + Count[j-1]
    
    sorted_array = [0] * len(arr)

    for num in arr:
        sorted_array[Pos[num] - 1] = num
        Pos[num] += 1
    
    return sorted_array

    
print(count_sort([3,3,2,4]))