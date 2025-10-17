def merge_list(list1, list2):
    # Validate inputs
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Inputs must be lists.")
    
    for val in list1 + list2:
        if not isinstance(val, int):
            raise TypeError("All elements must be integers.")
    
    # Combine lists
    merged = list1 + list2
    
    # Manual bubble sort (no built-in sort allowed)
    for i in range(len(merged)):
        for j in range(0, len(merged) - i - 1):
            if merged[j] > merged[j + 1]:
                merged[j], merged[j + 1] = merged[j + 1], merged[j]
    
    return merged
