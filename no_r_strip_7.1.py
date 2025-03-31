#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function

# FUNCTION custom_rstrip(string):
#     START from last character index
#     WHILE character is a space:
#         MOVE left
#     RETURN substring up to last non-space character

def custom_rstrip(string):
    index = len(string) - 1  
    while index >= 0 and string[index] == ' ':  
        index -= 1  
    return string[:index + 1]  


text = input("Enter a String:")
trimmed_text = custom_rstrip(text)
print(f'Original: "{text}"')
print(f'Trimmed: "{trimmed_text}"')