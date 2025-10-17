def reverse_sort_dictionary(dictionary):
    # Validate input
    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary.")
    
    # Verify keys and values
    for key, value in dictionary.items():
        if not isinstance(key, str):
            raise TypeError("All keys must be strings (names).")
        if not isinstance(value, tuple) or len(value) < 1:
            raise TypeError("All values must be tuples containing at least one element.")
        if not isinstance(value[0], int):
            raise TypeError("Phone number must be an integer.")
    
    # Sort keys in reverse order (Z → A)
    sorted_names = sorted(dictionary.keys(), reverse=True)
    
    # Build list of (name, phone_number)
    result = []
    for name in sorted_names:
        phone_number = dictionary[name][0]
        result.append((name, phone_number))
    
    return result
