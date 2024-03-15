from repository import Repository
from itertools import combinations


CSV_FILE= "dataset.csv"
# CSV_FILE= "dataset2_Python+P7.csv"
DATASET = Repository(CSV_FILE).read_csv()
BUDGET_LIMIT = 500 * 100
VALID_SHARES = [share for share in DATASET if share.price > 0]

def find_best_investment():
    best_combination = []
    max_profit = 0

    for r in range(1, len(VALID_SHARES) + 1):
        for combination in combinations(VALID_SHARES, r):
            total_cost = sum(action.price for action in combination)

            if total_cost <= BUDGET_LIMIT:
                profit = sum(action.profit_ratio for action in combination)
                if profit > max_profit:
                    max_profit = profit
                    best_combination = combination

    return best_combination, max_profit

best_combination, max_profit = find_best_investment()

for share in best_combination:
    print(share)
print("Total price of bought actions:", sum(action.get_price() for action in best_combination) ,"$")
print("Total profit after 2 years:", max_profit ,"$")
print("Total profit after 2 years (calculated):", sum(action.profit_ratio for action in best_combination) ,"$")