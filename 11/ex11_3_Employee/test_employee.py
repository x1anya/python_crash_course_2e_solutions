import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		firstname = "John"
		lastname = "Doe"
		salary = 100000
		self.employee = Employee(firstname, lastname, salary)
		self.sraise = 6000

	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(self.employee.salary, 105000)

	def test_give_custom_raise(self):
		self.employee.give_raise(self.sraise)
		self.assertEqual(self.employee.salary, 106000)

if __name__ == '__main__':
	unittest.main()