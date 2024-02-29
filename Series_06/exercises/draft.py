def profit(rate, actions):
    assert isinstance(actions, str), "invalid actions"
    assert len(actions) == len(rate), "invalid actions"

    bitcoin = 0
    total_profit = 0

    for i in range(len(actions) - 1):
        if actions[i] == 'B':
            assert bitcoin == 0, "invalid actions"
            bitcoin += 1
            total_profit -= rate[i]
        elif actions[i] == 'S':
            assert bitcoin == 1, "invalid actions"
            bitcoin -= 1
            total_profit += rate[i]

    if bitcoin == 1:
        total_profit += rate[-1]

    return total_profit


def maximal_profit(rate):
    min_price = float('inf')
    max_profit = 0

    for price in rate:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


def optimal_actions(rate):
    min_price = float('inf')
    actions = ""

    for i in range(len(rate) - 1):
        if rate[i] < rate[i + 1]:
            if min_price == float('inf'):
                actions += "B"
                min_price = rate[i]
        elif rate[i] > rate[i + 1]:
            if min_price != float('inf'):
                actions += "S"
                min_price = float('inf')
        else:
            actions += "-"

    if min_price != float('inf'):
        actions += "S"

    return actions


# Example usage:
bitcoin_rate = [5, 11, 4, 2]
actions = optimal_actions(bitcoin_rate)
print(profit(bitcoin_rate, actions))  # Output: 17
