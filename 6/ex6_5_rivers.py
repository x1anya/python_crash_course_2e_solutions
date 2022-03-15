rivers = {
	'nile': 'egypt',
	'amazon': 'brazil',
	'mississippi': 'america'
}

for k,v in rivers.items():
	print(f"The {k.title()} runs through {v.title()}.")

for k in rivers.keys():
	print(k.title())

for v in rivers.values():
	print(v.title())