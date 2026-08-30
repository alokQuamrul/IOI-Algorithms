string1 = "Hello Python"

multiLineString = """
Generalized Syntax:
variable = my_string.method_name() 
"""

#Capitalizing
text = "problem solving is awesome"
capitalized_text = text.capitalize()
print(capitalized_text)

#title case
print(text.title())

text2 = "pYtHoN Is cOoL"
lowercased_text = text2.lower()
print(lowercased_text)
uppercased_text = text2.upper()
print(uppercased_text)

is_lower = text.islower()
print(is_lower)
is_upper = text.isupper()
print(is_upper)

#Swapping case
print(text2.swapcase())

#checking alpha numerics
number = "pi:3141592"
print("Returns True if there is any alphabets or Numbers else False if there is any other kind of special characters :", number.isalnum()) #This checks both alphabets or numbers

digit = "12334"
print("String Digit Checking:", digit.isdigit())

#removing whitespaces from  a string
text = " hello    "
print(text.strip())#full strip
print(text.rstrip())#right strip


#replacing caharacter in a string
text3 = "I love to solve problems because it makes storms in my brain"
print(text3.replace("storms in my brain","branstorming"))

#Joining string from an iterable
"""
syntax:
separator.join(iterable)
iterable: arrays(list, tuple, array), strings
"""
string_list = ["Early", "to", "bed", "early", "to", "rise", "makes", "a", "man", "healthy", "wealthy", "and",  "wise"]
print(" ".join(string_list))
print("=>".join(string_list))
print("".join(string_list))

#counting the substrings
my_string = "python is pythonic and python rocks"
print(my_string.count("python"))
print(my_string.count("o"))

#Finding Out the ascii/unicodes of a character
my_text = input("Enter a character:")
print(ord(my_text)) #every character gets converted into the integers
