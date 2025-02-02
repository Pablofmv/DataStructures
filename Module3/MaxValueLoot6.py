def BestItem(weights, values):
    bestItem = 0
    maxValuePerWeight = 0
    n = len(weights)
    
    for i in range(0,n):
       if weights[i] > 0:
        if values[i] / weights[i]  > maxValuePerWeight:
            maxValuePerWeight = values[i] / weights[i] 
            bestItem = i
    
    return bestItem

def Knapsack(W, weights, values):
   n = len(weights)
   maxValue = 0
   amounts = [0] * n

   for i in range(0, n):
        if W == 0:
            return maxValue, amounts
      
        bestIndex = BestItem(weights,values)
        a = min(W, weights[bestIndex])
     
        
        maxValue = maxValue + (a) * (values[bestIndex] / weights[bestIndex])
        weights[bestIndex] = weights[bestIndex] - a
        amounts[bestIndex] = amounts[bestIndex] + a

        W = W - a


print(Knapsack(100,[100,99,0],[1,100,300]))




      
    