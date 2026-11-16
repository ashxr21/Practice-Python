
#*  Create a Python program that:
#*  1. Asks the user to enter their name.
#*  2. Asks the user to enter their numerical grade (0–100).
#*  3. Depending on the grade, print the appropriate message.
#*  Conditions
#*- If the grade is 90 or above, print "Excellent! You got an A."
#*- If the grade is 80–89, print "Great job! You got a B."
#*- If the grade is 75–79, print "You passed! You got a C."
#*- If the grade is below 75, print "Sorry, you failed."

name = input("Enter your name: ")
grade = int(input("Enter your grade: "))

if grade >= 90:
    print(f"Hello {name}!")
    print("Excellent job this semester! You got an A") 
elif grade >= 80 and grade <= 89:
    print(f"Hello {name}!")
    print("Great job this semester! You got a B.") 
elif grade >= 75 and grade <= 79:
    print(f"Hello {name}!")
    print("You passed this semester! You got a C.")
elif grade < 75:
    print(f"Hello {name}!")
    print("Sorry, you failed this semester.")
else:
    print("Invalid grade entered. Please enter a grade between 0 and 100.")