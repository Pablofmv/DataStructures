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

def Knapsack(W, weight_array,value_array):
    n = len(weight_array)
    amounts = [0] * n
    totalValue = 0

    for i in range(0, n):
        if W == 0:
            return amounts, totalValue
        
        i = BestItem(weight_array,value_array)
        a = min(W,weight_array[i])

        totalValue = totalValue + a * (value_array[i]/weight_array[i])
        W = W - a
        amounts[i] = amounts[i] + a
        weight_array[i] = weight_array[i] - a
    
    return amounts, totalValue


print(BestItem([0,99.5,100],[1,100,1]))
print(Knapsack(100, [0,99.5,100],[1,100,1]))


