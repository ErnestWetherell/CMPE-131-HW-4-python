def allcaps(func):
    def wrapper():
        result = func()           # Call the original function
        if isinstance(result, str):
            return result.upper()  # Convert to uppercase
        return result              # Return as-is if not a string
    return wrapper
