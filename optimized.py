from repository import Repository


JSON_FILE= "dataset.json"
DATASET = Repository(JSON_FILE).read_json()
BUDGET_LIMIT = 500

def find_best_investment_optimized():
    n = len(DATASET)

    DATASET.sort(key=lambda x: x['income'], reverse=True)

    best_combination = []
    max_profit = 0
    current_cost = 0
    i = 0

    while i < n and current_cost + DATASET[i]['cost'] <= BUDGET_LIMIT:
        current_cost += DATASET[i]['cost']
        best_combination.append(DATASET[i])
        max_profit += DATASET[i]['income']
        i += 1

    return best_combination, max_profit

best_combination, max_profit = find_best_investment_optimized()

print("Meilleure combinaison d'actions:", best_combination)
print("Profit maximal après 2 ans:", max_profit)
