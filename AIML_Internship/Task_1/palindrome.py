# Check palindrome (string or number) - Jayanth

def is_palindrome(value):
    value = str(value)
    return value == value[::-1]

value = 121
print("Is Palindrome:", is_palindrome(value))

