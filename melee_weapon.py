# melee_weapon.py
from weapon import Weapon

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword", description="A sharp blade for close combat.", damage=10, weapon_type="melee", range=1)

    def use(self, player):
        """
        Equip the sword for close combat.
        Melee weapons usually have short range but higher damage.
        """
        print(f"{player.name} equips the {self.name}. It deals {self.damage} damage at melee range (Range: {self.range}).")
        # Here, you could add more functionality, like changing the player's current weapon or adding an attack bonus.

    def attack(self, enemy):
        """
        Attack an enemy with the sword.
        """
        if enemy.is_alive():
            print(f"{enemy.name} is struck by the sword for {self.damage} damage!")
            enemy.take_damage(self.damage)
