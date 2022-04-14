from random import randint

class Die:
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print(randint(1, self.sides))

die1 = Die(6)

for _ in range(0, 10):
	die1.roll_die()

die2 = Die(10)

for _ in range(0, 10):
	die2.roll_die()

die3 = Die(20)

for _ in range(0, 10):
	die3.roll_die()
