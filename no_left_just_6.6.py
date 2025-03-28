#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# Define a function `custom_ljust` that pads a string with spaces to a specified width.
# Check if the string length is already equal to or greater than the specified width.
# If not, calculate the number of spaces needed and append them to the string.
# Return the modified string.

def custom_ljust(string, width):
    if len(string) >= width: 
        return string
    return string + ' ' * (width - len(string)) 

input_string = input("Enter a string: ")
width = int(input("Enter the total width: "))
output_string = custom_ljust(input_string, width)
print(f"Modified: '{output_string}'")
