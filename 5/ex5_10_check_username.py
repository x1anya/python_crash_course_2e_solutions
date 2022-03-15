current_users = ['applepie', 'John', 'MARS', 'natalie', 'lionking']
new_users = ['Mary', 'john', 'mars', 'Stephen', 'story']

backup_users = []
for user in current_users:
	backup_users.append(user.lower())

for user in new_users:
	if user.lower() in backup_users:
		print(f"The username '{user}' has already been used! Please choose another one!")
	else:
		print(f"Congratulations! The username '{user}' has not been used yet.")