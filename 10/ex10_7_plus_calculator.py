while True:
	num1 = input("Number 1: ")
	if num1 == 'q':
		break
	num2 = input("Number 2: ")
	if num2 == 'q':
		break
	try:
		sum = int(num1) + int(num2)
	except ValueError:
		print("One of your numbers is not an integer!")
	else:
		print(sum)