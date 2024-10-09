import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie

class CustomerTest(unittest.TestCase): 
    """Tests of the Customer class."""
    
    def setUp(self):
        """Test fixture contains:
        
        c = a customer
        movies = list of some movies.
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)
    
    def test_compute_total_charge(self):
        """Test total charge for a collection of rentals."""
        self.c.add_rental(Rental(self.new_movie, 4))  # $12.00
        self.c.add_rental(Rental(self.regular_movie, 3))  # $3.50
        self.c.add_rental(Rental(self.childrens_movie, 4))  # $3.00

        total_charge = self.c.compute_total_charge()
        self.assertEqual(total_charge, 18.50)  # Total should be $18.50
    
    def test_statement(self):
        stmt = self.c.statement()
        # Get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        
        # Add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # Days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
