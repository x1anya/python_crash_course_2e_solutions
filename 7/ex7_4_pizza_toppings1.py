prompt = "\nEnter some pizza toppings!"
prompt += "\nEnter 'quit' to quit."
topping = input(prompt)
while topping != 'quit':
	print(f"We will add {topping} to the pizza!")
	topping = input(prompt)