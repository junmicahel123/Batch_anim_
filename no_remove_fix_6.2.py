#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.


# Define a function `custom_removeprefix` that removes a given prefix from a string.
# chfeck if the string starts with the given prefix.
# If it does, return the substring excluding the prefix.
# Otherwise, return the original string.


def custom_removeprefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix):]
    return s

input_string = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")
output_string = custom_removeprefix(input_string, prefix)
print(f"Original: '{input_string}'")
print(f"Modified: '{output_string}'")
