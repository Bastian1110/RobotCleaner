from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

from robot import Robot
from trash import Trash


class Clean(Model):
    def __init__(self, size=9, robots=3, trashRate=0.5):
        self.schedule = SimultaneousActivation(self)

        self.grid = MultiGrid(size, size, torus=False)

        for i in range(robots):
            robot = Robot(i, (1, 1), self)
            self.grid.place_agent(robot, (1, 1))
            self.schedule.add(robot)

        for (contents, x, y) in self.grid.coord_iter():
            if self.random.random() < trashRate and self.grid.is_cell_empty((x, y)):
                trash = Trash((x, y), self)
                self.grid.place_agent(trash, (x, y))
                self.schedule.add(trash)

        self.running = True

    def step(self):
        self.schedule.step()
