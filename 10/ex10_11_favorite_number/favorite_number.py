import json

favorite = input("What's your favorite number? ")
with open('favorite.json', 'w') as f:
	json.dump(favorite, f)
