from Dinosaur import Dinosaur
from Robot import Robot


class Battlefield:
    def __init__(self):
        self.robot = Robot("Terminator")
        self.dinosaur = Dinosaur("Troodon", 40)
    
    def run_game(self):
        Battlefield.display_greeting()
        print()
        Battlefield.battle_phase(self)


    def display_greeting():
        print("Welcome to the Past Vs the Future! \nOnly one can be left standing")

    def battle_phase(self):
        
        while self.dinosaur.health >= 0 and self.robot.health >= 0:
            if self.dinosaur.health >= 0:
                self.dinosaur.attack(self.robot)    
                print(f"{self.dinosaur.name} attacked {self.robot.name} dealing {self.dinosaur.attack_power} damage!")
                print(f"{self.robot.name} has {self.robot.health} health remaining.")
            print()
            if self.robot.health >= 0:
                self.robot.weapon_change()
                self.robot.attack(self.dinosaur)
                print(f"{self.robot.name} attacked {self.dinosaur.name} using {self.robot.active_weapon.name} dealing {self.robot.active_weapon.attack_power} damage!")
                print(f"{self.dinosaur.name} has {self.dinosaur.health} health remaining!")
            print()
            Battlefield.display_winner(self)

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f"The battle of the ages has concluded! {self.robot.name} has won!")
        if self.robot.health <= 0:
            print(f"The battle of the ages has concluded! {self.dinosaur.name} has won!")
