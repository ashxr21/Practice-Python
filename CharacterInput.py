
#*      Create a program that asks the user to enter their name and their age. 
#*      Print out a message addressed to them that tells them the year that they will turn 100 years old. 

name = (input("Enter your name: "))

age = int(input("Enter your age: "))

currentYear = 2026
prediction = currentYear - age + 100

print(f"Hello {name}!, You will be turning 100 years old in the year: {prediction}")