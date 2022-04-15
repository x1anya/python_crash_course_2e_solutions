try:
	with open('cats.txt') as file_object:
		contents = file_object.read()
except FileNotFoundError:
	print("There is no file named 'cats.txt'!")
else:
	print(contents)

try:
	with open('dogs.txt') as file_object:
		contents = file_object.read()
except FileNotFoundError:
	print("There is no file named 'dogs.txt'!")
else:
	print(contents)