#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# Function custom_upper(string):
#     Initialize an empty result string
#     For each character in the input string:
#         If character is a lowercase letter:
#             Convert it to uppercase by subtracting 32 from its ASCII value
#         Append the character to the result string
#     Return the result string

def custom_upper(string):
    result = ""
    for char in string:
        if 'a' <= char <= 'z':  
            result += chr(ord(char) - 32)  
        else:
            result += char
    return result

# Example usage
text = input("Enter the string: ")
result = custom_upper(text)
print("Uppercase Result:", result)