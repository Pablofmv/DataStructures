def majority_element(arr):

    candidate = arr[0]
    count = 1
    n = len(arr)

    for num in arr[1:]:

        if count == 0:
            candidate = num

        if candidate == num:
            count += 1
        else:
            count -= 1
    
    for num in arr:
        total_count = sum(1 for num in arr if candidate == num)
    
    return 1 if total_count > len(arr) / 2 else 0

A = [2,3,9,2,2]
B = [1, 2, 3, 1]
C = [512766168,717383758,5,126144732,5,573799007,5,5,5,405079772]
D = [1,2,1]
print(majority_element(A))
print(majority_element(B))
print(majority_element(C))
print(majority_element(D))