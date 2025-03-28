def primitive_calculator(amount):
    
    min_operations = [float("inf")] * (amount + 1)
    min_operations[1] = 0
    prev = [0] * (amount + 1)

    for m in range(2,amount+1):

        add_1 = min_operations[m-1] + 1
        rest_operations = add_1
        prev[m] = m - 1

        if m % 2 == 0:
            divide_2 = min_operations[m // 2] + 1

            if divide_2 < rest_operations:
                rest_operations = divide_2
                prev[m] = m // 2

        if m % 3 == 0:
            divide_3 = min_operations[m // 3] + 1

            if divide_3 < rest_operations:
                rest_operations = divide_3
                prev[m] = m // 3
        
        min_operations[m] = rest_operations
    
    if min_operations[amount] == float("inf"):
        return -1, []
    
    sequence = []
    current = amount

    while current != 0:
        sequence.append(current)
        current = prev[current]  

    sequence.reverse()
    
    return min_operations[amount],sequence

amount = 96234
print(primitive_calculator(amount))


