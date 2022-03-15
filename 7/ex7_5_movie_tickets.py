prompt = "\nPlease enter your age: "
prompt += "\nEnter 'quit' to quit."
while True:
	age = input(prompt)
	if age == 'quit':
		break
	age = int(age)
	if age < 3:
		print("You can see the movie for free!")
	elif age >=3 and age <=12:
		print("You should pay 10 dollars for the movie.")
	else:
		print("You should pay 15 dollars for the movie.")