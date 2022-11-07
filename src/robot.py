from mesa import Agent
from random import choice


class Robot(Agent):
    TYPE = 1

    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.x, self.y = pos

    def step(self):
        neighborhood = self.model.grid.get_neighborhood((self.x, self.y), True)
        randomCell = choice(neighborhood)
        print(randomCell)
        if not self.model.grid.is_cell_empty(randomCell):
            if self.model.grid[randomCell].TYPE == 0:
                self.model.grid.remove_agent(self.model.grid[randomCell])
        self.model.grid.move_agent(self, randomCell)
