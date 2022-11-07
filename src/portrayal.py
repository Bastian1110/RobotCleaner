def portrayal(agent):
    if agent is None:
        return
    if agent.TYPE == 0:
       return {
           "Shape": "rect",
           "w": 1,
           "h": 1,
           "Filled": "true",
           "Layer": 0,
           "x": agent.x,
           "y": agent.y,
           "Color": "blue" if agent.isDirty else "white",
       }
    if agent.TYPE == 1:
        return {
            "Shape": "rect",
            "w": 1,
            "h": 1,
            "Filled": "true",
            "Layer": 0,
            "x": agent.x,
            "y": agent.y,
            "Color": "black",
        }