places = {}
active = True
while active:
	name = input("\nWhat is your name? ")
	place = input("If you could visit one place in the world, where would you go? ")

	places[name] = place

	repeat = input("Would you like to let another person respond? (yes / no)")
	if repeat == 'no':
		active = False
print("\n--- Results ---")
for name, place in places.items():
	print(f"{name} would like to visit {place}.")