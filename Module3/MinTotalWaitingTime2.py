def MinTotalWaitingTime(array):
    n = len(array)
    atended = [0] * n
    atendedOrder = []
    waitingTime = 0
    print(array)

    for i in range(0,n):
        tmin = 10000
        min_index = 0

        for j in range(0,n):
            if atended[j] == 0 and array[j] < tmin:
                tmin = array[j]
                min_index = j
        
        waitingTime =  waitingTime + tmin * (n -(i + 1))
        print(waitingTime)
        print()
        
        atended[min_index] = 1
        atendedOrder.append(tmin)

    print(atendedOrder)
    print(waitingTime)
    return waitingTime

MinTotalWaitingTime([3,1,2])

