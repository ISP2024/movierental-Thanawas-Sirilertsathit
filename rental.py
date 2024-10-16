from movie import Movie
from pricing import *
from datetime import datetime

class Rental:
    """
    A rental of a movie by a customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application, only days_rented is recorded.
    """ 
    REGULAR = RegularPriceStrategy()
    CHILDRENS = ChildrensPriceStrategy()
    NEW_RELEASE = NewReleasePriceStrategy()
    NOPRICE = NoPriceStrategy()
    def __init__(self, movie : Movie, days_rented : int): 
        """Initialize a new movie rental object for
        a movie with a known rental period (days_rented).
        """
        self.movie = movie
        self.days_rented = days_rented
        if self.movie.year == datetime.now().year:
            self.pricing = NewReleasePriceStrategy()
        elif "Child" in self.movie.genre or "Children" in self.movie.genre:
            self.pricing = ChildrensPriceStrategy()
        else:
            self.pricing = RegularPriceStrategy()

    def get_movie(self):
        """Return movie object."""
        return self.movie

    def get_days_rented(self):
        """Return the number of day you rent."""
        return self.days_rented

    def get_price(self):
        """Delegates price calculation to the movie's price strategy."""
        return self.pricing.get_price(self.days_rented)

    def rental_points(self):
        """Delegates rental points calculation to the movie's price strategy."""
        return self.pricing.get_rental_points(self.days_rented)

    def get_price_code(self):
        """Return price code."""
        return self.pricing.get_code()
    
    def get_price_for_movie(self):
        """Return price strategy."""
        return self.pricing

print(datetime.now().year)