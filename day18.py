def find_max_and_min(numbers):
    # Check if the list is empty
    if not numbers:
        return None, None
    
    # Start by assuming the first number is both the max and min
    max_num = numbers[0]
    min_num = numbers[0]
    
    # Loop through the rest of the numbers in the sequence
    for num in numbers:
        # If we find a number bigger than our current max, update max
        if num > max_num:
            max_num = num
        # If we find a number smaller than our current min, update min
        if num < min_num:
            min_num = num
            
    # Return both results as a pair
    return max_num, min_num

# --- Example Usage ---
my_list = [12, 5, 45, 18, 2, 99, 23]
largest, smallest = find_max_and_min(my_list)

print("The sequence is:", my_list)
print("Maximum number is:", largest)
print("Minimum number is:", smallest)