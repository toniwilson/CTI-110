# Wilson Toni
# 11-18-2024
# P5_HW
# Game

# Import libraries
import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def create_character():
    print_slow("Create Your Character 🏴‍☠️")
    character = {}

    name = input("Enter your character's name: ")
    hp = random.randint(100, 200)
    attack = random.randint(50, 100)
    defense = random.randint(20, 50)

    character = {
        "name" : name,
        "hp" : hp,
        "attack" : attack,
        "defense" : defense,
        "inventory" : [],
        "visited_paths" : []
    }
    return character

def display_character_status(character):
    print("\nCharacter Status")
    print(f"Name:{character['name']}")
    print(f"HP : {character['hp']}")
    print(f"Attack : {character['attack']}")
    print(f"Defense: {character['defense']}")
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

    print_slow("You come across a dark and eerie cave...")
    time.sleep(1)

    while True:
        print_slow("You approach slowly. Cautious steps turned into paniced ones at the sound of unsettling howls.")
        cave_choice = input("Would you like to enter the cave? (yes/no): ").lower()

        if cave_choice == 'yes':
            if random.random() < 0.5:
                treasure = random.choice(['Shield🛡️', 'Jeweled Dagger ⚔️', 'Mystic Amulet ✨'])
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

    while True:
        bridge_choice = input("\nYou see the bridge has two paths. Would you like to 'cross' or 'look around'? ").lower()

        if bridge_choice == 'look around':
            print_slow("\nYou stand still and observe the area around.")
            time.sleep(1)

            print_slow("\nYou find a safer route and continue on with your adventure.")
            time.sleep(1)

            return

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
    
def mountain_path(character):

    print_slow("You find yourself climbing the steep mountains...")
    time.sleep(1)

    print_slow("You come across an old mansion")
    time.sleep

    while True:
        mountain_choice = input("Which door would you like to go through? 'WHITE DOOR', 'BLUE DOOR', RED DOOR': ").lower()
        
        if mountain_choice == 'white door':
            print_slow("\nA bright light blinds you for a minute...")
            print_slow("\nThe screen flashes ⚠️ WARNING ⚠️")
            print_slow("\nHeadset battery low. Game Over!")
            time.sleep(1)

            return
        elif mountain_choice == 'blue door':
            print_slow("\nYou have found the treaure room!")
            time.sleep(1)
            
            treasures = [
                "sword",
                "jeweled dagger",
                "mystic amulet"
            ]
            treasure = random.choice(treasures)

            character['inventory'].append(treasure)
            print_slow(f"You discovered a {treasure}!")
            print_slow(f"{treasure} has been added to your inventory.")
            display_character_status(character)
            return character
        elif mountain_choice == 'red door':
            print_slow("\n OH NO! You've triggered a trap.")
            time.sleep(1)

            print_slow("GAME OVER!!!")
            return
        else:
            print("\nInvalid choice. Try again!")
        return character

def final_boss_battle(character):
    print_slow("\n🔥 THE FINAL BOSS APPEARS! 🔥")
    time.sleep(1)

    boss = {
        "name" : "Island Guardian 👹",
        "hp" : 200,
        "attack" : 25,
        "defense" : 15
    }

    print_slow(f"\nThe {boss['name']} challenges you to battle!")
    display_character_status(character)

    print_slow("\nYou approach the final boss...")
    time.sleep

    if not character['inventory']:
        print_slow("\n You have no items to help you in this battle!")
    else:
        print_slow("\n Your collected treasures begin to glow....")
        time.sleep(1)
    
        for item in character['inventory']:
            if "Jeweled Dagger" in item:
                character['attack'] += 15
                print_slow(f"\n {item} increases your attack!")
            elif "Shield" in item:
                character['defense'] += 10
                print_slow(f"\n {item} increases your defense!")
            elif "Mystic Amulet" in item or "Artifact" in item:
                character['attack'] += 10
                character['defense'] += 5
                print(f"\n {item} enhances your power!")
        display_character_status(character)

    # battle loop
    while boss['hp'] > 0 and character['hp'] > 0:
        # character's turn
        damage_to_boss = max(0, random.randint(10, character['attack']) - boss['defense'])
        boss['hp'] -= damage_to_boss
        print(f"\n⚔️ You deal {damage_to_boss} damage to {boss['name']}!")
        print(f"Boss HP: {boss['hp']}")
       
        if boss['hp'] <= 0:
            print("\n🎉 CONGRATULATIONS! 🎉")
            print("You've defeated the Island Guardian!")
            print("You are now the master of Treasure Island! 👑")
            character['game_complete'] = True
            return character

        damage_to_character = max(0, random.randint(15, boss['attack']) - character['defense'])
        character['hp'] -= damage_to_character
        print(f"\n💥 {boss['name']} deals {damage_to_character} damage to you!")
        display_character_status(character)
        
        time.sleep(1)
    
    if character['hp'] <= 0:
        print("\n💀 The Island Guardian was too powerful...")
        print("Game Over!")
    
    return character

def main ():
    character = create_character()
    character['game_complete'] = False
    display_character_status(character)

    print_slow(f"\nWelcome, {character['name']} to Treasure Island! 🏝️")
    time.sleep(1)
    print("\n\n\n")

    print_slow("You find yourself on a mysterious island and you are to make choices on which paths you would like to take.")
    time.sleep(1)

    while True:
        if character['game_complete']:  # Check if game is complete
            print("\n🎊 Thank you for playing! You've completed the game! 🎊")
            break

        print_slow("\nChoose your path:")

        if "forest_path" not in character ['visited_paths']:
            print_slow("1. A dark, misty forest path  🌲")
        if "bridge_path" not in character ['visited_paths']:
            print_slow("2. A rickety rope bridge")
        if "mountain_path" not in character ['visited_paths']:
            print_slow("3. A steep mountain route  🏔️")
        print_slow("4. Challenge Final Boss ⚔️")
        print_slow("5. Quit Game ❌")

        choice1 = input("\nWhich path would you like to choose? (1/2/3/4/5): ")

        if choice1 == '1' and "forest" not in character ['visited_paths']:
            character = forest_path(character)
            character['visited_paths'].append("forest")
        elif choice1 == '2' and "bridge" not in character['visited_paths']:
            character = bridge_path(character)
            character['visited_paths'].append("bridge")
        elif choice1 == '3' and "mountain" not in character['visited_paths']:
            character = mountain_path(character)
            character['visited_paths'].append("mountain")
        elif choice1 == '4':
            if len(character['visited_paths']) < 3:
                print("\n⚠️  You should explore more paths before facing the final boss!")
                continue
            character = final_boss_battle(character)
            if character['hp'] <= 0:
                break
        elif choice1 == '5':
            print_slow("Thanks for playing! 👋")
            break
        else:
            print("\n❌ Invalid choice or path already visited!")

        if character['game_complete']:  # Check if game is complete
            print("\n🎊 Thank you for playing! You've completed the game! 🎊")
            break

        if character ['hp'] <= 0:
            print("\n☠️ GAME OVER! Your character is dead! ☠️")
            break

if __name__ == "__main__":
    main()