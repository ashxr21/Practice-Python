#* PYTHON CHALLENGE 1
#* Check if a user's name is not empty and the age is greater than or equal to 18
#* it will return True if both conditions are met, otherwise it will return False

user = input("Enter your name: ")
print(user is not None and user != "")

#* PYTHON CHALLENGE 2
#* Check if the password is at least 8 characters long and does not contain spaces
#* it will return True if both conditions are met, otherwise it will return False
password = input("Enter your password: ")
print(len(password) >= 8 and " " not in password)  

#* PYTHON CHALLENGE 3
#*  Check if a user's email is not empty, contains '@', and ends with '.com
#* it will return True if all conditions are met, otherwise it will return False
user_email = input("Enter your email: ")
print(user_email is not None and user_email != "" and "@" in user_email and user_email.endswith(".com"))

#* PYTHON CHALLENGE 4
#* Check if a username is a string, is not None, and is longer than 5 characters
#* it will return True if all conditions are met, otherwise it will return False
username = input("Enter your username: ")
print(isinstance(username, str) and username is not None and len(username) > 5)

#* PYTHON CHALLENGE 5
#* Check if the user is either an admin or a moderator,
#* and either they're not banned or they've verified their email
#* it will return True if all conditions are met, otherwise it will return False
userRole = input("Enter your role (admin/moderator/user): ")
isBanned = input("Are you banned? (yes/no): ").lower() == "yes"
isEmailVerified = input("Is your email verified? (yes/no): ").lower() == "yes"
print((userRole == "admin" or userRole == "moderator") and (not isBanned or isEmailVerified))   