from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
			'a', 'b', 'c', 'd', 'e']

num1 = choice(lottery)
num2 = choice(lottery)
num3 = choice(lottery)
num4 = choice(lottery)

print(f"You have {num1}{num2}{num3}{num4} on the lottery. You win the prize!")