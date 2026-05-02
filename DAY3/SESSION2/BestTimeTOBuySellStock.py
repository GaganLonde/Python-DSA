# def bestTimeToBuySellStock(prices):
#     min_price = prices[0]
#     max_profit = 0

#     for i in range(1, len(prices)):
#         max_profit = max(max_profit, prices[i] - min_price)
#         min_price = min(min_price, prices[i])

#     return max_profit

def bestTimeToBuySellStock(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i-1]
    
    return max_profit

# print(bestTimeToBuySellStock([7,1,5,3,6,4]))
