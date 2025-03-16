def greedy_change(money,denominations):

    denominations = sorted(denominations, reverse=True)
    Change = []

    while money > 0:

        for coin in denominations:

            if money >= coin:

                money -= coin
                Change.append(coin)
                break

    return Change

money = 17
denominations = [5,1,10]
print(greedy_change(money,denominations))
