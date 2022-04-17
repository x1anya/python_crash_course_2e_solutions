class Employee:
	def __init__(self, firstname, lastname, salary):
		self.firstname = firstname
		self.lastname = lastname
		self.salary = salary

	def give_raise(self, sraise=''):
		if sraise:
			self.salary += sraise
		else:
			self.salary += 5000
