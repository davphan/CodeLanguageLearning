def nordstromProb(orders):
    food = []
    orderNums = {}
    fullOrder = orders.splitlines()
    for oneOrder in fullOrder:
        splitOrder = oneOrder.split(",")
        table = splitOrder[1]
        food = splitOrder[2][:len(splitOrder[2] - 1)]
        

