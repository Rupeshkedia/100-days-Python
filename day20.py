def fibonacci(n, current=0):
    """Recursive function to print Fibonacci series up to n terms"""
    if current >= n:
        return
    
    # Calculate Fibonacci number at position 'current'
    if current == 0:
        fib_num = 0
    elif current == 1:
        fib_num = 1
    else:
        fib_num = fibonacci_helper(current)
    
    print(fib_num, end=" ")
    fibonacci(n, current + 1)

def fibonacci_helper(k):
    """Helper function to calculate Fibonacci number at position k recursively"""
    if k <= 1:
        return k
    return fibonacci_helper(k - 1) + fibonacci_helper(k - 2)

# Example usage:
n = int(input("Enter number of terms: "))
print(f"Fibonacci series up to {n} terms:")
fibonacci(n)