import unittest
from rental import Rental
from movie import Movie
from price_code import PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan")
		self.regular_movie = Movie("CitizenFour")
		self.childrens_movie = Movie("Frozen")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour")
		self.assertEqual("CitizenFour", m.get_title())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1, PriceCode.NEW_RELEASE)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5, PriceCode.NEW_RELEASE)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.regular_movie, 1, PriceCode.REGULAR)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 9, PriceCode.REGULAR)
		self.assertEqual(rental.get_price(), 12.5)
		rental = Rental(self.childrens_movie, 2, PriceCode.CHILDRENS)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 4, PriceCode.CHILDRENS)
		self.assertEqual(rental.get_price(), 3.0)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1, PriceCode.NEW_RELEASE)
		self.assertEqual(rental.get_rental_points(), 1)
		rental = Rental(self.new_movie, 5, PriceCode.NEW_RELEASE)
		self.assertEqual(rental.get_rental_points(), 5)
		rental = Rental(self.regular_movie, 1, PriceCode.REGULAR)
		self.assertEqual(rental.get_rental_points(), 1)
		rental = Rental(self.regular_movie, 9, PriceCode.REGULAR)
		self.assertEqual(rental.get_rental_points(), 1)
		rental = Rental(self.childrens_movie, 2, PriceCode.CHILDRENS)
		self.assertEqual(rental.get_rental_points(), 1)
		rental = Rental(self.childrens_movie, 4, PriceCode.CHILDRENS)
		self.assertEqual(rental.get_rental_points(), 1)