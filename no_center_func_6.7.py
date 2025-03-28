#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# 1. Define a function `custom_center` that centers a string within a specified width.
# 2. Check if the string length is already equal to or greater than the specified width.
# 3. If not, calculate the number of spaces needed on both sides.
# 4. Add extra space to the right if needed to handle odd spacing.
# 5. Return the modified string.


def custom_center(string, width):
    if len(string) >= width:  
        return string
    total_padding = width - len(string)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding  
    return ' ' * left_padding + string + ' ' * right_padding

# Example usage
input_string = input("Enter a string: ")
width = int(input("Enter the total width: "))
output_string = custom_center(input_string, width)
print(f"Modified: '{output_string}'")