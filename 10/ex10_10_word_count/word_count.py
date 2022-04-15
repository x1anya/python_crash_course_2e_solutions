try:
	with open('alice.txt') as file_object:
		contents = file_object.read()
except FileNotFoundError:
	pass
else:
	number1 = contents.lower().count('the')
	print(number1)
	number2 = contents.lower().count('the ')
	print(number2)