# enemy.py

class Enemy:
    def __init__(self, name, health, attack_power):
        """
        Initialize the enemy with a name, health, and attack power.
        
        :param name: The enemy's name
        :param health: The enemy's health
        :param attack_power: The enemy's attack power (damage it can inflict)
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        """
        Attack the player, reducing their health by the enemy's attack power.
        """
        print(f"{self.name} attacks {player.name} for {self.attack_power} damage!")
        player.take_damage(self.attack_power)

    def take_damage(self, damage):
        """
        Reduce the enemy's health when they take damage.
        """
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Current health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated.")

    def is_alive(self):
        """
        Check if the enemy is still alive.
        """
        return self.health > 0
