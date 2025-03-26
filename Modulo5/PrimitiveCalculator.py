def primitive_calculator(amount):

    min_operations = [float("inf")] * (amount + 1)
    min_operations[1] = 0
    intermediate_numbers = [0] * (amount + 1)

    for m in range(2,amount+1):

        add_one = min_operations[m-1] + 1
        rest_operations = add_one

        if m%2 == 0:
            divide_2 = min_operations[m//2] + 1
            rest_operations = min(rest_operations,divide_2)
        
        if m%3 == 0:
            divide_3 = min_operations[m//3] + 1
            rest_operations = min(rest_operations,divide_3)
        
        min_operations[m] = rest_operations


    if min_operations[amount] == float("inf"):
        return -1
    
    return min_operations[amount]

amount = 96234
print(primitive_calculator(amount))

