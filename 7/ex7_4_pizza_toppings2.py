prompt = "\nEnter some pizza toppings!"
prompt += "\nEnter 'quit' to quit."
active = True
while active:
	topping = input(prompt)
	if topping == 'quit':
		active = False
	if active:
		print(f"We will add {topping} to the pizza!")
	