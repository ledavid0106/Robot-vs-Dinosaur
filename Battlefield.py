from Dinosaur import Dinosaur
from Robot import Robot


class Battlefield:
    def __init__(self):
        self.robot = Robot("Terminator")
        self.dinosaur = Dinosaur("Troodon", 40)
    
    def run_game(self):
        Battlefield.display_greeting()
        Battlefield().battle_phase()


    def display_greeting():
        print("Welcome to the Past Vs the Future! \nOnly one can be left standing")

    def battle_phase(self):
        while (self.dinosaur.health<=0) or (self.robot.health<=0):
            # self.robot.health = (self.robot.health - self.dinosaur.attack_power)
            self.dinosaur.attack(self.robot)    
            print(f"{self.dinosaur} attacked {self.robot} dealing {self.dinosaur.attack_power} damage!")
            print(f"{self.robot} has {self.robot.health} health remaining.")
            print()
            # self.dinosaur.health = (self.dinosaur.health - self.robot.active_weapon.attack_power)
            self.robot.attack(self.dinosaur)
            print(f"{self.robot} attacked {self.dinosaur} dealing {self.robot.active_weapon.attack_power}!")
            print(f"{self.dinosaur} has {self.dinosaur.health} health remaining!")
            Battlefield.display_winner()

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print("The battle of the ages has concluded! Robot has won!")
        if self.robot.health <= 0:
            print("The battle of the ages has concluded! Dinosaur has won!")

            
