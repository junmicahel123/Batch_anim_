#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

#Define a function `custom_capitalize` that capitalizes the first letter of a string.
#Convert the first character to uppercase if it is a letter.
#Convert the rest of the string to lowercase.
#Return the modified string.


def custom_capitalize(s):
    if not s:
        return ""
    return (s[0].upper() if 'a' <= s[0] <= 'z' else s[0]) + s[1:].lower()

input_string = input("Enter a string: ")
output_string = custom_capitalize(input_string)
print(f"Modified: '{output_string}'")
