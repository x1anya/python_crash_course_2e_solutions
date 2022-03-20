def make_album(singer, name, number=None):
	album = {}
	album['singer'] = singer
	album['name'] = name
	if number:
		album['number'] = number
	return album

while True:
	print("You can press 'q' at any time to quit.")
	singer = input("Please enter the name of the singer: ")
	if singer == 'q':
		break
	name = input("Please enter the name of the album: ")
	if name == 'q':
		break
	number = input("Please enter the number of the songs: ")
	if number == 'q':
		break
	print(make_album(singer, name, number))