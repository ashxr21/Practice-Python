
#* PYTHON CHALLENGE
#* Validate the Quality and Correctness of Email Values using If, elif, else Statements

#* - Must not be empty
#* - Must contain '.' and '@'
#* - Must contain exactly one '@' symbol
#* - Must end with '.com', '.org', or '.net'
#* - Must not be longer than 254 characters
#* - Must start and end with a letter or digit

email = input("Enter your email address: ")
email = email.strip()
#* Remove leading and trailing whitespace  
if email == "":
    print("Email cannot be empty")
elif "@" not in email or "." not in email:
    print("Email must contain '@' and '.'")
elif email.count("@") != 1:
    print("Email must contain exactly one '@' symbol")
elif email.count(".") != 1:
    print("Email must contain exactly one '.' symbol")
elif not email.endswith((".com", ".org", ".net")):
    print("Email must end with '.com', '.org', or '.net'")
elif len(email) > 254:
    print("Email must not be longer than 254 characters")
elif not (email[0].isalnum() and email[-1].isalnum()):
#* isalnum() - Checks if the string contains only letters and digits
    print("Email must start and end with a letter or digit")
else:
    print("Valid email address")


#* Python Challenge - Validate the Quality and Correctness of Passwords using case match 

#*- Must not be empty
#*- Must be at least 8 characters
#*- Must include at least 1 uppercase
#*- Must include at least 1 lowercase
#*- Must not be same as the email
#*- Must not contain any spaces
#*- Must start and end with a letter or digit

password = input("Enter your password: ")
password = password.strip()  # Remove leading and trailing whitespace

match password:
    case "":
        print("Password cannot be empty")
    case _ if len(password) < 8:
        print("Password must be at least 8 characters")
    case _ if not any(char.isupper() for char in password):
        print("Password must include at least 1 uppercase letter")
    case _ if not any(char.islower() for char in password):
        print("Password must include at least 1 lowercase letter")
    case _ if " " in password:
        print("Password must not contain any spaces")
    case _ if not (password[0].isalnum() and password[-1].isalnum()):
        print("Password must start and end with a letter or digit")
    case _:
        print("Valid password")

