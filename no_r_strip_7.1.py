#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function

# FUNCTION custom_rstrip(string):
#     START from last character index
#     WHILE character is a space:
#         MOVE left
#     RETURN substring up to last non-space character

def custom_rstrip(s):
    index = len(s) - 1  
    while index >= 0 and s[index] == ' ':  
        index -= 1  
    return s[:index + 1]  


text = input("Enter a String:  ")
trimmed_text = custom_rstrip(text)
print(f'Original: "{text}"')
print(f'Trimmed: "{trimmed_text}"')