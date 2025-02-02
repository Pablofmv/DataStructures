def BestItem(weight_array, value_array):
    bestItem = 0
    maxWeightPerValue = 0
    n = len(weight_array)

    for i in range(0,n):
        if weight_array[i] > 0:
            if (value_array[i] / weight_array[i] > maxWeightPerValue):
                maxWeightPerValue = (value_array[i] / weight_array[i])
                bestItem = i
    
    return bestItem

def Knapsack(W, weight_array, value_array):
    n = len(weight_array)
    amounts = [0] * n
    totalValue = 0

    for i in range(0, n):
        if W == 0:
            return amounts, totalValue
        
        bestItem = BestItem(weight_array,value_array)
        a = min(W,weight_array[bestItem])

        W = W - a
        totalValue = totalValue + a * (value_array[bestItem] / weight_array[bestItem])
        amounts[bestItem] = amounts[bestItem] + a
        weight_array[bestItem] = weight_array[bestItem] - a
        


print(Knapsack(100,[100,99.5,100],[1,100,10]))
    