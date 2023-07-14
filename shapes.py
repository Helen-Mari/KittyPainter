class Shape:
    def __init__(self, x: list[float], y: list[float], color: str = "#000000"):
        self.x = x
        self.y = y
        self.color = color

    def paint(self, ax):
        ax.plot(self.x, self.y, c = self.color)