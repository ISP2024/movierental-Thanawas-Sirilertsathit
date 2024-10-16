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
        self.new_movie = Movie("Mulan", 2011, ["Action"])
        self.regular_movie = Movie("CitizenFour", 2013, ["Civilization"])
        self.childrens_movie = Movie("Frozen", 2012 , ["Fantasy"])
    
    def test_compute_total_charge(self):
        """Test total charge for a collection of rentals."""
        self.c.add_rental(Rental(self.new_movie, 4, Rental.NEW_RELEASE))  # $12.00
        self.c.add_rental(Rental(self.regular_movie, 3, Rental.REGULAR))  # $3.50
        self.c.add_rental(Rental(self.childrens_movie, 4, Rental.CHILDRENS))  # $3.00

        total_charge = self.c.compute_total_charge()
        self.assertEqual(total_charge, 18.50)  # Total should be $18.50
    
    def test_compute_total_rental_points(self):
        """Test total rental points for a collection of rentals."""
        self.c.add_rental(Rental(self.new_movie, 4, Rental.NEW_RELEASE))  # 4 points for new release
        self.c.add_rental(Rental(self.regular_movie, 3, Rental.REGULAR))  # 1 point for regular movie
        self.c.add_rental(Rental(self.childrens_movie, 4, Rental.CHILDRENS))  # 1 point for children's movie

        total_points = self.c.compute_total_rental_points()
        self.assertEqual(total_points, 6)  # Total points should be 4 + 1 + 1 = 6

    def test_statement(self):
        stmt = self.c.statement()
        # Get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        
        # Add a rental
        self.c.add_rental(Rental(self.new_movie, 4, Rental.NEW_RELEASE))
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
