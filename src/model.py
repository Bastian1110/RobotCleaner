from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import Grid

from robot import Robot
from cell import Cell


class Clean(Model):
    def __init__(self, height=50, width=50):
        self.schedule = SimultaneousActivation(self)

        self.grid = Grid(height, width, torus=True)

        robot = Robot((1, 1), self)
        self.grid.place_agent(robot, (1, 1))
        self.schedule.add(robot)

        for (contents, x, y) in self.grid.coord_iter():
            if x != 1 and y != 1:
                cell = Cell((x, y), self)
                if self.random.random() < 0.1:
                    cell.state = cell.DIRTY
                    self.grid.place_agent(cell, (x, y))
                    self.schedule.add(cell)

        self.running = True

    def step(self):
        self.schedule.step()