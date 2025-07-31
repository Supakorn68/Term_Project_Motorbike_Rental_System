def print_all(*args):
    for index, arg in enumerate(args):
        print(f"Argument {index + 1}: {arg}")

# Example usage
print_all("Python", 3.8, True, [1, 2, 3,], {"key": "value"})
# Output:
# Argument 1: Python
# Argument 2: 3.8
# Argument 3: True
# Argument 4: [1, 2, 3]
# Argument 5: {'key': 'value'}