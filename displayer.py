class Displayer:
    def __init__(self, title=""):
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def display_results(self, result, total_profit=0):
        print(f"[{self._title}] Total price of bought actions:", sum(action.get_price() for action in result) ,"$")
        if total_profit != 0: print(f"[{self._title}] Total profit after 2 years:", total_profit ,"$")
        print(f"[{self._title}] Total profit after 2 years (calculated):", sum(action.profit_ratio for action in result) ,"$")
        
    def display_list(list):
        for elem in list:
            print(elem)
        
    def display_duration(self, duration):
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        milliseconds = int((duration % 1) * 1000)
        
        formatted_time = "{:02d}:{:02d}.{:03d}".format(minutes, seconds, milliseconds)
        
        print(f"[{self._title}] Process completed after: {formatted_time}")