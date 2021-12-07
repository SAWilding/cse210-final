from game import constants
from game.actor import Actor
from game.point import Point
from random import randint

class Coin(Actor):
    def __init__(self):
        super().__init__()
        self._prepare()
        self._prepare_animation()

    def _prepare(self):
        self.set_name("Coin")
        self.set_height(constants.COIN_HEIGHT)
        self.set_width(constants.COIN_WIDTH)
        self.set_velocity(Point(constants.OBSTACLE_SPEED, 0))
        self.set_position(Point(constants.MAX_X, randint(10, constants.MAX_Y - constants.COIN_HEIGHT)))

    def _prepare_animation(self):
        self.set_animation(constants.IMAGE_COIN_ANIMATION)