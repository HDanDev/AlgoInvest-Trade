from repository import Repository
from itertools import combinations


JSON_FILE= "dataset.json"
DATASET = Repository(JSON_FILE).read_json()
BUDGET_LIMIT = 500

def calculate_profit(combination):
    total_profit_percentage = sum(action['income'] for action in combination)
    return total_profit_percentage

def find_best_investment():
    best_combination = []
    max_profit = 0

    for r in range(1, len(DATASET) + 1):
        for combination in combinations(DATASET, r):
            total_cost = sum(action['cost'] for action in combination)

            if total_cost <= BUDGET_LIMIT:
                profit = calculate_profit(combination)
                if profit > max_profit:
                    max_profit = profit
                    best_combination = combination

    return best_combination, max_profit

best_combination, max_profit = find_best_investment()

print("Meilleure combinaison d'actions:", best_combination)
print("Profit maximal après 2 ans:", max_profit)