def compute_operations(n):
    min_operations = [float("inf")] * (n + 1)
    min_operations[1] = 0

    prev = [0] * (n+1)

    for m in range(2,n+1):

        add_one = min_operations[m-1] + 1
        total_operations = add_one
        prev[m] = m - 1

        if m % 2 == 0:
            divide_two = min_operations[m // 2] + 1

            if divide_two < total_operations:
                total_operations = divide_two
                prev[m] = m // 2
        
        if m % 3 == 0:
            divide_three = min_operations[m // 3] + 1

            if divide_three < total_operations:
                total_operations = divide_three
                prev [m]= m // 3
        
        min_operations[m] = total_operations
    
    if min_operations[n] == float("inf"):
        return []
    
    sequence = []
    current = n

    while current != 0:
        sequence.append(current)
        current = prev[current]

    return sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
