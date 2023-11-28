def max_profit(prices):
    max_profit = 0
    current_profit = 0

    for i in range(1, len(prices)):
        current_profit = max(0, current_profit + prices[i] - prices[i - 1])
        max_profit = max(max_profit, current_profit)

    return max_profit

# Пример использования
lst = [7, 4, 8, 10, 7, 4, 9]
result = max_profit(lst)
print(lst)
print("Максимальная прибыль:", result)
