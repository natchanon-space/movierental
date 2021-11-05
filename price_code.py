from enum import Enum

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
