while(True):
	guestname = input("Please enter your name: ")
	if guestname == 'exit':
		break
	print(f"Welcome to our place, my guest {guestname}!")
	with open('guest_book.txt', 'a') as file_object:
		file_object.write(guestname)
		file_object.write('\n')