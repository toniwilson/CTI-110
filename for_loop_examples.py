# for loop runs a predetermined amount of times (range function & iterate through list)
# while loop runs until a certain condition is met (variable controlled by user input)

# For Loop Examples

# For Loop with Range - one parameter
for item in range (5):
    print(item)
    
print()

# For Loop with Range - two parameters
# range (start, stop) - stop is not inclusive
for banana in range (3,10):
    print(banana)
    
print()

# For Loop with Range - three parameters
# RANGE (start, stop, step) - stop is not inclusive
print("PAIRS OF CATS")
for cat in range (2,21,2):
    print(cat)
    
print()

print("PAIRS OF CATS by 5")
for cat in range (5,21,5):
    print(cat)
    
print()

# Print all values in a list
trees = ["Pine", "Willow", "Palm", "Oak"]

print("Lemme tell ya about trees")

for tree in trees:
    print(tree, "tree")
    print("**********")
    
print()

num_list = [0, -7, 2, 8]

num_sum = 0
for num in num_list:
    #num_sum += num
    num_sum = num_sum + num
# Loop breaks
print("Final Sum is ", num_sum)
