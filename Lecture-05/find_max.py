def find_max(*args):
    if not args:
        return None
    max_value = args[0]
    for numder in args:
        if numder > max_value:
            max_value = numder
    return max_value

# Example usage
result = find_max(3, 5, 7, 2, 8)
print(f"the maximum value is: {result}") # Output: the maximumvalue is: 8
