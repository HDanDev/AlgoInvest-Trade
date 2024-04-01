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
        
    def display_duration(self, duration, is_printable=True):
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        milliseconds = int((duration % 1) * 1000)
        hours = minutes // 60
        minutes %= 60
        days = hours // 24
        hours %= 24

        formatted_time = ""
        if days != 0:
            formatted_time += f"{days}d "
        if hours != 0 or days != 0:
            formatted_time += f"{hours}h:"
        formatted_time += "{:02d}m:{:02d}.{:03d}s".format(minutes, seconds, milliseconds)

        if is_printable:
            print(f"[{self._title}] Process completed after: {formatted_time}")
        return formatted_time