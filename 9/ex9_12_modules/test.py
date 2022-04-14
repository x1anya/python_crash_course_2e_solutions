import privileges

privilege = privileges.Privileges()
admin_user = privileges.Admin("John", "Doe", privilege)
admin_user.privileges.show_privileges()