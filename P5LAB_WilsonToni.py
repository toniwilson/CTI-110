# Wilson Toni
# 11-13-2024
# P5LAB
# Simulate a self check out using functions

# Import the random library to use in the program
import random

def disperse_change(change):
    print()
    print(f"Change owed: ${change:.2f}")
    
    change = int(round(change *  100, 2))
    
    if change == 0:
        print("No Change Due")
        
    # Determine how many dollars are needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickles == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else:
            print(f"{num_pennies} Pennies")
    
# Define the main function
def main():
    print("Welcome to the store!")
    # Generate money owed
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${owed:.2f}")

    cashInput = float(input("How much cash will you put in the self-checkout? $"))
    change = cashInput - owed
    change_owed = round(change,2)

    # Call the function to show the change as coins
    disperse_change(change_owed)
    
    
# Call the main
if __name__ == "__main__":
    main()
