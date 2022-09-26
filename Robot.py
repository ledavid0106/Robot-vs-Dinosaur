from Weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Sword", 40)
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
    def weapon_change(self):
        change = input(f"What weapon would you like {self.name} to use? Sword, Gun, or Dagger\n")
        if change == "Gun":
            self.active_weapon = Weapon("Gun", 50)
        if change == "Dagger":
            self.active_weapon = Weapon("Dagger", 30)
        if change == "Sword":
            self.active_weapon = Weapon("Sword", 40)
 




