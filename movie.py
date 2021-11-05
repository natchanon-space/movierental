from typing import List


class Movie:
	"""
	A movie available for rent.
	"""
	def __init__(self, title: str, year: int, genre: List[str]):
		# Initialize a new movie. 
		self._title = title
		self._year = year
		self._genre = genre

	def get_title(self):
		return self._title

	def get_year(self):
		return self._year

	def is_genre(self, genre: str):
		return genre in self._genre

	def get_price_code(self):
		# get the price code
		return self.price_code
	
	def __str__(self):
		return self.title
