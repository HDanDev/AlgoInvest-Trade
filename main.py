from bruteforce import Bruteforce
from optimized import Optimized
from dataset import Dataset
from optimized import *
from displayer import *
from share import Share
import numpy as np
from sklearn.linear_model import LinearRegression

DATASET1 = Dataset("dataset.csv").valid_shares
DATASET2 = Dataset("dataset1_Python+P7.csv").valid_shares
DATASET3 = Dataset("dataset2_Python+P7.csv").valid_shares

BUDGET_LIMIT = 500 * 100

### Check if CSV file is correctly read by comparing our data with Sienna's ###
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
# selected_sienna = [obj for obj in DATASET3 if obj.name in names_sienna]
# Displayer("Sienna").display_results(selected_sienna)
###########################################################################

def evaluate_bruteforce_greediness():    
    datatest = []
    durations = []
    displayer = Displayer("Bruteforce greediness test")
    for i in range(24):
        share = Share(f'Test share {i}', i, i)
        datatest.append(share)
        bruteforce_selection, bruteforce_profit, bruteforce_duration = Bruteforce(datatest, BUDGET_LIMIT, f"Set test {i}").find_best_investment_bruteforce()
        displayer.display_duration(bruteforce_duration)
        durations.append(bruteforce_duration)
    iterations = np.arange(1, len(durations) + 1).reshape(-1, 1)

    model = LinearRegression()
    model.fit(iterations, durations)

    displayer.display_duration(model.predict([[20]])[0])
    displayer.display_duration(model.predict([[30]])[0])
    displayer.display_duration(model.predict([[40]])[0])
    print("Estimated time for 20 loops:")

# bruteforce_selection, bruteforce_profit, bruteforce_duration = Bruteforce(DATASET1, BUDGET_LIMIT, "Set 1", True).find_best_investment_bruteforce()
# zero_one_selection, zero_one_profit, zero_one_duration = Optimized(DATASET1, BUDGET_LIMIT, "Set 1", True).find_best_investment_knapsack()
# greedy_selection, greedy_duration = Optimized(DATASET1, BUDGET_LIMIT, "Set 1", True).find_best_investment_greedy()
# evaluate_bruteforce_greediness()

test = [0.0,
0.000997304916381836,
0.001995086669921875,
0.0029914379119873047,
0.0059926509857177734,
0.011959075927734375,
0.02493429183959961,
0.04951167106628418,
0.10372257232666016,
0.2104659080505371,
0.4328792095184326,
0.8887746334075928,
1.8600504398345947,
3.814664125442505,
8.03862190246582,
16.51408076286316,
34.35612773895264,
74.62053847312927]

def calculate_value_at_index(initial_value, x):
    return initial_value * (2 ** (x - 1))

value_at_x = calculate_value_at_index(test[1], 17)
print(value_at_x)
Displayer().display_duration(value_at_x)