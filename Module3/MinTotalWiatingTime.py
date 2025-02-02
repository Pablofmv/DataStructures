def MinTotalWaitingTime(array):
    waitingTime = 0
    treatedPacients = [0] * len(array)
    array_order = []
    n = len(array)


    for i in range(0,n):
        
        tmin = 100000
        min_index = 0

        for j in range(0,n):
            if treatedPacients[j] == 0 and array[j] < tmin:
                tmin = array[j]
                min_index = j
        
        treatedPacients[min_index] = 1
        array_order.append(tmin)
        waitingTime = waitingTime + tmin * (n -(i+1))

    print(array)
    print(array_order)
    print(waitingTime)
    return waitingTime


    

MinTotalWaitingTime([1,2,3])