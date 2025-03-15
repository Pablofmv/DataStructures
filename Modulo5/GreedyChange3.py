def greedy_change(money,denomination):

    denomination = sorted(denomination, reverse=True)
    Change = []

    while money > 0:

        for coin in denomination:

            if coin <= money:
                money -= coin
                Change.append(coin)
                break
        
    return Change

money = 20
denomination = [1,5,10]
print(greedy_change(money,denomination))
