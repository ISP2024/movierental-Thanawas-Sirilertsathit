import unittest
from customer import Customer
from unittest import mock
from rental import Rental
from movie import Movie
import logging


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment by creating movie instances."""
        self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
        self.regular_movie = Movie("Air", Movie.REGULAR)
        self.children_movie = Movie("Frozen", Movie.CHILDRENS)

    def test_movie_attributes(self):
        """Trivial test to catch refactoring errors or changes in the API of Movie."""
        m = Movie("Air", Movie.REGULAR)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(Movie.REGULAR, m.get_price_code())

    def test_rental_price(self):
        """General movie renting."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

    def test_regular_movie_price(self):
        """Regular movie renting."""
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_price(), 3.5)  # $2 for first 2 days + $1.5 for the extra day

    def test_children_movie_price(self):
        """Children's movie renting."""
        rental = Rental(self.children_movie, 4)
        self.assertEqual(rental.get_price(), 3.0)  # $1.5 for first 3 days + $1.5 for the extra day

    def test_new_release_movie_price(self):
        """New release movie renting."""
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)  # $3 per day for 5 days

    def test_unrecognized_price_code(self):
        """Test behavior for unrecognized price code."""
        mock_logger = mock.Mock()
        logging.getLogger = lambda: mock_logger
        
        mock_movie = mock.Mock()
        mock_movie.get_price_code.return_value = "UNKNOWN"
        
        rental = Rental(mock_movie, 2)
        price = rental.get_price()

        self.assertEqual(price, 0)  # No price should be calculated for unrecognized code
        mock_logger.error.assert_called_once()

    def test_rental_points_new_release(self):
        """Test frequent renter points for new release movies."""
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.rental_points(), 5)  # New release earns 1 point per day rented

    def test_rental_points_regular_movie(self):
        """Test frequent renter points for regular movies."""
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.rental_points(), 1)  # Regular movie earns 1 point

    def test_rental_points_children_movie(self):
        """Test frequent renter points for children's movies."""
        rental = Rental(self.children_movie, 4)
        self.assertEqual(rental.rental_points(), 1)  # Children's movie earns 1 point
        