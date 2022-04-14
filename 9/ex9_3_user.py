class User:

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name


	def describe_user(self):
		print(f"The user's name is {self.first_name.title()} {self.last_name.title()}.")
	

	def greet_user(self):
		print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")


user_1 = User('John', 'Doe')
user_2 = User('Natalie', 'Rice')
user_3 = User('Mary', 'Lynne')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()