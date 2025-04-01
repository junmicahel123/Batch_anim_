#
# Function custom_index(string, substring):
#     Get the length of the substring
#     Loop through the string:
#         If a portion of the string matches the substring:
#             Return the current index
#     If substring is not found:
#         Return -1 (or raise an error if desired)

def custom_index(string, substring):
    sub_len = len(substring)
    
    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == substring:
            return i  
    
    return -1

text = input("Enter the string: ")
sub = input("Enter the substring to find: ")

result = custom_index(text, sub)
if result != -1:
    print("First occurrence index:", result)
else:
    print("Substring not found.")
