# Define the lambda function
max_min_lambda = lambda lst: (max(lst), min(lst)) if lst else (None, None)

# Sample input
sample_list = [10, 6, 8, 90, 12, 56]

# Call the function
result = max_min_lambda(sample_list)

print(f"Input:  {sample_list}")
print(f"Output: {result}")