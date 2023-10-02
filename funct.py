class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name =restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		""" gives a simple description of the restaurant """
		print("Restaurant name: {}\nCuisine type: {}\n".format(
					self.restaurant_name, self.cuisine_type
		))
	
	def open_restaurant(self):
		""" indicates that restaurant is open """
		print("\n{} is open!".format(self.restaurant_name))


restaurant1 = Restaurant("The Swa Spot", "Swahili dishes")
restaurant1.describe_restaurant()

restaurant2 = Restaurant("Bits n Bytez", "Mexican bitings")
restaurant2.describe_restaurant()

