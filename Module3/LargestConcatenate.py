import time 

def LargestConcatenate(array):
    result = ''
    while array != []:
        maxNumber = max(array)
        result += str(maxNumber)
        array.remove(maxNumber)

    return result

def LargestConcatenateOpt(array):
    return ''.join(map(str,(sorted(array,reverse=True))))

def LargestConcatenateGlobal(array):
    temp = [digit for number in array for digit in str(number)]
    return ''.join(map(str,sorted(temp,reverse=True)))

print(LargestConcatenateGlobal([2,21]))


'''
start_time = time.time()
print(LargestConcatenateOpt([2,3,9,2,2]))
end_time = time.time()

print(end_time - start_time)

start_time = time.time()
print(LargestConcatenate([2,3,9,2,2]))
end_time = time.time()

print(end_time - start_time)
'''


