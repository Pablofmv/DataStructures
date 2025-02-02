def BestItem(weight_array,value_array):
    bestItem = 0
    maxValuePerWeight = 0
    n = len(weight_array)

    for i in range(0,n):
        if weight_array[i] > 0:
            if (value_array[i] / weight_array[i]) > maxValuePerWeight:
                 maxValuePerWeight = value_array[i] / weight_array[i]
                 bestItem = i
    print(bestItem)
    return bestItem

def Knapsack(W, weight_array, value_array):
    n = len(weight_array)
    maxValue = 0
    amounts = [0] * n

    for i in range(0,n):
        if W == 0:
            return maxValue, amounts
        
        bestIndex = BestItem(weight_array,value_array)
        a = min(W,weight_array[bestIndex])

       
        W = W - a 
        
        print(a *  value_array[bestIndex]/weight_array[bestIndex])
        maxValue = maxValue + a * (value_array[bestIndex]/weight_array[bestIndex])
        weight_array[bestIndex] = weight_array[bestIndex] - a
        amounts[bestIndex] = amounts[bestIndex] + a

print(Knapsack(100,[100,99,0],[1,100,300]))