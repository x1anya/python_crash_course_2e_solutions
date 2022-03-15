pets = []

pet_0 = {
	'type': 'cat',
	'owner': 'John'
}

pet_1 = {
	'type': 'dog',
	'owner': 'Marie'
}

pet_2 = {
	'type': 'rabbit',
	'owner': 'Tom'
}

pets.append(pet_0)
pets.append(pet_1)
pets.append(pet_2)

for pet in pets:
	for k, v in pet.items():
		print(f"{k.title()}: {v}")