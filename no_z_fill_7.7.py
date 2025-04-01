#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

 # Function custom_zfill(string, width):
#     Calculate the number of zeros needed by subtracting string length from width
#     If zeros needed is less than or equal to 0:
#         Return string (no padding needed)
#     Else:
#         Concatenate the required number of zeros with the string
#         Return the zero-filled string

def custom_zfill(string, width):
    zeros_needed = width - len(string)
    if zeros_needed <= 0:
        return string
    return "0" * zeros_needed + string


text = input("Enter the string: ")
width = int(input("Enter the total width: "))

result = custom_zfill(text, width)
print("Zero-filled string:")
print(result)
