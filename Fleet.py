from Robot import Robot



class Fleet:
    def __init__(self):
        self.robots = []
        self.fleets()

    def fleets(self):
        robo1 = Robot("Terminator")
        robo2 = Robot("Danimal")
        robo3 = Robot("Dan")

        self.robots.append(robo1)
        self.robots.append(robo2)
        self.robots.append(robo3)