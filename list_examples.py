# Using lists in Python

my_string = "BaNaNas!!*"

# Returns the number of characters in a string
print(len(my_string))
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[5])
print(my_string[6])

# Returns one or more characters from a string
# Ending value is not included
print(my_string[0:6])
print(my_string[0:7])

# Print only the punctuation
print(my_string[7:10])

# Add text to the end of the string
print(my_string + "@@@%$")
print(my_string[2:5])

# Create empty list
my_list = []

day_of_the_week = input("What is today? ")
weather = input("How is the weather? ")
temp = float(input("What is the temperature outside? "))
classes = int(input("How many classes do you have today? "))

#Add variables to the list
my_list.append(day_of_the_week)
my_list.append(weather)
my_list.append(temp)
my_list.append(classes)

# Print my list
print(my_list)

# Get number of values in the list
print(f"The list has {len(my_list)} items.")

num_list = [20, 66.5, 1, 99, 0.2, 100, 7]
print(f"The smallest value is {min(num_list)}")
print(f"The largest value is {max(num_list)}")
print(f"The total value is {sum(num_list)}")
