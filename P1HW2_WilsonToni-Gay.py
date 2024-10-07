# Toni-Gay Wilson
# 09/23/24
# P1HW2
# Calculates and displays travel expenses

# User input of travel info
budget = float(input("Enter budget: "))
destination = input("Enter travel destination: ")
gas_amount = float(input("Enter amount that will be spent of gas: "))
accommodation = float(input("How much will be spent on accommodations: "))
food_amount = float(input("How much will be spent on food: "))
print()
print("---------- Travel Expenses ----------")
print()
print("Location: ", destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas_amount)
print("Accommodation: ", accommodation)
print("Food: ", food_amount)
print()
total = budget - (gas_amount+accommodation+food_amount)
print(f"Remaining Balance: ${total:.2f}")
