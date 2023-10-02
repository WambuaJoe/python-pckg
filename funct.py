class Restaurant:

	number_of_rest = 0
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name =restaurant_name
		self.cuisine_type = cuisine_type

		Restaurant.number_of_rest += 1

	def describe_restaurant(self):
		""" gives a simple description of the restaurant """
		print("Restaurant name: {}\nCuisine type: {}\n".format(
					self.restaurant_name, self.cuisine_type
		))
	
	def open_restaurant(self):
		""" indicates that restaurant is open """
		print("\n{} is open!".format(self.restaurant_name))


for num in range(Restaurant.number_of_rest):
	if num == 0:
		print("No restaurants recorded")
	elif num == 1:
		print("Only 1 restaurant: {}".format(Restaurant.number_of_rest))
	else:
		print("Restaurants: {}".format(Restaurant.number_of_rest))

restaurant1 = Restaurant("The Swa Spot", "Swahili dishes")
restaurant1.describe_restaurant()

restaurant2 = Restaurant("Bits n Bytez", "Mexican bitings")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("Benjy's", "Quick lunches")
restaurant3.describe_restaurant()

print()

