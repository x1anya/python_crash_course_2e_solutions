guestname = input("Please input your name: ")
with open('guest.txt', 'a') as file_object:
	file_object.write(guestname)