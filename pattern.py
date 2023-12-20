def print_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Example: Print a right-angled triangle with 5 rows
rows = 5
print_triangle(rows)

