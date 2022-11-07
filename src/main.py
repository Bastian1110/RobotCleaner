from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter


from portrayal import portrayal
from model import Clean

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

canvas_element = CanvasGrid(portrayal, 50, 50, CANVAS_WIDTH, CANVAS_HEIGHT)

server = ModularServer(Clean, [canvas_element], "Cleaner Robots")

if __name__ == "__main__":
    server.launch()