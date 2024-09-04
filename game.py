# game.py

from dungeon_room import DungeonRoom
from player import Player
from enemy import Enemy
from healing_potion import HealingPotion
from melee_weapon import Sword
from ranged_weapon import Bow

def create_world():
    """
    Create the rooms and connect them.
    """
    room1 = DungeonRoom("\033[3mYou are in a dark, cold room.\033[0m")
    room2 = DungeonRoom("\033[3mThis room is filled with light and strange symbols on the walls.\033[0m")
    
    # Create an enemy in room1
    goblin = Enemy("Goblin", health=30, attack_power=10)
    room1.add_enemy(goblin)

    # Create items in rooms
    potion = HealingPotion(20)
    sword = Sword()  # Melee weapon
    bow = Bow()  # Ranged weapon
    room1.add_item(potion)
    room2.add_item(sword)
    room2.add_item(bow)

    # Connect rooms
    room1.connect_room('north', room2)
    room2.connect_room('south', room1)

    return room1  # Start the game in room1

def begin_game():
        # Create a player
        player_name = input("Enter your character's name: ")
        player = Player(name=player_name)

        current_room = create_world()

        while player.is_alive():
            # Describe the current room
            print(current_room.describe())
            
            # List the enemies and items in the room
            print(current_room.list_enemies())
            print(current_room.list_items())
            
            # List the available exits
            print(current_room.get_exits())

            # Get player input
            action = input("\nWhat would you like to do? ").strip().lower()
            
            if action in current_room.exits:
                current_room = current_room.exits[action]
            elif action == "attack":
                if current_room.enemies:
                    enemy = current_room.enemies[0]
                    print(f"You attack the {enemy.name}!")
                    enemy.take_damage(15)
                    if not enemy.is_alive():
                        current_room.enemies.remove(enemy)
                    else:
                        enemy.attack(player)
                else:
                    print("There are no enemies here.")
            elif action.startswith("use"):
                # Use an item (e.g., "use healing potion")
                item_name = action.split("use ")[-1]
                player.use_item(item_name)
            elif action.startswith("pick up "):
                item_name = action[8:]  # Extract the item name from the command
            # Check if an item with this name exists in the room
                for item in current_room.items:
                    if item.name.lower() == item_name.lower():  # Compare by item name (case-insensitive)
                        current_room.items.remove(item)  # Remove the item object from the room
                        player.add_item(item)  # Add the item object to the player's inventory
                        print(f"You picked up {item.name}")
                        break
                else:
                    print(f"{item_name} is not in the room.")
            elif action == "quit":
                print("Exiting to main menu...")
                break
            else:
                print("Invalid action. Try moving in a direction, 'attack', 'pick up [item]', 'use [item]', or 'quit'.")


def main():
    """
    Main game loop.
    """
    print("\033[1m\033[36mWelcome to the Dungeon Crawler Game!\033[0m")
    print()
    while True:
        print("--- Main Menu ---")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            begin_game()
        elif choice == "2":
            print("Thanks for playing! Goodbye.")
            break
    
    

if __name__ == "__main__":
    main()
