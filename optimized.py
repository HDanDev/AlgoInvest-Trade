from repository import Repository

# CSV_FILE= "dataset.csv"
# CSV_FILE= "dataset1_Python+P7.csv"
CSV_FILE= "dataset2_Python+P7.csv"
DATASET = Repository(CSV_FILE).read_csv()
BUDGET_LIMIT = 500 * 100
VALID_SHARES = [share for share in DATASET if share.price > 0]
# PRICES = [share.price for share in DATASET]
# PROFITS = [share.profit for share in DATASET]

def knapsack(actions, budget):
    n = len(actions)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if actions[i - 1].price <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - actions[i - 1].price] + actions[i - 1].profit)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_actions = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_actions.append(actions[i - 1])
            w -= actions[i - 1].price

    return selected_actions, dp[n][budget]

selected_actions, total_profit = knapsack(VALID_SHARES, BUDGET_LIMIT)

print("Selected actions using knapsack algorithm:")
for action in selected_actions:
    print(action)
print("Total price:", sum(action.price for action in selected_actions) / 100, "$")
print("Total profit:", total_profit / 100, "%")
print("Total profit (calculated):", sum(action.profit for action in selected_actions) / 100, "%")