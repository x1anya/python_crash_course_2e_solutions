class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		print(f"The restaurant's name is {self.restaurant_name}.")
		print(f"The cuisine type of the restaurant is {self.cuisine_type}.")


	def open_restaurant(self):
		print("The restaurant is openning!")