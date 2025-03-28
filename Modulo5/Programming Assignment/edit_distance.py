def edit_distance(first_string, second_string):

    n = len(first_string)
    m = len(second_string)

    if n == 0:
        return m
    
    if m == 0:
        return n

    if first_string[n-1] == second_string[m-1]:
        return edit_distance(first_string[0:n-1], second_string[0:m-1])
    
    deletion = edit_distance(first_string[0:n-1], second_string[0:m]) + 1
    insertion = edit_distance(first_string[0:n], second_string[0:m-1]) + 1
    sustitution = edit_distance(first_string[0:n-1], second_string[0:m-1]) + 1

    return min(deletion, insertion, sustitution)


if __name__ == "__main__":
    print(edit_distance(input(), input()))
