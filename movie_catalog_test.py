import unittest
from movie_catalog import MovieCatalog
from movie import Movie

class TestMovieCatalog(unittest.TestCase):

    def setUp(self):
        """Initialize MovieCatalog."""
        self.catalog = MovieCatalog()

    def test_get_movie_by_title(self):
        """Test getting a movie by its title."""
        movie = self.catalog.get_movie("Mulan")
        self.assertIsNotNone(movie, "Movie should be found by title")
        self.assertEqual(movie.title, "Mulan")
    
    def test_get_movie_by_title_and_year(self):
        """Test getting a movie by both title and year."""
        movie = self.catalog.get_movie("Mulan", 1998)
        self.assertIsNotNone(movie, "Movie should be found by title and year")
        self.assertEqual(movie.title, "Mulan")
        self.assertEqual(movie.year, 1998)
    
    def test_movie_not_found(self):
        """Test getting a movie that doesn't exist."""
        movie = self.catalog.get_movie("Nonexistent Movie")
        self.assertIsNone(movie, "Should return None if the movie doesn't exist")

    def test_multiple_movies_with_same_title(self):
        """Search for same movie but different years."""
        movie_1998 = self.catalog.get_movie("Mulan", 1998)
        movie_2020 = self.catalog.get_movie("Mulan", 2020)
        
        self.assertIsNotNone(movie_1998, "Mulan (1998) should be found")
        self.assertIsNotNone(movie_2020, "Mulan (2020) should be found")

        self.assertEqual(movie_1998.year, 1998)
        self.assertEqual(movie_2020.year, 2020)
