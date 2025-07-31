def format_strings(*args):
    return "".join(args).replace(" ", "-").upper

print(format_strings("Hello", "world", "this", "is", "a", "test"))
print(format_strings("Python", "is", "fun"))
print(format_strings("Concatenate", "these", "these", "strings", "please"))