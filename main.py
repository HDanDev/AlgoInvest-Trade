from dataset import Dataset
from tester import Tester, AlgoType

DATASET1 = Dataset("dataset.csv").valid_shares
DATASET2 = Dataset("dataset1_Python+P7.csv").valid_shares
DATASET3 = Dataset("dataset2_Python+P7.csv").valid_shares

BUDGET_LIMIT = 500 * 100

# Tester(DATASET3, BUDGET_LIMIT).estimate_processing_duration_by_index()
# Tester(DATASET3, BUDGET_LIMIT).evaluate_bruteforce_greediness(True)
Tester(DATASET1, BUDGET_LIMIT).select_best_share(AlgoType.Bruteforce)
Tester(DATASET1, BUDGET_LIMIT).select_best_share(AlgoType.Greedy)
Tester(DATASET1, BUDGET_LIMIT).select_best_share(AlgoType.Zero_one)
Tester(DATASET3, BUDGET_LIMIT).select_best_share(AlgoType.Greedy, "Set 3")
Tester(DATASET3, BUDGET_LIMIT).select_best_share(AlgoType.Zero_one, "Set 3")
Tester(DATASET3, BUDGET_LIMIT).check_csv_validity()
