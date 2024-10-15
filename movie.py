from pricing import *

class Movie:
    REGULAR = RegularPriceStrategy()
    CHILDRENS = ChildrensPriceStrategy()
    NEW_RELEASE = NewReleasePriceStrategy()

    def __init__(self, title : str, price_strategy : PriceStrategy):
        self.title = title
        if not isinstance(price_strategy, PriceStrategy):
            self.price_strategy = NoPriceStrategy()
        else:
            self.price_strategy = price_strategy

    def get_title(self):
        return self.title
