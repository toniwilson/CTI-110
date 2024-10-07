# Formating output using the f-string

name = "Toni Wilson"
address = "123 ABC St. Fay, NC"
age = 3
cost = 2500.00432487553
cost_to_feed = 25000.034535439634
isCute = True

# Print the characters 20 times
print("*-" * 26)
print(f"{'Name:':<18}{name:<25}")
print(f"{'Address:':<18}{address:<25}")
print(f"{'Age:':<18}{age:<25}")
print(f"{'Cost To Buy:':<18}${cost:<25,.2f}")
print(f"{'Cost To Feed:':<18}${cost_to_feed:<25,.2f}")
print(f"{'Is Toni cute?':<18}{str(isCute):<25}")
