# ranged_weapon.py
from weapon import Weapon

class Bow(Weapon):
    def __init__(self):
        super().__init__(name="Bow", description="A bow that can shoot arrows from a distance.", damage=8, weapon_type="ranged", range=5)

    def use(self, player):
        """
        Equip the bow for ranged combat.
        Ranged weapons have longer range but typically deal less damage.
        """
        print(f"{player.name} equips the {self.name}. It deals {self.damage} damage from a distance (Range: {self.range}).")
        # As with melee, you could add more game logic here for equipping the weapon or enhancing the player's stats.

    def attack(self, enemy, distance):
        """
        Attack an enemy with the bow, considering the distance.
        """
        if distance <= self.range:
            if enemy.is_alive():
                print(f"{enemy.name} is shot with an arrow for {self.damage} damage from a distance of {distance} units!")
                enemy.take_damage(self.damage)
        else:
            print(f"The enemy is too far away! The bow has a range of {self.range} units.")
