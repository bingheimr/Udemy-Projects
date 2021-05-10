def check_palindrome():
    """
    Takes in a string "s" and returns
    True if string is a Palindrome or
    False if not.
    """
    s = input("Please enter a word to check for palindrome status: ")
    if s == s[::-1]:
        print("True")
    else:
        print("False")

check_palindrome()

