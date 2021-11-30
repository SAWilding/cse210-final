from game.actor import Actor
from game import constants
from game.point import Point

class Scoreboard(Actor):
    def __init__(self):
        super().__init__()
        self._score = 0
        self._prepare()


    def _prepare(self):
        self.set_position(Point(0, constants.SCORE_HEIGHT))
        self.set_width(constants.SCORE_WIDTH)
        self.set_height(constants.SCORE_HEIGHT)
        self.set_text(f"Score: {self._score}")
        self.set_name("Scoreboard")

    def add_points(self, points):
        self._score += points
        self.set_text(f"Score: {self._score}")
