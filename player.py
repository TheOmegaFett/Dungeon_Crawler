# player.py

class Player:
    def __init__(self, name, health=100, inventory=[]):
        self.name = name
        self.health = health
        self.inventory = inventory

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Current health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated.")

    def add_item(self, item):
        """
        Add an item to the player's inventory.
        """
        self.inventory.append(item)
        print(f"{item.name} has been added to your inventory.")

    def use_item(self, item_name):
        """
        Use an item from the player's inventory.
        """
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
                self.inventory.remove(item)
                break
        else:
            print(f"You don't have {item_name} in your inventory.")
    
    def get_inventory(self):
        """
        Return a list of items in the player's inventory.
        """
        if not self.inventory:
            return "Your inventory is empty."
        return f"Your inventory: {', '.join(item.name for item in self.inventory)}"

    def is_alive(self):
        return self.health > 0