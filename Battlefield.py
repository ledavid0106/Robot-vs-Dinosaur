from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.robot = Robot("Terminator")
        self.dinosaur = Dinosaur("Troodon", 40)
    
    def run_game(self):
        self.display_greeting()
        print()
        self.battle_phase()


    def display_greeting(self):
        print("Welcome to the Past Vs the Future! \nOnly one can be left standing")

    def battle_phase(self):
        
        while self.dinosaur.health >= 0 and self.robot.health >= 0:
            if self.dinosaur.health >= 0:
                self.dinosaur.attack(self.robot)    
            print()
            if self.robot.health >= 0:
                self.robot.weapon_change()
                self.robot.attack(self.dinosaur)
            print()
            self.display_winner()

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f"The battle of the ages has concluded! {self.robot.name} has won!")
        if self.robot.health <= 0:
            print(f"The battle of the ages has concluded! {self.dinosaur.name} has won!")

                # print(f"{self.dinosaur.name} attacked {self.robot.name} dealing {self.dinosaur.attack_power} damage!")
                # print(f"{self.robot.name} has {self.robot.health} health remaining.")
                # print(f"{self.robot.name} attacked {self.dinosaur.name} using {self.robot.active_weapon.name} dealing {self.robot.active_weapon.attack_power} damage!")
                # print(f"{self.dinosaur.name} has {self.dinosaur.health} health remaining!")