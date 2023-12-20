def sum_of_natural_numbers(n):
    # Formula for the sum of the first n natural numbers: sum = n * (n + 1) / 2
    return n * (n + 1) // 2

# Example: Calculate the sum of the first 10 natural numbers
n = 10
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")
