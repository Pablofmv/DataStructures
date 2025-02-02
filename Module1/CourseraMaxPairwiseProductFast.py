def MaxPairwiseProductFast(numbers):
    n = len(numbers) - 1
    print(n)
    index = 0
    for i in range(1, n+1):
        if numbers[i] > numbers[index]:
            index = i

    numbers[index],numbers[n] = numbers[n],numbers[index]
    
    index = 0
    for i in range(1,n):
        if numbers[i] > numbers[index]:
            index = i
    
    numbers[index],numbers[n-1] = numbers[n-1],numbers[index]

    return numbers[n-1] * numbers[n]

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(MaxPairwiseProductFast(input_numbers))