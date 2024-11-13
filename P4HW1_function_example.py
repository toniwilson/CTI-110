# Similar program to P4HW1

def getItem(items):
    # This part different from HW
    inStore = ["bread", "milk", "eggs", "beef", "pasta", \
               "ham", "cheese", "grapes", "apples", "tomato"]

    # In HW, ask for a float
    userInput = input(f"Enter grocery item #{items+1}: ")
    
    # In HW, make sure userInput between and 100
    # In this program, userInput should be in the list
    while userInput not in inStore:
        print(f"{userInput} is not available.")
        userInput = input(f"Enter grocery item #{items+1}: ")
        
    # In this program & HW, add valid inputs to a list
    return userInput

def displayItems(validItems):
    # Display for HW, similar to example
    # For loop breaks, no more shopping
    print()
    print("DONE SHOPPING!!!!")
    print()
    print()
    print("Here are the items you purchased!")
    print("---" * 10)
    for valid_item in validItems:
        print(valid_item)

def main():
    # Get the number of items from user
    userNum = int(input("How many items do you want to purchase? "))

    # Empty list to hold valid items
    validItems = []

    # For loop to allow user to enter items
    for items in range(0, userNum):
        validItems.append(getItem(items))
        print (validItems)
    print(f"The final list is: {validItems}")

    displayItems(validItems)

if __name__ == "__main__":
    main()
