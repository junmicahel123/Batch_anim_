#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

#Define a function `custom_endswith` that checks if a string ends with a given suffix.
# 2. Compare the last characters of the string with the suffix.
# 3. If they match, return True; otherwise, return False.


def custom_endswith(s, suffix):
    if len(suffix) > len(s):  
        return False
    return s[-len(suffix):] == suffix  

input_string = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")
output_result = custom_endswith(input_string, suffix)
print(f"Does the string end with '{suffix}'? {output_result}")
