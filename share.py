from decimal import Decimal, ROUND_HALF_UP

class Share:
    def __init__(self, name, price, profit):
        self._name = name
        self._price = int(float(price) * 100)
        self._profit = int(float(profit) * 100)
        self._profit_ratio = self.rounded((float(price) * (float(profit) / 100)))
        
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
        
    @property
    def profit_ratio(self):
        return self._profit_ratio

    @profit_ratio.setter
    def profit_ratio(self, value):
        self._profit_ratio = value
            
    def get_price(self):
        return self.rounded(self._price / 100)
                
    def get_profit(self):
        return self.rounded(self._profit / 100)

    def __str__(self):
        return f"{self.name} - Price: {self.get_price()}$, Profit(%): {self.get_profit()}%, Profit($): {self._profit_ratio}$"
    
    def rounded(self, value):
        return Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
