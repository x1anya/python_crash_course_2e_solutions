favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

investigation = ['jen', 'phil', 'mary', 'john']

for person in investigation:
	if person in favorite_languages.keys():
		print(f"Dear {person.title()}, thank you for taking the investigation!")
	else:
		print(f"Dear {person.title()}, we kindly invite you to take the investigation!")