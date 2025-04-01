#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# Function custom_islower(string):
#     For each character in the input string:
#         If character is an uppercase letter:
#             Return False
#     Return True (if no uppercase letters found)

def custom_islower(string):
    for char in string:
        if 'A' <= char <= 'Z':  
            return False
    return True


text = input("Enter the string: ")
result = custom_islower(text)
print("Is the string lowercase?", result)