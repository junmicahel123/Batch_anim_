#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# Define a function `custom_title` that capitalizes the first letter of each word in a string.
#  Split the string into words based on spaces.
# Capitalize the first letter of each word and convert the rest to lowercase.
# Join the words back together with spaces.
#  Return the modified string.


def custom_title(string):
    words = string.split()  
    capitalized_words = [(word[0].upper() + word[1:].lower()) if word else "" for word in words]
    return " ".join(capitalized_words)

input_string = input("Enter a string: ")
output_string = custom_title(input_string)
print(f"Modified: '{output_string}'")