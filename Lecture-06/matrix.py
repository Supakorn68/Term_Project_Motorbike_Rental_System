matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][1] = 10
print(matrix)
# Output:
# [
#  [1, 10, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]
print("\nIterating through the matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print() 