"""
    Turns a user-inputted string into pig latin

    Introduction to Python Lists: http://effbot.org/zone/python-list.htm 
"""

orig_string = raw_input("Enter your string here: ")

vowels = [ "a" , "e" , "i" , "o" , "u" ]

suffix = "way"

pig_string = None

if orig_string[0] in vowels:
    pig_string = orig_string + suffix

else:


print pig_string
