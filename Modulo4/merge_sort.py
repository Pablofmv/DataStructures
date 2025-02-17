def merge(left_half, right_half):
    sorted_array = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):

        if left_half[i] <= right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1
        
    sorted_array.extend(left_half[i:])
    sorted_array.extend(right_half[j:])

    return sorted_array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[0:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

arr = [7,2,9,4,6,1]
print(merge_sort(arr))

