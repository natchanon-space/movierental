from movie import Movie
import logging


class PriceCode:
	PRICE_CODE = {
		Movie.REGULAR: {
			"price": lambda days: 2.0 + 1.5*max(0, days-2),
			"frp": lambda days: 1
		},
		Movie.CHILDRENS: {
			"price": lambda days: 1.5 + 1.5*max(0, days-3),
			"frp": lambda days: 1
		},
		Movie.NEW_RELEASE: {
			"price": lambda days: 3.0*days,
			"frp": lambda days: days
		}
	}

	def __init__(self, movie):
		self.movie_code = movie.get_price_code()

	def price(self, days_rented):
		if self.movie_code in self.PRICE_CODE.keys():
			return self.PRICE_CODE[self.movie_code]["price"](days_rented)
		raise KeyError()

class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""
	
	def __init__(self, movie, days_rented): 
		"""Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented
		self.price_code = PriceCode(self.movie)

	def get_movie(self):
		return self.movie

	def get_days_rented(self):
		return self.days_rented

	def get_price(self):
		amount = 0
		try:
			amount += self.price_code.price(self.days_rented)
		except KeyError:
			log = logging.getLogger()
			log.error(f"Movie {self.get_movie()} has unrecognized priceCode {self.get_movie().get_price_code()}")
		return amount

	def get_rental_points(self):
		frequent_renter_points = 0
		if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
			frequent_renter_points += self.get_days_rented()
		else:
			frequent_renter_points += 1
		return frequent_renter_points
