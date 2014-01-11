

class GameScreen():
    """ Abstract definition of a game screen, capable of handling input events and
    rendering itself. """

    def __init__(self, size):
        self.size = size

    def render(self):
        pass
        #should return a surface

    def handle(self, event):
        pass

