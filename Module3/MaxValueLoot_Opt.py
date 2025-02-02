def MaxValueOpt(W, weight_array, value_array):
    n = len(weight_array)
    weightPerValue = [0] * n

    amounts = [0] * n
    totalValue = 0

    for i in range(0,n):
        if weight_array[i] == 0:
            weightPerValue[i] = 0
        else:
            weightPerValue[i] = value_array[i] / weight_array[i]

    print(weightPerValue)
    sortIndex = sorted(range(0,n), key = lambda x:weightPerValue[x], reverse=True)

    
    for index in sortIndex:
        if W == 0:
            return totalValue, amounts 
        
        a = min(W, weight_array[index])

        W = W - a
        amounts[index] = amounts[index] + a
        totalValue = totalValue + a * (weightPerValue[index])


print(MaxValueOpt(100,[100,99.5,100],[50,100,1]))




