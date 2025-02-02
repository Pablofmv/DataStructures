import random

def MaxPairwiseProduct(numbers):
    n = len(numbers)
    max_products = 0

    for i in range(0,n):
        for j in range(i+1,n):
            max_products = max(max_products, numbers[i] * numbers[j])
    
    return max_products

def MaxPairwiseProductFast(numbers):
    n = len(numbers)-1
    index = 0
    for i in range(1, n):
        if numbers[i] > numbers[index]:
            index = i

    numbers[index],numbers[n] = numbers[n],numbers[index]
    
    index = 0
    for i in range(1,n):
        if numbers[i] > numbers[index]:
            index = i
    
    numbers[index],numbers[n-1] = numbers[n-1],numbers[index]

    return numbers[n-1] * numbers[n]

def FindTwoLargest(numbers):
    n = len(numbers)
    print(n)
    largest = 0
    challengers = []

    for i in range(0,n):
        if numbers[i] > largest:
            challengers.append(numbers[i])
            largest = numbers[i]
    

    second_largest = 0
    for i in range(0,len(challengers)):
        if 

    print(challengers, largest)

FindTwoLargest([100,1,2,100,0,3,4,300])



'''
def StressTest(a,b):
    while True:
        n = random.randint(2,a)
        print(n)
        A = []

        for i in range(0,n):
            A.append(random.randint(0,b))
        
        print(A)

        result1 = MaxPairwiseProduct(A)
        result2 = MaxPairwiseProductFast(A)

        if result1 == result2:
            print("OK")
        else:
            print(f'Wrong Answer {result1} {result2}')
            break



StressTest(1000,200000)
'''



'''
if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split())) 
    print(MaxPairwiseProduct(input_numbers))
'''