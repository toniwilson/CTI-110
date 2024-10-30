# Wilsont Toni
# 10-30-2024
# P4LAB2
# Use a for loop and a while loop to display positive multiplication tables

# Create a variable to make the program run the first time
run_again = "yes"

# While loop to control entire program
while run_again == "yes":
    
    # Get input from user
    num = int(input("Enter an integer: "))
    print()
    
    # Check if num is positive
    if num >= 0:
        
        # Loop to print multiplication
        for userNum in range(1,13):
            print(f"{num}*{userNum} = {num*userNum}")

    # If num is negative, tell the user
    else:
        print("Program does not handle negative numbers.")
    print()

    run_again = input("Would you like to run the program again? (yes/no) ").lower()

# Loop break
print("Exiting Program ...")
