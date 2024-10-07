# Wilson Toni
# 09/16/2024
# P1HW1
# Using math expressions with user input

print("--------Calculating Exponents--------")
print()
print()
# Get input from user
base_value = input("Enter an integer as the base value: ")

# Convert base_value to integer
base_value = int(base_value)

# Get input from user and convert to integer
exponent = int(input("Enter an integer as the exponent: "))
print()

# Display math results to the user
print(base_value, "raised to the power of", exponent, "is", str(base_value**exponent) + "!!!")
print()
print()
print("--------Addition and Subtraction--------")
print()
print()
# Get integers from user
starting_value = int(input("Enter a starting integer: "))
int_add = int(input("Enter an integer to add: "))
int_subtract = int(input("Enter an integer to subtract: "))
print()
print()
# Calculate the result
result_value = starting_value + int_add - int_subtract

# Display all variables and the result
print(starting_value, "+" ,int_add, "-" ,int_subtract, "is equal to", result_value)
