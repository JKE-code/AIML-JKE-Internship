# Find maximum element in a list - Jayanth

def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

numbers = [4, 8, 1, 9, 3]
print("Maximum Element:", find_max(numbers))

