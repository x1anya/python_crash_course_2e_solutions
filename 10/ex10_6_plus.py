num1 = input("Number 1: ")
num2 = input("Number 2: ")
try:
	sum = int(num1) + int(num2)
except ValueError:
	print("One of your numbers is not an integer!")
else:
	print(sum)