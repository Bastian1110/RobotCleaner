from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from robot import Robot
from trash import Trash


class Clean(Model):
    def __init__(self, size=9, robots=3, trashRate=0.5, maxSteps=100):
        self.maxSteps = maxSteps
        self.currentSteps = 0
        self.robots = robots
        self.trashCount = 0
        self.initialTrash = 0

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
                self.trashCount += 1
                self.initialTrash += 1

        self.running = True

    def getPercentage(self):
        return (self.trashCount * 100) / self.initialTrash

    def getTotalMoves(self):
        total = 0
        for (contents, x, y) in self.grid.coord_iter():
            if not self.grid.is_cell_empty((x, y)):
                if self.grid[x, y][0].TYPE == 1:
                    total = total + self.grid[(x, y)][0].movements
        return total

    def step(self):
        if self.currentSteps < self.maxSteps:
            self.schedule.step()
            self.currentSteps += 1
            if self.trashCount == 0:
                print("Steps : ", self.currentSteps, "0% trash left")
        else:
            print(
                "Steps : ",
                self.currentSteps,
                " ",
                self.getPercentage(),
                "% trash left ",
                self.getTotalMoves(),
                " total moves",
            )
