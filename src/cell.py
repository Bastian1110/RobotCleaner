from tarfile import DIRTYPE
from mesa import Agent


class Cell(Agent):
    TYPE = 0
    CLEAN = 0
    DIRTY = 1

    def __init__(self, pos, model, init_state = CLEAN):
        super().__init__(pos, model)
        self.x, self.y = pos
        self.state = init_state

    @property
    def isDirty(self):
        return self.state == self.DIRTY

    def step(self):
        pass