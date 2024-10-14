# In class examples of branching

# Get age from the user
user_age = int(input("Gimme your age: "))

# If/Else statements todetermine age group
if user_age >= 65:
    age_group = "Senior Citizen"
elif user_age > 0 and user_age < 5:
    age_group = "Toddler"
elif user_age > 12 and user_age < 20:
    age_group = "Teenager"
else:
    age_group = "Not a Senior Citizen"

# Display results to the user
print(f"You are {user_age} and your age group is: {age_group}")
