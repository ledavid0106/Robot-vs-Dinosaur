
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
    def attack(self, robot):
        robot.health -=  self.attack_power
        print(f"{self.name} has attacked {robot.name} dealing {self.attack_power} damage!")
        print(f"{robot.name} has {robot.health} health remaining.")



