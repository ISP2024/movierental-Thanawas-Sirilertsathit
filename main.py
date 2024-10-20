# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer

def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", 2024, ["Action"]),
        Movie("Oppenheimer", 2011, ["Action"]),
        Movie("Frozen", 2014, ["Fantasy", "Children"]),
        Movie("Bitconned", 2024, ["Finance"]),
        Movie("Particle Fever", 2010, ["Fantasy"])
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
