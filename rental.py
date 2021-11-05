from enum import Enum
from movie import Movie
from datetime import datetime
import logging


class PriceCode(Enum):
	REGULAR = {
		"price": lambda days: 2.0 + 1.5*max(0, days-2),
		"frp": lambda days: 1
	}
	CHILDRENS = {
		"price": lambda days: 1.5 + 1.5*max(0, days-3),
		"frp": lambda days: 1
	}
	NEW_RELEASE = {
		"price": lambda days: 3.0*days,
		"frp": lambda days: days
	}

	def price(self, days_rented):
		return self.value["price"](days_rented)

	def frequent_renter_points(self, day_rented):
		return self.value["frp"](day_rented)

	@classmethod
	def for_movie(self, movie: Movie):
		"""Get price code for a moive."""
		current_year = datetime.now().year
		if current_year == movie.get_year():
			return PriceCode.NEW_RELEASE
		if movie.is_genre("Children"):
			return PriceCode.CHILDRENS
		return PriceCode.REGULAR
		

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
	
	def __init__(self, movie: Movie, days_rented: int, price_code: PriceCode): 
		"""Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented
		self.price_code = price_code

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
		return self.price_code.frequent_renter_points(self.days_rented)

