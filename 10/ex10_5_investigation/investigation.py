while(True):
	reason = input("Why do you like programming? ")
	if reason == 'exit':
		break
	with open('reason.txt', 'a') as file_object:
		file_object.write(reason)
		file_object.write('\n')