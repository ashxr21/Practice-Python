
#*         You received a raw, corrupted text string from an old database export. 
#*          Your task is to write a Python program that converts the messy string into a clean, human-readable sentence.

messyString = "968-Maria, ( D@t@ Engineer ) ;; 27y"

name = messyString.split("-")[1:].split(",")[0].strip().lower()
role = messyString.split("(")[1:].split(")")[0].replace("@", "a").strip().lower()
age = messyString.split(";;")[1:].split("y")[0].strip()

print(f"name: {name} | role: {role} | age: {age}")