from bruteforce import Bruteforce
from optimized import Optimized
from optimized import *
from displayer import *
from share import Share
import numpy as np
from sklearn.linear_model import LinearRegression
from enum import Enum

PROCESSING_TIMES = [0.0,
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

class AlgoType(Enum):
    Bruteforce = 1
    Greedy = 2
    Zero_one = 3
    
class Tester:
    def __init__(self, dataset, budget, displayer_name=''):
        self._dataset = dataset
        self._budget = budget
        self._displayer_name = displayer_name
        self._displayer = Displayer(self._displayer_name)
                
    @property
    def dataset(self):
        return self._dataset

    @dataset.setter
    def dataset(self, value):
        self._dataset = value
        
    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        self._budget = value
        
    @property
    def displayer_name(self):
        return self._displayer_name

    @displayer_name.setter
    def displayer_name(self, value):
        self._displayer_name = value
        self._displayer = Displayer(value)
        
    def check_csv_validity(self):        
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
        selected_sienna = [obj for obj in self._dataset if obj.name in names_sienna]
        Displayer("Sienna").display_results(selected_sienna)

    def evaluate_bruteforce_greediness(self, is_allowing_custom_index_input=False):    
        datatest = []
        durations = []
        displayer = Displayer("Bruteforce greediness test")
        for i in range(24):
            share = Share(f'Test share {i}', i, i)
            datatest.append(share)
            bruteforce_selection, bruteforce_profit, bruteforce_duration = Bruteforce(datatest, self._budget, f"Set test {i}").find_best_investment_bruteforce()
            displayer.display_duration(bruteforce_duration)
            durations.append(bruteforce_duration)
            
        if is_allowing_custom_index_input: self.estimate_processing_duration_by_index(durations)
        # iterations = np.arange(1, len(durations) + 1).reshape(-1, 1)

        # model = LinearRegression()
        # model.fit(iterations, durations)

        # displayer.display_duration(model.predict([[20]])[0])
        # print("Estimated time for 20 loops:")
        
    def select_best_share(self, enum_type, set_name="Set 1"):
        if enum_type == AlgoType.Bruteforce:
            bruteforce_selection, bruteforce_profit, bruteforce_duration = Bruteforce(self._dataset, self._budget, set_name, True).find_best_investment_bruteforce()
        if enum_type == AlgoType.Zero_one:
            zero_one_selection, zero_one_profit, zero_one_duration = Optimized(self._dataset, self._budget, set_name, True).find_best_investment_knapsack()
        if enum_type == AlgoType.Greedy:
            greedy_selection, greedy_duration = Optimized(self._dataset, self._budget, set_name, True).find_best_investment_greedy()
    
    def _get_ratios_between_items(self, list):
        ratios = []
        for i in range(1, len(list)):
            if list[i - 1] != 0:
                ratio = list[i] / list[i - 1]
                ratios.append(ratio)
            else:
                print("Warning: Zero division encountered, skipping ratio calculation.")
                
        return ratios
    
    def _estimate_index_value_using_ratio(self, ratios_list, target_list, targeted_index):
        result = target_list
        avg_ratio = np.mean(ratios_list)
            
        for j in range ((len(result) - 1), targeted_index):

            next_entry = result[-1] * avg_ratio
            result.append(next_entry)
            
        return result

    def _get_index_value(self, previous_entries, target_index):
        
        if target_index < (len(previous_entries) - 1):
            return previous_entries[target_index]
        
        if len(previous_entries) < 2:
            print("Not enough entries to make a prediction.")
            return None
    
        ratios = self._get_ratios_between_items(previous_entries)
        
        if not ratios:
            print("Unable to calculate prediction due to zero division.")
            return None
        
        next_entry = self._estimate_index_value_using_ratio(ratios, previous_entries, target_index)

        return next_entry[-1]

    def estimate_processing_duration_by_index(self, list=PROCESSING_TIMES):
        while True:
            input_key = input("Type the loop index for which you would like to estimate the completion time, or press 'q' to quit: ")

            if input_key.lower() == 'q':
                break
            
            elif input_key.isdigit():
                input_key = int(input_key)
                next_entry = self._get_index_value(list, input_key)
                if next_entry != None:
                    print(f"After {input_key} loops the estimated completion time would be of: {Displayer().display_duration(next_entry, False)}")
                else:
                    print("No enough data to estimate next entry value")

        print("Done!")
        
    def calculate_value_at_index(self, initial_value, x):
        result = initial_value * (2 ** (x - 1))
        result = self._displayer.display_duration(result, False)
        return result