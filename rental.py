import logging
from movie import Movie

class Rental:
    """
    A rental of a movie by a customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application, only days_rented is recorded.
    """
    
    def __init__(self, movie, days_rented): 
        """Initialize a new movie rental object for
        a movie with a known rental period (days_rented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        """Calculate the price of a rental based on the movie type and days rented.

        Returns:
            The price of the rental as a float.
        """
        amount = 0
        
        if self.get_movie().get_price_code() == Movie.REGULAR:
            # Two days for $2, additional days $1.50 per day.
            amount = 2.0
            if self.get_days_rented() > 2:
                amount += 1.5 * (self.get_days_rented() - 2)

        elif self.get_movie().get_price_code() == Movie.CHILDRENS:
            # Three days for $1.50, additional days $1.50 per day.
            amount = 1.5
            if self.get_days_rented() > 3:
                amount += 1.5 * (self.get_days_rented() - 3)

        elif self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            # Straight $3 per day charge.
            amount = 3 * self.get_days_rented()

        else:
            log = logging.getLogger()
            log.error(f"Movie {self.get_movie()} has an unrecognized price code {self.get_movie().get_price_code()}")
        
        return amount
    
    def rental_points(self):
        """Calculate frequent renter points based on movie price code."""
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            return self.get_days_rented()  # New release earns 1 point per day rented
        else:
            return 1  # Other rentals get only 1 point
