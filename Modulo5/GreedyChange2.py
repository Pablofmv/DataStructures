def greedy_change(money,denominations):
    denominations = sorted(denominations,reverse=True)
    Change = []

    while money > 0:
        for coin in denominations:
            if coin <= money:
                money -= coin
                Change.append(coin)
                break
    
    return Change

money = 24
denominations = [20,1,8]
print(greedy_change(money,denominations))
