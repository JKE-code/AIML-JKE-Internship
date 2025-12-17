# Create dictionary with number as key and square as value - Jayanth

def square_dictionary(lst):
    result = {}
    for num in lst:
        result[num] = num ** 2
    return result

numbers = [1, 2, 3, 4]
print("Square Dictionary:", square_dictionary(numbers))

