from mesa import Agent


class Robot(Agent):
    TYPE = 1

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.x, self.y = pos

    @property
    def neighbors(self):
        return self.model.grid.get_neighbors((self.x, self.y), True)

    def step(self):
        neighborhood = self.model.grid.get_neighborhood((self.x, self.y), True)
        while True:
            randomCell = self.random.choice(neighborhood)
            if not self.model.grid.is_cell_empty(randomCell):
                if self.model.grid[randomCell][0].TYPE == 0:
                    self.model.grid.remove_agent(self.model.grid[randomCell][0])
                    break
            else:
                break

        self.model.grid.move_agent(self, randomCell)
        self.x = randomCell[0]
        self.y = randomCell[1]
