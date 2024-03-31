from displayer import Displayer

class Algo:
    def __init__(self, dataset, budget_limit, set_name, is_displaying_result=False, is_displaying_list=False):
        self._dataset = dataset
        self._budget_limit = budget_limit
        self._set_name = set_name
        self._is_displaying_result = is_displaying_result
        self._is_displaying_list = is_displaying_list
        self._displayer = Displayer()
        
    @property
    def dataset(self):
        return self._dataset

    @dataset.setter
    def dataset(self, value):
        self._dataset = value
        
    @property
    def budget_limit(self):
        return self._budget_limit

    @budget_limit.setter
    def budget_limit(self, value):
        self._budget_limit = value
        
    @property
    def set_name(self):
        return self._set_name

    @set_name.setter
    def set_name(self, value):
        self._set_name = value
        
    @property
    def is_displaying_result(self):
        return self._is_displaying_result

    @is_displaying_result.setter
    def is_displaying_result(self, value):
        self._is_displaying_result = value
        
    @property
    def is_displaying_list(self):
        return self._is_displaying_list

    @is_displaying_list.setter
    def is_displaying_list(self, value):
        self._is_displaying_list = value
        
    @property
    def displayer(self):
        return self._displayer

    @displayer.setter
    def displayer(self, value):
        self._displayer = value
        
    def display_info(self, time, list, profit=0):
        self._displayer.display_duration(time)
        if self.is_displaying_result: self._displayer.display_results(list, profit)
        if self.is_displaying_list: self._displayer.display_list(list, profit)