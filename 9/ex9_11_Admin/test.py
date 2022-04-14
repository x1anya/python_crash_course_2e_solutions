import users

privileges = users.Privileges()
admin_user = users.Admin("John", "Doe", privileges)
admin_user.privileges.show_privileges()