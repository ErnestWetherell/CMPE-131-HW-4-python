def my_steps(n):
    # Check bounds
    if n < 1 or n > 25:
        raise ValueError("Input out of bounds. Must be between 1 and 25.")
    
    # Base cases
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    # Iterative Fibonacci-like solution
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
