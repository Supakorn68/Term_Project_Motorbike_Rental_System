# counter = 0 
# def increment():
#     global counter
#     counter += 1

# increment()
# increment()

# print(counter)

counter = 0 
def increment_counter():
     counter = 0
     counter = counter + 1
     print(f"local counter {counter}")

increment_counter()
increment_counter()

print(f"counter incremented{counter}")