from repository import Repository

# CSV_FILE= "dataset.csv"
# CSV_FILE= "dataset1_Python+P7.csv"
CSV_FILE= "dataset2_Python+P7.csv"
DATASET = Repository(CSV_FILE).read_csv()
BUDGET_LIMIT = 500 * 100
VALID_SHARES = [share for share in DATASET if share.price > 0]
# PRICES = [share.price for share in DATASET]
# PROFITS = [share.profit for share in DATASET]

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

names_dp = [
"Share-GYES",
"Share-ZGFP",
"Share-FWBE",
"Share-PLLK",
"Share-JWDZ",
"Share-DEPW",
"Share-MEQV",
"Share-TQMM",
"Share-LXZU",
"Share-KRRA",
"Share-RWIW",
"Share-JCWZ",
"Share-LAIC",
"Share-OEYT",
"Share-KOVS",
"Share-ZKOZ",
"Share-SCWM",
"Share-DQXJ",
"Share-ZLMC",
"Share-JMLZ",
"Share-FUGM",
"Share-KPBW",
"Share-VVYP",
"Share-FCHD",
"Share-PILL",
"Share-MZLD",
"Share-FAKH",
"Share-TMRA",
"Share-EOEN",
"Share-LKSD",
"Share-GIXZ",
"Share-CXYC",
"Share-DHIE",
"Share-OWMP",
"Share-BBNF",
"Share-BPPA",
"Share-GRVG",
"Share-OCKK",
"Share-BIJV",
"Share-DSOO",
"Share-IWTG",
"Share-TGPO",
"Share-VQQX",
"Share-RBCS",
"Share-LFXB",
"Share-XYMR",
"Share-YIFQ",
"Share-DYVD",
"Share-BMHD",
"Share-XQII",
"Share-FFZA",
"Share-ROOM",
"Share-FUDY",
"Share-GEBJ"
]
selected_dp = [obj for obj in VALID_SHARES if obj.name in names_dp]


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
print("Total price (Algorithm outcome):", sum(action.price for action in selected_actions) / 100, "$")
print("Total profit (Algorithm outcome):", total_profit / 100, "%")
print("Total profit (calculated):", sum(action.profit for action in selected_actions) / 100, "%")
print("Sienna selected shares total price (from CSV):", sum(action.price for action in selected_sienna) / 100, "$")
print("Sienna selected shares total profit (from CSV):", sum(action.profit for action in selected_sienna) / 100, "%")
print("DP selected shares total price (from CSV):", sum(action.price for action in selected_dp) / 100, "$")
print("DP selected shares total profit (from CSV):", sum(action.profit for action in selected_dp) / 100, "%")