def majority_element_naive(elements):

    candidate = elements[0]
    count = 1

    for num in elements[1:]:

        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1
    
    if count <= 0:
        return 0
    
    total_count = sum(1 for num in elements if num == candidate)

    return 1 if  total_count > len(elements) / 2 else 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))

