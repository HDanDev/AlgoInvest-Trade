class Share:
    def __init__(self, name, price, profit):
        self._name = name
        self._price = float(price)
        self._profit = float(profit)
        
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

    def __str__(self):
        return f"{self.name} - Price: {self.price}, Profit: {self.profit}"