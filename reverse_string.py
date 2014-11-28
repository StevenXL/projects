"""
    This program will reverse a user inputed string

    This method uses Python's slices to go from beginning to end, backwards:

    Tutorial on Python Strings & Slices: http://www.pythoncentral.io/cutting-and-slicing-strings-in-python/
"""

orig_string = raw_input("Enter your string here: ")

rever_string = orig_string[::-1]

print rever_string
