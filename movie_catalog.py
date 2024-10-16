import csv
import logging
from pricing import NoPriceStrategy
from movie import Movie

class MovieCatalog:
    _instance = None

    def __new__(cls):
        """Define singleton."""
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance._load_movies()
        return cls._instance

    def _load_movies(self):
        """Load movies from the CSV file."""
        self.movies = {}
        try:
            with open('movies.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) < 4:
                        logging.error(f"Skipping invalid row: {row}")
                        continue
                    title, year, genres, price_strategy_code = row[0], int(row[1]), row[2].split('|'), row[3]
                    if price_strategy_code == "REGULAR":
                        price_strategy = Movie.REGULAR
                    elif price_strategy_code == "CHILDREN":
                        price_strategy = Movie.CHILDRENS
                    elif price_strategy_code == "NEW_RELEASE":
                        price_strategy = Movie.NEW_RELEASE
                    else:
                        price_strategy = NoPriceStrategy()
                    movie = Movie(title=title, year=year, genre=genres, price_strategy=price_strategy)
                    if title not in self.movies:
                        self.movies[title] = []
                    self.movies[title].append(movie)
        except Exception as e:
            logging.error(f"Error reading movies.csv: {e}")

    def get_movie(self, title, year=None):
        """Retrieve movie by title, optionally by year."""
        if title in self.movies:
            if year is None:
                return self.movies[title][0]
            for movie in self.movies[title]:
                if movie.year == year:
                    return movie
        return None
