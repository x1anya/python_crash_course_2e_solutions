from random import choice

my_ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
			'a', 'b', 'c', 'd', 'e']

prize1 = 0
prize2 = 8
prize3 = 0
prize4 = 4

number = 0

while(True):
	num1 = choice(my_ticket)
	num2 = choice(my_ticket)
	num3 = choice(my_ticket)
	num4 = choice(my_ticket)

	number += 1

	if num1 == prize1 and num2 == prize2 and num3 == prize3 and num4 == prize4:
		print("You win the prize!")
		break

print(f"{number} loops to get the prize!")