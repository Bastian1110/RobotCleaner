from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

from robot import Robot
from trash import Trash


class Clean(Model):
    def __init__(self, height=9, width=9):
        self.schedule = SimultaneousActivation(self)

        self.grid = MultiGrid(height, width, torus=False)

        for i in range(10):
            robot = Robot(i, (1, 1), self)
            self.grid.place_agent(robot, (1, 1))
            self.schedule.add(robot)

        for (contents, x, y) in self.grid.coord_iter():
            if self.random.random() < 0.5 and self.grid.is_cell_empty((x, y)):
                trash = Trash((x, y), self)
                self.grid.place_agent(trash, (x, y))
                self.schedule.add(trash)

        self.running = True

    def step(self):
        self.schedule.step()
