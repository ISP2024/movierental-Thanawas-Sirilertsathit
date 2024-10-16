import csv
import logging
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
                    if len(row) < 3:
                        logging.error(f"Skipping invalid row: {row}")
                        continue
                    title, year, genres = row[0], int(row[1]), row[2].split('|')
                    movie = Movie(title=title, year=year, genre=genres)
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
