from itertools import combinations
from algo import Algo
from displayer import *
import time

class Bruteforce(Algo):
    
    def __init__(self, dataset, budget_limit, set_name, is_displaying_result=False, is_displaying_list=False):
        super().__init__(dataset, budget_limit, set_name, is_displaying_result, is_displaying_list)
        self._displayer = Displayer(f"Bruteforce ({self._set_name})")
        
    # Algorithm: Brute Force Investment Strategy
    def find_best_investment_bruteforce(self):
        start_time = time.time()
        
        best_combination = []
        max_profit = 0

        # Iterate through all possible sizes of combinations
        for r in range(1, len(self._dataset) + 1):
            # Generate all combinations of investments with current size
            for combination in combinations(self._dataset, r):
                # Calculate total cost of current combination
                total_cost = sum(action.price for action in combination)

                # Check if total cost is within budget limit
                if total_cost <= self._budget_limit:
                    # Calculate total profit of current combination
                    profit = sum(action.profit_ratio for action in combination)
                    # Update maximum profit and best combination if current combination yields higher profit
                    if profit > max_profit:
                        max_profit = profit
                        best_combination = combination
                            
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        self.display_info(elapsed_time, best_combination, max_profit)
        
        return best_combination, max_profit, elapsed_time
