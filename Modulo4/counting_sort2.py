def count_sort(arr):

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
        sorted_array[Pos[num] -1] = num
        Pos[num] += 1
    
    return sorted_array

A = [3,2,2]
print(count_sort(A))

M = 3
Count = [0,0,0,0]
Count = [0,0,2,1]

Pos = [0,0,0,0]
Pos = [0,1,0,0]

Pos[2] = Pos[1] + Count[1] = 1 + 0 = 1
Pos[3] = Pos[2] + Count[2] = 1 + 2 = 3

Pos = [0,1,1,3]

sorted_Array = [0,0,0]

sorted_array = [0,0,3]
Pos = [0,1,1,4]
sorted_array = [2,0,3]
Pos = [0,1,2,4]
sorted_array = [2,2,3]