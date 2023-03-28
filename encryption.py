##This python program encrypts a message from user input based on a specified distance value; using the cipher technique.
##Marwan Abdeladyem 3/27/2023
##1.0
message = input("Enter a message: ")
distanceValue = int(input("Enter distance value: "))
result = ""
for char in message:
    result += chr(ord(char)+distanceValue)
print(""+result)
