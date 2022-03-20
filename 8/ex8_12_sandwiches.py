def make_sandwich(*foods):
	print("\nMaking a sandwich with: ")
	for food in foods:
		print(f" - {food}")

make_sandwich('chicken')
make_sandwich('extra cheese', 'vegetable')
make_sandwich('beef', 'egg', 'lattace')