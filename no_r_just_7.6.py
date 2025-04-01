#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# Function custom_rjust(string, width):
#     Calculate the number of spaces needed by subtracting string length from width
#     If spaces needed is less than or equal to 0:
#         Return string (no padding needed)
#     Else:
#         Concatenate the required number of spaces with the string
#         Return the justified string

def custom_rjust(string, width):
    spaces_needed = width - len(string)
    if spaces_needed <= 0:
        return string
    return " " * spaces_needed + string

text = input("Enter the string: ")
width = int(input("Enter the total width: "))

result = custom_rjust(text, width)
print("Right-justified string:")
print(result)