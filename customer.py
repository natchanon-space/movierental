from rental import PriceCode, Rental
from movie import Movie
import logging


class Customer:
    """
       A customer who rents movies.
       The customer object holds information about the
       movies rented for the current billing period,
       and can print a statement of his rentals.
    """
    def __init__(self, name: str):
        """ Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statement(self):
        """
            Print all the rentals in current period,
            along with total charges and reward points.
            Returns:
                the statement as a String
        """
        total_amount = 0 # total charges
        frequent_renter_points = 0 
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        for rental in self.rentals:
            # award renter points
            frequent_renter_points += rental.get_rental_points()
            #  add detail line to statement
            statement += fmt.format(rental.get_movie().get_title(), rental.get_days_rented(), rental.get_price())
            # compute rental change and accumulate activity
            total_amount += rental.get_price()

        # footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
                       "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement

if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = Movie("Hacker Noon", 2000, ["Action"])
    customer.add_rental(Rental(movie, 2, PriceCode.for_movie(movie)))
    movie = Movie("CitizenFour", 2002, ["Action"])
    customer.add_rental(Rental(movie, 3, PriceCode.for_movie(movie)))
    print(customer.statement())
