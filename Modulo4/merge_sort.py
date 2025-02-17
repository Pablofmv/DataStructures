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


def nerge_a(left_part, right_part):
    
    sorted_array = []
    i,j = 0,0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            sorted_array.append(left_part[i])
            i += 1
        else:
            sorted_array.append(right_part[j])
            j += 1
        
    
    sorted_array.extend(left_part[i:])
    sorted_array.extend(right_part[j:])

    return sorted_array



def merge_sort_a(arr):
    if len(arr) == 1:
        return arr
   
    n = len(arr)
    mid = n // 2

    left_part = merge_sort_a(arr[0:mid])
    right_part = merge_sort_a(arr[mid:])
    
    return nerge_a(left_part,right_part)


arr = [7,2,9,4,6,1]
print(merge_sort_a(arr))

arr = [7,2,9,4,6,1]
print(merge_sort(arr))

