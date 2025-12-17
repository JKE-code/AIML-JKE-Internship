# Find all even numbers from a list - Jayanth

def find_even_numbers(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

numbers = [1, 2, 3, 4, 5, 6]
print("Even Numbers:", find_even_numbers(numbers))

