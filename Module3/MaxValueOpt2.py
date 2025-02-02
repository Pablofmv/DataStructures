def KnapsackFast(W,weight_array,value_array):
    n = len(weight_array)
    valuePerWeight = [0] * n

    for i in range(0,n):
        if weight_array[i] == 0 :
            valuePerWeight[i] = 0
        else:
            valuePerWeight[i] = value_array[i] / weight_array[i]
    
    orderIndex = [i for i in sorted(range(0,n), key = lambda x: valuePerWeight[x], reverse=True)]

    maxValue = 0
    amounts = [0] * n

    for index in orderIndex:
        if W == 0:
            return maxValue, amounts
        
        a = min(W,weight_array[index])

        amounts[index] = amounts[index] + a
        maxValue = maxValue + a * valuePerWeight[index]

        W = W - a


print(KnapsackFast(100,[0,99,100],[100,200,1]))
