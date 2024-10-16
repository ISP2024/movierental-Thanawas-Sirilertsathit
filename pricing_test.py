import unittest
from rental import Rental
from movie import Movie
from pricing import *

class PricingTest(unittest.TestCase):
    
    def test_regular_pricing(self):
        """Test regular pricing strategy."""
        rental = Rental(Movie("Mulan", 1999, "Action"), 2)
        self.assertTrue(isinstance(rental.get_price_for_movie(), RegularPriceStrategy))

    def test_new_release_pricing(self):
        """Test new release pricing strategy."""
        rental = Rental(Movie("Mulan", 2024, "Action"), 2)
        self.assertTrue(isinstance(rental.get_price_for_movie(), NewReleasePriceStrategy))

    def test_children_pricing(self):
        """Test new release pricing strategy."""
        rental = Rental(Movie("Mulan", 1999, "Children"), 2)
        self.assertTrue(isinstance(rental.get_price_for_movie(), ChildrensPriceStrategy))