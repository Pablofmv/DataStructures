def counting_sort(arr):

    M = max(arr)

    Count = [0] * (M + 1)

    for num in arr:
        Count[num] += 1
    
    Pos = [0] * (M + 1)
    Pos[1] = 1

    for j in range(2,M + 1):
        Pos[j] = Pos[j - 1] + Count[j - 1]

    sorted_array = [0] * len(arr)

    for num in arr:
        sorted_array[Pos[num] - 1] = num
        Pos[num] += 1
    
    return sorted_array

def count_sort(arr):

    M = max(arr)

    Count = [0] * (M + 1)

    for num in arr:
        Count[num] += 1
    
    Pos = [0] * (M + 1)
    Pos[1] = 1

    for j in range(2, M+1):
        Pos[j] = Pos[j-1] + Count[j-1]
    
    sorted_array = [0] * len(arr)

    for num in arr:
        sorted_array[Pos[num] - 1] = num
        Pos[num] += 1
    
    return sorted_array

def counting_sorting(arr):

    M = max(arr)

    Count = [0] * (M + 1)

    for num in arr:
        Count[num] += 1
    
    Pos = [0] * (M + 1)
    Pos[1] = 1

    for j in range(2,M+1):
        Pos[j] = Pos[j-1] + Count[j-1]
    
    sorted_array = [0] * len(arr)

    for num in arr:
        sorted_array[Pos[num]-1] = num
        Pos[num] += 1

    return sorted_array



A = [4,2,2,8,3,3,1] 
print(counting_sorting(A))
print(counting_sort(A))
print(count_sort(A))