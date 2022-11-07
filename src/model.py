from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import Grid

from robot import Robot
from trash import Trash


class Clean(Model):
    def __init__(self, height=50, width=50):
        self.schedule = SimultaneousActivation(self)

        self.grid = Grid(height, width, torus=True)

        robot = Robot((25, 25), self)
        self.grid.place_agent(robot, (25, 25))
        self.schedule.add(robot)

        for (contents, x, y) in self.grid.coord_iter():
            if self.random.random() < 0.7 and self.grid.is_cell_empty((x, y)):
                trash = Trash((x, y), self)
                self.grid.place_agent(trash, (x, y))
                self.schedule.add(trash)

        self.running = True

    def step(self):
        self.schedule.step()
