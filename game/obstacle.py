from game.actor import Actor
from game import constants
from game.point import Point
from random import randint

class Obstacle(Actor):
    def __init__(self):
        super().__init__()
        self._prepare()

    def _prepare(self):
        self.set_position(Point(constants.MAX_X, randint(0, constants.MAX_Y - constants.OBSTACLE_HEIGHT)))
        self.set_height(constants.OBSTACLE_HEIGHT)
        self.set_width(constants.OBSTACLE_WIDTH)
        self.set_velocity(Point(constants.OBSTACLE_SPEED, 0))
        self.set_name("Obstacle")
        self.set_image(constants.IMAGE_OBSTACLE)

        