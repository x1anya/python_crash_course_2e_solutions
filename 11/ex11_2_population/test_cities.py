import unittest
from city_functions import city_function

class NamesTestCase(unittest.TestCase):
	def test_city_country(self):
		city_country = city_function('beijing', 'china')
		self.assertEqual(city_country, "Beijing, China")

	def test_city_country_population(self):
		city_country = city_function('santiago', 'chile', 5000000)
		self.assertEqual(city_country, "Santiago, Chile - Population 5000000")

if __name__ == '__main__':
	unittest.main()