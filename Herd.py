from dinosaur import Dinosaur



class Herd:
    def __init__(self):
        self.dino = []
        self.herd()

    def herd(self):
        Dino1 = Dinosaur("Troodon", 40)
        Dino2 = Dinosaur("Pterodactyls", 50)
        Dino3 = Dinosaur("TRex", 70)

        self.dino.append(Dino1)
        self.dino.append(Dino2)
        self.dino.append(Dino3)

    def removal2(self):
        if self.dino[0].health <= 0:
            self.dino.remove(self.dino[0])