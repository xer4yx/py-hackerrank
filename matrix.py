def create_matrix(rows, cols):
    matrix = [[int(input("Enter a value: ").split()) for _ in range(cols)] for _ in range(rows)]
    return matrix

# Get the number of rows and columns from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create the matrix
matrix = create_matrix(rows, cols)

# Print the matrix
for row in matrix:
    print(row)
