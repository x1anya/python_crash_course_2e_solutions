person_0 = {
	'first': 'John',
	'last': 'Doe',
	'age': '35',
	'city': 'Seattle'
}

person_1 = {
	'first': 'Marie',
	'last': 'Lee',
	'age': '17',
	'city': 'Boston'
}

person_2 = {
	'first': 'Natalie',
	'last': 'Rice',
	'age': '32',
	'city': 'Amsterdam'
}

people = []
people.append(person_0)
people.append(person_1)
people.append(person_2)

for person in people:		
	print(f"The name of the person is {person['first']}.")
	print(f"The last_name of the person is {person['last']}.")
	print(f"The age of the person is {person['age']}.")
	print(f"The city of the person is {person['city']}.")