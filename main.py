# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental, PriceCode
from customer import Customer

def make_movies():
    catalog = MovieCatalog()
    movies = [
        catalog.get_movie("La La Land"),
        catalog.get_movie("Deadpool"),
        catalog.get_movie("Mulan"),
        catalog.get_movie("The Great Wall"),
        catalog.get_movie("Arrival")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        price_code = Rental.for_movie(movie)
        customer.add_rental(Rental(movie, days, price_code))
        days += 1
    print(customer.statement())
