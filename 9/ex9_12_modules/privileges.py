from users import User

class Admin(User):

	def __init__(self, first_name, last_name, privileges):
		super().__init__(first_name, last_name)
		self.privileges = privileges



class Privileges:

	def __init__(self):
		self.privileges = ["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		print("The admin user has these privileges:")
		for item in self.privileges:
			print(item)