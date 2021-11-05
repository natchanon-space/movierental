import unittest
from datetime import datetime
from rental import Rental, PriceCode
from movie import Movie


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.year = datetime.now().year
		self.new_movie = Movie("New", self.year, ["New"])
		self.regular_movie = Movie("Regular", self.year+1, ["Regular"])
		self.childrens_movie = Movie("Children", self.year+1, ["Children"])

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", self.year, ["Action"])
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

	def test_price_code_factory(self):
		# new
		self.assertEqual(PriceCode.NEW_RELEASE, Rental.for_movie(self.new_movie))
		# regular
		self.assertEqual(PriceCode.REGULAR, Rental.for_movie(self.regular_movie))
		# children
		self.assertEqual(PriceCode.CHILDRENS, Rental.for_movie(self.childrens_movie))
		# test not equal
		self.assertNotEqual(PriceCode.NEW_RELEASE, Rental.for_movie(self.regular_movie))