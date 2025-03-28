#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

#  Define a function `custom_isupper` that checks if all characters in a string are uppercase.
#  Iterate through each character in the input string.
#  If any character is a lowercase letter (a-z), return False.
#  If no lowercase letters are found, return True.


def custom_isupper(s):
    for char in s:
        if 'a' <= char <= 'z':  # Check if character is lowercase
            return False
    return True  # Return True if no lowercase letters found

# Example usage
input_string = input("Enter a string: ")
output_result = custom_isupper(input_string)
print(f"Is the string uppercase? {output_result}")