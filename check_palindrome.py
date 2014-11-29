user_in = raw_input("Enter your word here: ")

reverse = user_in[::-1]

if reverse == user_in:
    print ("%s is a palindrome.") % user_in
else:
    print ("%s is not a palindrome.") % user_in
