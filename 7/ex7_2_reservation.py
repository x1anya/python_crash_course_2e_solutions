number = input("How many guests are there for the reservation? ")
number = int(number)

if number <= 8:
	print("We will prepare a table for you!")
else:
	print("Sorry, we don't have a table big enough for you!")