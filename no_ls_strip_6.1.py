#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
# Define a function `custom_lstrip`
# Initialize an index variable to 0.
# Use a while loop to iterate through the string:
#  - If the current character is a space, increment the index.
#    - Stop when a non-space character is found or the end of the string is reached.
# Return the substring starting from the first non-space character.
# Test the function with an example input and print the results.

def custom_lstrip(string):
    index = 0
    while index < len(string) and string[index] == ' ':
        index += 1
    return string[index:]


input_string = input("word?:")
output_string = custom_lstrip(input_string)
print(f"Original: '{input_string}'")
print(f"Modified: '{output_string}'")
