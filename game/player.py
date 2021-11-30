from game.actor import Actor
from game.point import Point
from game import constants

class Player(Actor):
    def __init__(self):
        super().__init__()
        self._prepare()

    def _prepare(self):
        self.set_position(Point(constants.MAX_X / 8, constants.MAX_Y / 2))
        self.set_image(constants.IMAGE_PLAYER)
        self.set_height(constants.PLAYER_HEIGHT)
        self.set_width(constants.PLAYER_WIDTH)
        self.set_name("Player")
