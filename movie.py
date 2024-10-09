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

    def get_price(self, days_rented):
        """Delegate price calculation to the price strategy."""
        return self.price_strategy.get_price(days_rented)

    def get_rental_points(self, days_rented):
        """Delegate rental points calculation to the price strategy."""
        return self.price_strategy.get_rental_points(days_rented)

    def get_price_code(self):
        return self.price_strategy.get_code()
