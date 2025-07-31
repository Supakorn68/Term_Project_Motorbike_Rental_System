# input_string = input("Enter a string: ")
# Modifird_String = " "
# vowels = "aeiouAEIOU"

# for char in input_string:
#     upper_char = char.upper ()

#     if upper_char in vowels: 
#         Modifird_String += "*"
#     else:
#         Modifird_String += upper_char

# print("Modifird_String:" , Modifird_String)

input_string = input("Enter a string: ")
Modifird_String = " "
vowels = "AEIOU"

for char in input_string:
    upper_char = char.upper ()

    if char.upper in vowels: 
        Modifird_String += "*"
    else:
        Modifird_String += upper_char

print("Modifird_String:" , Modifird_String)
