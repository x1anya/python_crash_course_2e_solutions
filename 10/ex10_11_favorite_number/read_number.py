import json

with open('favorite.json') as f:
	favorite = json.load(f)
	print(f"I know your favorite number! It's {favorite}.")
