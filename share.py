class Share:
    def __init__(self, name, price, profit):
        self._name = name
        self._price = int(float(price) * 100)
        self._profit = int(float(profit) * 100)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        
    @property
    def profit(self):
        return self._profit

    @profit.setter
    def profit(self, value):
        self._profit = value
        
    def get_price(self):
        return float(self._price / 100)
            
    def get_profit(self):
        return float(self._profit / 100)

    def __str__(self):
        return f"{self.name} - Price: {self.price / 100}$, Profit: {self.profit / 100}%"