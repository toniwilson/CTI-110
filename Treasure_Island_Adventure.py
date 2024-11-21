# Wilson Toni
# 11-18-2024
# P5_HW
# Game

# Import libraries
import random
import time

def print_slow(text):
    # Text is printed out slowly for dramatic effect
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def create_character():
    print_slow("Create Your Character")
    character = {}

    name = input("Enter your character's name: ")
    hp = random.randint(100, 200)
    attack = random.randint(50, 100)

    character = {
        "name": name,
        "hp" : hp,
        "attack" : attack,
        "inventory" : []
    }

    return character

def display_character_status(character):
    print("\nCharacter Status")
    print(f"Name:{character['name']}")
    print(f"HP : {character['hp']}")
    print(f"Attack : {character['attack']}")
    print(f"Inventory : {', '.join(character['inventory']) if character ['inventory'] else 'Empty'}")

def battle(attacker, defender):
    damage = random.randint(0, attacker['damage'])
    defender['hp'] -= damage
    return defender

def take_damage(character, amount):
    character['hp'] -= amount
    print_slow(f"\n {character['name']} takes {amount} damage!")
    display_character_status(character)
    return character

def add_item(character, newItem):
    character['inventory'].append(newItem)
    print_slow(f"\n {character['name']} found {newItem}!")
    display_character_status(character)

    return character

def forest_path(character):
    print_slow("\nYou enter the dark forest...")
    time.sleep(1)

    print_slow("You come across a dark and eerie cave")
    time.sleep(1)

    print_slow("You approach slowly. Cautious steps turned into paniced ones at the sound of unsettling howls.")
    cave_choice = input("Would you like to enter the cave? (yes/no): ").lower()

    if cave_choice == 'yes':
        if random.random() < 0.4:
            treasure = random.choice(['Ancient Artifact', 'Jeweled Dagger', 'Mystic Amulet'])
            character['inventory'].append(treasure)
            print_slow(f"You discovered a {treasure}!")
            print_slow(f"{treasure} has been added to your inventory.")
            display_character_status(character)
    else:
        treasure_trap = random.choice(['Poisonous Spider'])
        damage = random.randint(15, 35)
        character['hp'] -= damage
        print_slow(f"You discovered a {treasure_trap}!!! You lost {damage} HP!!!")
        display_character_status(character)
    return character

def bridge_path(character):
    bridge_choice = input("\nYou see the bridge has two paths. Would you like to 'cross' or 'look for another path'? ").lower()

    if bridge_choice == 'look for another path':
        print_slow("\nYou stand still and observe the area around, looking for a safer route.")
    elif bridge_choice == 'cross':
        print_slow("\n You decide to cross the bridge despite the decrapid state...")
        time.sleep(1)

        print_slow("\nThe bridge gives out under your weight.")
        time.sleep(1)

        print_slow("\nYou fall impaled on the sharp rocks.")
        time.sleep(1)

        print_slow("\nGAME OVER!!!")

        return
    else:
        print_slow("Invalid choice. Try again!")
    return character

def main ():
    character = create_character()
    display_character_status(character)

    print_slow(f"\nWelcome, {character['name']} to Treasure Island! 🏝️")
    time.sleep(1)
    print("\n\n\n")

    print_slow("You find yourself on a mysterious island and you are to make choices on which paths you would like to take.")
    time.sleep(1)

    print_slow("\nYou see three paths:")
    print_slow("1. A dark, misty forest path")
    print_slow("2. A rickety rope bridge")
    print_slow("3. A steep mountain route")


    choice1 = input("\nWhich path would you like to choose? (1/2/3): ")

    if choice1 == '1':
        forest_path(character)
    elif choice1 == '2':
        bridge_path(character)
    elif choice1 == '3':
        mountain_path(character)
    else:
        print_slow("Invalid choice. The island's magic chooses for you ....")
        bridge_path(character)

    if character ['hp'] <= 0:
        print("\n GAME OVER! Your character is dead!")

    

    
if __name__ == "__main__":
    main()