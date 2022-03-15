favorite_places = {
	'John': {
		'Seattle',
		'Beijing',
		'Amsterdam'
	},
	'Marie': {
		'Boston',
		'Paris'
	},
	'Stephan': {
		'Helsinki',
		'Berlin'
	}
}

for key, value in favorite_places.items():
	print(f"{key}'s favorite cities:")
	for v in value:
		print(f"\t{v}")