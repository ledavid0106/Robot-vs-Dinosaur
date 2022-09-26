from Robot import Robot



robo1 = Robot("Terminator")
robo2 = Robot("Danimal")
robo3 = Robot("Dan")


class Fleet:
    def __init__(self, robo1, robo2, robo3):
        self.robo_list = [robo1, robo2, robo3] 
