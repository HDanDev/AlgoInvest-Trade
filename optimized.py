import time
from algo import Algo
from displayer import *

class Optimized(Algo):
    def __init__(self, dataset, budget_limit, set_name, is_displaying_result=False, is_displaying_list=False):
        super().__init__(dataset, budget_limit, set_name, is_displaying_result, is_displaying_list)
        
    # Algorithm: Greedy Investment Strategy
    def find_best_investment_greedy(self):
        start_time = time.time()
        
        # Sort dataset based on profit ratio to price ratio in descending order
        self._dataset.sort(key=lambda x: x.profit_ratio / x.price, reverse=True)

        selected_actions = []
        total_cost = 0

        # Iterate through sorted dataset
        for action in self._dataset:
            # Check if adding action's price exceeds budget limit
            if total_cost + action.price <= self._budget_limit:
                # Add action to selected_actions
                selected_actions.append(action)
                # Update total_cost
                total_cost += action.price
                    
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        self._displayer = Displayer(f"Optimized greedy ({self._set_name})")
        self.display_info(elapsed_time, selected_actions)
                    
        return selected_actions, elapsed_time

    # Algorithm: 0/1 Knapsack Investment Strategy
    def find_best_investment_knapsack(self):
        start_time = time.time()
        
        # Get number of investments
        n = len(self._dataset)
        # Initialize dp table to store maximum profit for each weight limit
        dp = [[0] * (self._budget_limit + 1) for _ in range(n + 1)]

        # Iterate through investments
        for i in range(1, n + 1):
            # Iterate through budget weights
            for w in range(1, self._budget_limit + 1):
                # Check if current investment's price fits within current weight limit
                if self._dataset[i - 1].price <= w:
                    # Update dp table with maximum profit
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - self._dataset[i - 1].price] + self._dataset[i - 1].profit_ratio)
                else:
                    # If not, inherit maximum profit from the previous row
                    dp[i][w] = dp[i - 1][w]

        # Initialize list to store selected actions
        selected_actions = []
        # Start from the last investment and maximum weight
        w = self._budget_limit
        for i in range(n, 0, -1):
            # Check if current investment contributes to maximum profit
            if dp[i][w] != dp[i - 1][w]:
                # If yes, add the investment to selected_actions
                selected_actions.append(self._dataset[i - 1])
                # Update remaining weight
                w -= self._dataset[i - 1].price
                    
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        self._displayer = Displayer(f"Optimized 0/1 ({self._set_name})")
        self.display_info(elapsed_time, selected_actions, dp[n][self._budget_limit])

        return selected_actions, dp[n][self._budget_limit], elapsed_time