def make_car(manufacturer, ctype, **keywords):
	keywords['manufacturer'] = manufacturer
	keywords['type'] = ctype
	return keywords

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)