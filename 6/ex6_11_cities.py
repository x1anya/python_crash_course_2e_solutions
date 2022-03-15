cities = {
	'Amsterdam': {
		'country': "The Netherlands",
		'population': 730000,
		'fact': "red light zone"
	},
	'Boston': {
		'country': "The United States",
		'population': 4900000,
		'fact': "Boston Legal"
	},
	'Berlin': {
		'country': "Germany",
		'population': 3650000,
		'fact': "the capital"
	}
}

for key, value in cities.items():
	print(f"{key}:")
	for k, v in value.items():
		print(f"\t{k}: {v}")