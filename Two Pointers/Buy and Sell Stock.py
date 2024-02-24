def maxProfit(prices):
    left, right = 0,1 # Buy/Sell
    max_profit = 0

    while right < len(prices):
        currentProfit = prices[right] - prices[left] # Current profit
        if prices[left] < prices[right]:
            max_profit = max(currentProfit, max_profit)
        else:
            left = right
        right += 1
    return max_profit