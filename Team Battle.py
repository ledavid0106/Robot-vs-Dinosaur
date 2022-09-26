from Dinosaur import Dinosaur
from Fleet import *
from Robot import Robot
from Herd import *

class TeamBattle:
    def __init__(self):
        self.Robos = Fleet()
        self.Herds = Herd()
    
    def run_game(self):
        TeamBattle.display_greeting()
        print()
        self.battle_phase()


    def display_greeting():
        print("Welcome to the Past Vs the Future! \nOnly one team can be left standing")

    def battle_phase(self):
        
        while len(self.Herds.dino) >= 0 and len(self.Robos.robots) >= 0:
    
            if (self.display_winner()) == True:
                break                    
            if self.Herds.dino[0].health > 0:
                self.Herds.dino[0].attack(self.Robos.robots[0])    
                print(f"{self.Herds.dino[0].name} attacked {self.Robos.robots[0].name} dealing {self.Herds.dino[0].attack_power} damage!")
                print(f"{self.Robos.robots[0].name} has {self.Robos.robots[0].health} health remaining.")
                if self.Robos.robots[0].health <= 0:
                    self.Robos.robots.remove(self.Robos.robots[0])
            print()
            if (self.display_winner()) == True:
                break
            if self.Robos.robots[0].health > 0:
                self.Robos.robots[0].weapon_change()
                print()
                self.Robos.robots[0].attack(self.Herds.dino[0])
                print(f"{self.Robos.robots[0].name} attacked {self.Herds.dino[0].name} using {self.Robos.robots[0].active_weapon.name} dealing {self.Robos.robots[0].active_weapon.attack_power} damage!")
                print(f"{self.Herds.dino[0].name} has {self.Herds.dino[0].health} health remaining!")
                if self.Herds.dino[0].health <= 0:               
                    self.Herds.dino.remove(self.Herds.dino[0])
            print()

    def display_winner(self):
        if len(self.Herds.dino) <= 0:
            print(f"The battle of the ages has concluded! Team Robots has won!")
            return True
        if len(self.Robos.robots) <= 0:
            print(f"The battle of the ages has concluded! Team Dinos has won!")
            return True

Past_Vs_Future = TeamBattle()
Past_Vs_Future.run_game()
