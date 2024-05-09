

class Player:
    def __init__(self, name, symbol:int):
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return self.name+" : with symbol "+str(self.symbol)

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name
