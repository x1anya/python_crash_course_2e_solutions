class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		print(f"The restaurant's name is {self.restaurant_name}.")
		print(f"The cuisine type of the restaurant is {self.cuisine_type}.")


	def open_restaurant(self):
		print("The restaurant is openning!")


restaurant_1 = Restaurant('KFC', 'fast food')
restaurant_2 = Restaurant('Sichuan Restaurant', 'chuancai')
restaurant_3 = Restaurant('Ramen', 'Japanese food')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()