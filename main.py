# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer

def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", 2020, ["Action"],Movie.NEW_RELEASE),
        Movie("Oppenheimer", 2011, ["Action"],Movie.REGULAR),
        Movie("Frozen", 2014, ["Fantasy"],Movie.CHILDRENS),
        Movie("Bitconned", 2020, ["Finance"],Movie.NEW_RELEASE),
        Movie("Particle Fever", 2034, ["Fantasy"],Movie.REGULAR)
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
