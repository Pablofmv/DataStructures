def min_operations_to_target(target):

    if target == 1:
        return 0 

    min_operations = [float("inf")] * (target + 1)
    min_operations[1] = 0

    for i in range(2,target+1):

        min_operations[i] = min_operations[i-1] + 1

        if i% 2 ==0:
            min_operations[i] = min(min_operations[i],min_operations[i // 2] +1)
        
        if i%3 ==0:
            min_operations[i] = min(min_operations[i], min_operations[i//3] +1)


    return min_operations[target]
    

target = 99
print(min_operations_to_target(target))

