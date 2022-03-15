favorite_numbers = {
	'Mary': {
		12,
		15,
		3
	},
	'John': {
		45,
		7
	},
	'Stephen': {
		13,
		14
	},
	'Sarah': {
		103,
		111,
		150,
		124
	},
	'Mike': {
		8,
		190
	}
}

for key, value in favorite_numbers.items():
	print(f"{key}'s favorite numbers are:")
	for v in value:
		print(f"\t{v}")