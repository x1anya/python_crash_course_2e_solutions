sandwich_orders = ['chicken', 'pastrami', 'fish', 'cheese', 'pastrami', 'vegan', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	if sandwich == 'pastrami':
		print(f"{sandwich.title()} is out!")
		while 'pastrami' in sandwich_orders:
			sandwich_orders.remove('pastrami')
	else:
		print(f"I made your {sandwich} sandwich.")
		finished_sandwiches.append(sandwich)

print(finished_sandwiches)
