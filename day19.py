def find_max_min(numbers):
    # Check if the sequence is empty
    if not numbers:
        return None, None
    
    # Initialize max and min with the first element of the sequence
    max_num = numbers[0]
    min_num = numbers[0]
    
    # Loop through the rest of the numbers in the sequence
    for num in numbers:
        # If we find a number larger than our current max, update max_num
        if num > max_num:
            max_num = num
        # If we find a number smaller than our current min, update min_num
        elif num < min_num:
            min_num = num
            
    return max_num, min_num

# --- Example Usage ---
my_list = [34, 12, 78, 2, 45, 99, 23]
maximum, minimum = find_max_min(my_list)

print(f"The sequence is: {my_list}")
print(f"Maximum Number: {maximum}")
print(f"Minimum Number: {minimum}")