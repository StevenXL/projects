"""
    Counts the number of vowels
"""

user_input = raw_input("Enter your string here: ")

user_input = user_input.lower()

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for char in user_input:
    if char in vowels.keys():
        vowels[char] = vowels[char] + 1

sum = 0

print "=" * 30

for key in vowels.keys():
    print "%s: %d" % (key.upper(), vowels[key])
    sum = sum + vowels[key]

print "Total Vowels: %d" % sum

print "=" * 30
