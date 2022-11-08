from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter


from portrayal import portrayal
from model import Clean

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

TABLE_SIZE = 18

canvas_element = CanvasGrid(
    portrayal, TABLE_SIZE, TABLE_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT
)

model_params = {
    "robots": UserSettableParameter(
        "number", "Robots", value=1, min_value=1, max_value=8
    ),
    "trashRate": UserSettableParameter(
        "slider", "Trash %", value=0.5, min_value=0.1, max_value=1, step=0.01
    ),
    "size": TABLE_SIZE,
}

server = ModularServer(Clean, [canvas_element], "Cleaner Robots", model_params)

if __name__ == "__main__":
    server.launch()
