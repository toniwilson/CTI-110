# Toni Wilson
# 10-02-2024
# P2LAB2
# Using dictionaries

# Create dictionary
cars = {"Camaro":18.1, "Prius":52.36, "Model S":110, "Silverado":26}
print()

# Print all keys in the dictionary
print(cars.keys())
print()

#Get a car (key) from user
userCar = input("Enter a vehicle to see its mpg: ")
print()

# Display mpg for the userCar
print(f"The {userCar} gets {cars[userCar]} mpg.")
print()

# Gte miles to drive from the user
miles_to_drive = int(input(f"How many miles will you drive the {userCar}? "))
print()

# Caluclate gallons of gas needed
gallons_needed = miles_to_drive/cars[userCar]

# Display gallons of gas needed
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {userCar} {miles_to_drive} miles.")
