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

def Knapsack(W,weight_array,value_array):
    n = len(weight_array)
    amounts = [0] * n
    totalValue = 0

    for i in range(0,n):
        if W == 0:
            return totalValue, amounts
        
        i = BestItem(weight_array,value_array)
        a = min(weight_array[i],W)

        totalValue = totalValue + a * (value_array[i]/weight_array[i])        
        W = W - a
        weight_array[i] = weight_array[i] - a
        amounts[i] = amounts[i] + a

print(Knapsack(100, [100,99.5,100],[50,100,1]))