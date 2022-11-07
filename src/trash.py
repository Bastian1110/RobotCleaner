from tarfile import DIRTYPE
from mesa import Agent


class Trash(Agent):
    TYPE = 0

    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.x, self.y = pos

    def step(self):
        pass
