#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# Define a function `custom_lower` that converts all uppercase letters in a string to lowercase.
# Initialize an empty string to store the result.
# Iterate through each character in the input string.
# If the character is an uppercase letter (A-Z), convert it to lowercase using ASCII values.
# Append the converted character to the result string.
# Return the modified string.

def custom_lower(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z': 
            result += chr(ord(char) + 32) 
            result += char 
    return result


input_string = input("Enter a string: ")
output_string = custom_lower(input_string)
print(f"Original: '{input_string}'")
print(f"Modified: '{output_string}'")
