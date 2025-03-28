#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# Define a function `custom_swapcase` that swaps the case of each character in a string.
# Initialize an empty string to store the result.
# Iterate through each character in the input string.
# If the character is uppercase, convert it to lowercase.
# If the character is lowercase, convert it to uppercase.
# Append the modified character to the result string.
# Return the modified string.


def custom_swapcase(string):
    result = ""
    for char in string:
        if 'A' <= char <= 'Z': 
            result += chr(ord(char) + 32) 
        elif 'a' <= char <= 'z':  
            result += chr(ord(char) - 32) 
        else:
            result += char 
    return result


input_string = input("Enter a string: ")
output_string = custom_swapcase(input_string)
print(f"Modified: '{output_string}'")