
from fleet import *
from herd import *

class TeamBattle:
    def __init__(self):
        self.robos = Fleet()
        self.herds = Herd()
    
    def run_game(self):
        self.display_greeting()
        print()
        self.battle_phase()


    def display_greeting(self):
        print("Welcome to the Past Vs the Future! \nOnly one team can be left standing")

    def battle_phase(self):
        
        while len(self.herds.dino) >= 0 and len(self.robos.robots) >= 0:

            if (self.display_winner()) == True:
                break                    
            if self.herds.dino[0].health > 0:
                self.herds.dino[0].attack(self.robos.robots[0])  
                self.robos.removal()  
            print()
            if (self.display_winner()) == True:
                break
            #Reason for having it break in two places is because when one of the robos or dinos get removed from the list at the end, there is no longer any index thus it will return an error. To work around this I went with the break.
            #originally wanted to work with the while condition to break the loop but it doesnt work if robos lose since the list will be empty as it goes to the second half of the loop
            if self.robos.robots[0].health > 0:
                self.robos.robots[0].weapon_change()
                print()
                self.robos.robots[0].attack(self.herds.dino[0])
                self.herds.removal2()

            print()

    def display_winner(self):
        if len(self.herds.dino) <= 0:
            print(f"The battle of the ages has concluded! Team robots has won!")
            return True
        if len(self.robos.robots) <= 0:
            print(f"The battle of the ages has concluded! Team Dinos has won!")
            return True




# run = TeamBattle()
# run.run_game()
                # print(f"{self.herds.dino[0].name} attacked {self.robos.robots[0].name} dealing {self.herds.dino[0].attack_power} damage!")
                # print(f"{self.robos.robots[0].name} has {self.robos.robots[0].health} health remaining.")
                # print(f"{self.robos.robots[0].name} attacked {self.herds.dino[0].name} using {self.robos.robots[0].active_weapon.name} dealing {self.robos.robots[0].active_weapon.attack_power} damage!")
                # print(f"{self.herds.dino[0].name} has {self.herds.dino[0].health} health remaining!")