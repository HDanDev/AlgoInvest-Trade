from repository import Repository

# CSV_FILE= "dataset.csv"
# CSV_FILE= "dataset1_Python+P7.csv"
CSV_FILE= "dataset2_Python+P7.csv"
DATASET = Repository(CSV_FILE).read_csv()
BUDGET_LIMIT = 500 * 100
VALID_SHARES = [share for share in DATASET if share.price > 0]

names_sienna = [
    "Share-ECAQ",
    "Share-IXCI",
    "Share-FWBE",
    "Share-ZOFA",
    "Share-PLLK",
    "Share-YFVZ",
    "Share-ANFX",
    "Share-PATS",
    "Share-NDKR",
    "Share-ALIY",
    "Share-JWGF",
    "Share-JGTW",
    "Share-FAPS",
    "Share-VCAX",
    "Share-LFXB",
    "Share-DWSK",
    "Share-XQII",
    "Share-ROOM"
]
selected_sienna = [obj for obj in VALID_SHARES if obj.name in names_sienna]

def greedy(actions, budget):
    actions.sort(key=lambda x: x.profit_ratio / x.price, reverse=True)

    selected_actions = []
    total_cost = 0

    for action in actions:
        if total_cost + action.price <= budget:
            selected_actions.append(action)
            total_cost += action.price
            
    return selected_actions

def knapsack(actions, budget):
    n = len(actions)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if actions[i - 1].price <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - actions[i - 1].price] + actions[i - 1].profit_ratio)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_actions = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_actions.append(actions[i - 1])
            w -= actions[i - 1].price

    return selected_actions, dp[n][budget]

zero_one_selection, total_profit = knapsack(VALID_SHARES, BUDGET_LIMIT)
greedy_selection = greedy(VALID_SHARES, BUDGET_LIMIT)

print("Selected actions using knapsack algorithm:")
for action in zero_one_selection:
    print(action)
print("Total price (Algorithm outcome):", sum(action.get_price() for action in zero_one_selection), "$")
print("Total profit (Algorithm outcome):", total_profit, "$")
print("Total profit (calculated):", sum(action.profit_ratio for action in zero_one_selection), "$")
print("Sienna selected shares total price (from CSV):", sum(action.get_price() for action in selected_sienna), "$")
print("Sienna selected shares total profit (from CSV):", sum(action.profit_ratio for action in selected_sienna), "$")
print("Total price (Greedy outcome):", sum(action.get_price() for action in greedy_selection), "$")
print("Total profit (Greedy outcome):", sum(action.profit_ratio for action in greedy_selection), "$")