def BestItem(weight_array,value_array):
    maxValuePerWeight = 0
    bestItem = 0
    n = len(weight_array)

    for i in range(0,n):
        if weight_array[i] > 0:
            if (value_array[i] / weight_array[i]) > maxValuePerWeight:
                maxValuePerWeight = value_array[i] / weight_array[i]
                bestItem = i
    
    return bestItem

def Knaspack(W,weight_array,value_array):
    n = len(weight_array)
    amounts = [0] * n
    totalValue = 0

    for i in range(0,n):
        if W == 0:
            return totalValue, amounts

        bestItem = BestItem(weight_array,value_array)
        a = min(W,weight_array[bestItem])

        totalValue = totalValue + a * (weight_array[bestItem] / value_array[bestItem])

        W = W - a
        weight_array[bestItem] = weight_array[bestItem] - a
        amounts[bestItem] = amounts[bestItem] + a

print(Knaspack(100, [100,99.5,100],[50,100,1]))