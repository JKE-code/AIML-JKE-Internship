# Reverse a string without using reverse() - jayanth

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

string = "HITAM"
print("Reversed String:", reverse_string(string))

