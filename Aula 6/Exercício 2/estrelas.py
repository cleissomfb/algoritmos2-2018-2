
class Estrela:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.velocidade = 0

    def set_coordenadaX(self, coordenadaX):
        if coordenadaX >= 0 and coordenadaX <= 800:
            self.x = coordenadaX
        elif coordenadaX < 0:
            self.x = 0

    def set_coordenadaY(self, coordenadaY):
        if coordenadaY >= 0 and coordenadaY <= 600:
            self.y = coordenadaY
        elif coordenadaY < 0:
            self.Y = 0

    def set_velocidade(self, vel):
        if vel >= 0 and vel <= 3:
            self.velocidade = vel

    def get_coordendaX(self):
        return self.x

    def get_coordendaY(self):
        return self.y

    def get_velocidade(self):
        return self.velocidade
