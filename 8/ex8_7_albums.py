def make_album(singer, name, number=None):
	album = {}
	album['singer'] = singer
	album['name'] = name
	if number:
		album['number'] = number
	return album

print(make_album('Adele', '19'))
print(make_album('Adele', '21', 11))
print(make_album('Adele', '22'))