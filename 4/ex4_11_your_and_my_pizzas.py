pizzas = ['pepperoni', 'cheese', 'sausage']
for pizza in pizzas:
	print(f"I like {pizza} pizza.")
print("I really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append('vegan')
friend_pizzas.append('chicken')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)