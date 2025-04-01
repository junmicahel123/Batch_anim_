#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# Function custom_removesuffix(string, suffix):
#     If string ends with suffix:
#         Remove the suffix from the string
#         Return the modified string
#     Else:
#         Return the original string

def custom_removesuffix(string, suffix):
    if string.endswith(suffix):
        return string[:len(string) - len(suffix)]
    return string


text = input("Enter the string: ")
suffix = input("Enter the suffix to remove: ")

result = custom_removesuffix(text, suffix)
print("Result:", result)