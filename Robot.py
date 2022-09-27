from Weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Sword", 40)
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f"{self.name} has attacked {dinosaur.name} dealing {self.active_weapon.attack_power} damage!")
        print(f"{dinosaur.name} has {dinosaur.health} health remaining.")        
    def weapon_change(self):
        change = input(f"What weapon would you like {self.name} to use? Sword, Gun, or Dagger\n")
        if change == "Gun":
            self.active_weapon = Weapon("Gun", 60)
        if change == "Dagger":
            self.active_weapon = Weapon("Dagger", 30)
        if change == "Sword":
            self.active_weapon = Weapon("Sword", 40)
 




                # print(f"{self.Robos.robots[0].name} attacked {self.Herds.dino[0].name} using {self.Robos.robots[0].active_weapon.name} dealing {self.Robos.robots[0].active_weapon.attack_power} damage!")
                # print(f"{self.Herds.dino[0].name} has {self.Herds.dino[0].health} health remaining!")


