from mesa import Agent
from random import choice


class Robot(Agent):
    TYPE = 1

    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.x, self.y = pos

    @property
    def neighbors(self):
        return self.model.grid.iter_neighbors((self.x, self.y), True)

    def step(self):
        neighborhood = self.model.grid.get_neighborhood((self.x, self.y), True)
        # Implement the algorithm
