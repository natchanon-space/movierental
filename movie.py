import csv
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


class MovieCatalog:
	CATALOG_PATH = "movies.csv"

	def __init__(self) -> None:
		self.data = {}
		with open(self.CATALOG_PATH) as f:
			reader = csv.DictReader(f)
			for line in reader:
				self.data[line["title"]] = {
					"#id": line["#id"],
					"year": int(line["year"]),
					"genre": [g for g in line["genres"].split("|")] 
				}

	def get_movie(self, title) -> Movie:
		movie_data = self.data[title]
		return Movie(title, movie_data["year"], movie_data["genre"])
