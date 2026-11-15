
#*      Ask the user for a number. 
#*      Depending on whether the number is even or odd, print out an appropriate message to the user.

#*      Extras:
#*              If the number is a multiple of 4, print out a different message.
#*              Ask the user for two numbers: one number to check (call it num) 
#*               and one number to divide by (check). If check divides evenly into num, 
#*               tell that to the user. If not, print a different appropriate message.   

num = int(input("Enter a number: "))
check = int(input("Give me a number to divide by: "))

if num % 4 == 0:
    print(f"{num} is a multiple of 4.")
elif num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

if num % check == 0:
    print(f"{check} divides evenly into {num}.")
else:
    print(f"{check} does not divide evenly into {num}.")        