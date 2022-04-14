class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0


	def describe_restaurant(self):
		print(f"The restaurant's name is {self.restaurant_name}.")
		print(f"The cuisine type of the restaurant is {self.cuisine_type}.")


	def open_restaurant(self):
		print("The restaurant is openning!")


	def set_number_served(self, number):
		self.number_served = number


	def increment_number_served(self, increment):
		self.number_served += increment


class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ["apple", "vanilla", "pineapple", "chocolate"]

	def show_icecreams(self):
		print("We have icecream flavors:")
		for item in self.flavors:
			print(item)


icecream_stand = IceCreamStand("DQ", "icecream")
icecream_stand.show_icecreams()