# Toni-Gay Wilson
# 10/07/24
# P2HW1
# Calculates and displays travel expenses

# User input of travel info
budget = float(input("Enter budget: "))
destination = input("Enter travel destination: ")
gas_amount = float(input("Enter amount that will be spent of gas: "))
accommodation = float(input("How much will be spent on accommodations: "))
food_amount = float(input("How much will be spent on food: "))
print()
print("---------- Travel Expenses ----------")
print(f"{'Location:':<18}{destination:<25}")
print(f"{'Initial Budget:':<18}${budget:<25,.2f}")
print(f"{'Fuel:':<18}${gas_amount:<25,.2f}")
print(f"{'Accommodation:':<18}${accommodation:<25,.2f}")
print(f"{'Food:':<18}${food_amount:<25,.2f}")
print("-------------------------------------")
print()
total = budget - (gas_amount+accommodation+food_amount)
print(f"Remaining Balance: ${total:.2f}")
