def BestItem(weight_array, value_array):
    maxValuePerWeight = 0
    n = len(weight_array)
    bestItem = 0
    for i in range(0,n):
        if weight_array[i] != 0:
            if value_array[i] / weight_array[i] > maxValuePerWeight:
                maxValuePerWeight = value_array[i] / weight_array[i]
                bestItem = i
    
    return bestItem

def MaxValueLoot(W, weight_array, value_array):
    n = len(weight_array)
    amounts = [0] * n
    maxAmount = 0

    while W > 0:
        bestIndex =  BestItem(weight_array, value_array)
        a = min(W, weight_array[bestIndex])

        amounts[bestIndex] = amounts[bestIndex] + a
        maxAmount = maxAmount + a * (value_array[bestIndex] / weight_array[bestIndex])

        weight_array[bestIndex] = weight_array[bestIndex] - a

        W = W - a
    
    return amounts, maxAmount


print(BestItem([10,10,10],[10,100,300]))
print(MaxValueLoot(100,[100,1,98],[100,100,300]))