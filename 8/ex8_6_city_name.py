def city_country(city_name, country):
	message = f"{city_name.title()}, {country.title()}"
	return message

print(city_country("amsterdam", "the netherlands"))
print(city_country("beijing", "china"))
print(city_country("berlin", "germany"))