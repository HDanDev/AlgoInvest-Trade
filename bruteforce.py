from repository import Repository
from itertools import combinations


# CSV_FILE= "dataset.csv"
CSV_FILE= "dataset2_Python+P7.csv"
DATASET = Repository(CSV_FILE).read_csv()
BUDGET_LIMIT = 500

def find_best_investment():
    best_combination = []
    max_profit = 0

    for r in range(1, len(DATASET) + 1):
        for combination in combinations(DATASET, r):
            total_cost = sum(action.price for action in combination)

            if total_cost <= BUDGET_LIMIT:
                profit = sum(action.profit for action in combination)
                if profit > max_profit:
                    max_profit = profit
                    best_combination = combination

    return best_combination, max_profit

best_combination, max_profit = find_best_investment()

print(best_combination)
print("Profit maximal après 2 ans:", max_profit ,"%")