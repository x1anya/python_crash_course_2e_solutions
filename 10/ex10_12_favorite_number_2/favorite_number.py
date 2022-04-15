import json

def get_stored_number():
	filename = 'favorite.json'
	try:
		with open(filename) as f:
			favorite = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return favorite

def get_new_number():
	number = input("What's your favorite number? ")
	filename = 'favorite.json'
	with open(filename, 'w') as f:
		json.dump(number, f)
	return number

def print_favorite():
	favorite = get_stored_number()
	if favorite:
		print(f"I know your favorite number! It's {favorite}.")
	else:
		favorite = get_new_number()
		print(f"We will know when you come back.")

print_favorite()