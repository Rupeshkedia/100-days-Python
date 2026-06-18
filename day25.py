#Find Second Largest Number

numbers = [10, 25, 8, 40, 15]

largest = max(numbers)
numbers.remove(largest)

second_largest = max(numbers)

print("Second Largest Number:", second_largest)