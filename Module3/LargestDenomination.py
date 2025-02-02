def Change(money, Denominations):
    numCoins = 0
    sortedDemonitations = sorted(Denominations, reverse = True)
    print(sortedDemonitations)
    i = 0
    while money > 0:
        print(numCoins, money, sortedDemonitations[i])
        numCoins += money // sortedDemonitations[i]
        money = money % sortedDemonitations[i]
        print(money)
        i += 1

    return numCoins

def ChangeOptimal(money,denominations):
    numCoins = 0
    sortedDenominations = sorted(denominations, reverse=True)
    i = 0
    minCoins = 9999

    for denomination in denominations:
        if money % denomination == 0:
            if money // denomination < minCoins:
                minCoins = money // denomination

    while money > 0:

        numCoins += money // sortedDenominations[i]
        money =  money % sortedDenominations[i]
        i += 1
    
    if minCoins < numCoins:
        return minCoins
    else:
        return numCoins

def Change(money):
    numCoins = 0

    while money > 0:
        if money >= 10:
            money = money - 10
        elif money >= 5:
            money = money - 5
        else:
            money = money - 1
        
        numCoins = numCoins + 1

    return numCoins

def ChangeBreak(money):
    return money // 10 + (money % 10) // 5 + money % 5

import random 

for i in range(0,20):
    m = random.randint(0,200)
    
    if Change(m) != ChangeBreak(m):
        print(m , Change(m), ChangeBreak(m))



'''
print(ChangeBreak(17))
    

print(ChangeOptimal(10,[1,5,10]))
print(ChangeOptimal(8,[1,4,6]))

print(Change(10,[1,5,10]))
print(Change(8,[1,4,6]))
'''