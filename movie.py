from pricing import *
from dataclasses import dataclass, field
from typing import Collection

@dataclass(frozen=True)
class Movie:
    title: str
    year: int
    genre: Collection[str]

    def __str__(self) -> str:
        """Return the string representation of the movie as 'Title (Year)'."""
        return f"{self.title} ({self.year})"

    def is_genre(self, genre_name: str) -> bool:
        """Return True to check genre name."""
        return genre_name.lower() in (genre.lower() for genre in self.genre)
    