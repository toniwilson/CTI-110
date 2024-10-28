# While Loop Examples

# Program only runs if user says yes
user_choice = input("Wanna run the program? ").lower()
while user_choice == "yes":
    print("^:^" * 10)
    print("The program is running")
    print()
    user_choice = input("Run Again? ").lower()

# Loop Breaks
print("Thanks for using the program, bye!!!")

# Numeric variable to control loop
controller = 0

max_value = int(input("Enter max value: "))

while controller <= max_value:
    # Add one to controller
    print(controller)
    controller += 1

# Loop Breaks
print(f"Loop broke because controller hit max value")
print("Controller is ", controller)
