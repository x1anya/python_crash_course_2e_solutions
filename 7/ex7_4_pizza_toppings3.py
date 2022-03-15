prompt = "\nEnter some pizza toppings!"
prompt += "\nEnter 'quit' to quit."
while True:
	topping = input(prompt)
	if topping == 'quit':
		break
	else:
		print(f"We will add {topping} to the pizza!")