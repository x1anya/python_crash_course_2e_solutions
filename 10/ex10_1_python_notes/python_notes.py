with open('learning_python.txt') as file_object:
	print("First:")
	contents = file_object.read()
	print(contents)

with open('learning_python.txt') as file_object:
	print("Second:")
	for line in file_object:
		print(line.rstrip())

with open('learning_python.txt') as file_object:
	lines = file_object.readlines()

print("Third:")
for line in lines:
	print(line.rstrip())

