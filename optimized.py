import time
from algo import Algo
from displayer import *

class Optimized(Algo):
    def __init__(self, dataset, budget_limit, set_name, is_displaying_result=False, is_displaying_list=False):
        super().__init__(dataset, budget_limit, set_name, is_displaying_result, is_displaying_list)

    def find_best_investment_greedy(self):
        start_time = time.time()
        
        self._dataset.sort(key=lambda x: x.profit_ratio / x.price, reverse=True)

        selected_actions = []
        total_cost = 0

        for action in self._dataset:
            if total_cost + action.price <= self._budget_limit:
                selected_actions.append(action)
                total_cost += action.price
                
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        self._displayer = Displayer(f"Optimized greedy ({self._set_name})")
        self.display_info (elapsed_time, selected_actions)
                
        return selected_actions, elapsed_time

    def find_best_investment_knapsack(self):
        start_time = time.time()
        
        n = len(self._dataset)
        dp = [[0] * (self._budget_limit + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, self._budget_limit + 1):
                if self._dataset[i - 1].price <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - self._dataset[i - 1].price] + self._dataset[i - 1].profit_ratio)
                else:
                    dp[i][w] = dp[i - 1][w]

        selected_actions = []
        w = self._budget_limit
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_actions.append(self._dataset[i - 1])
                w -= self._dataset[i - 1].price
                
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        self._displayer = Displayer(f"Optimized 0/1 ({self._set_name})")
        self.display_info (elapsed_time, selected_actions, dp[n][self._budget_limit])

        return selected_actions, dp[n][self._budget_limit], elapsed_time