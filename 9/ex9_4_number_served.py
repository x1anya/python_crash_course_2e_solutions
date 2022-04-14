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


restaurant = Restaurant('KFC', 'fast food')

print(f"The restaurant's name is {restaurant.restaurant_name}.")
print(f"The cuisine type of the restaurant is {restaurant.cuisine_type}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 3
print(f"Number served in this restaurant is {restaurant.number_served}.")

restaurant.set_number_served(15)
print(f"Number served in this restaurant is {restaurant.number_served}.")

restaurant.increment_number_served(30)
print(f"I believe the restaurant can server {restaurant.number_served} people per day!")