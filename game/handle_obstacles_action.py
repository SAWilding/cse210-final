from random import randint
from game import constants
from game.action import Action
from game.obstacle import Obstacle
from game.coin import Coin

class HandleObstaclesAction(Action):
    def __init__(self, cast) -> None:
        super().__init__()
        self._cast = cast


    def execute(self, cast):
        for obstacle in cast["obstacles"]:
            obstacle_position = obstacle.get_position()
            obstacle_x = obstacle_position.get_x()

            if (obstacle_x == constants.MAX_X / 2):
                cast["obstacles"].append(Obstacle())
            elif (obstacle_x == constants.MAX_X / 4) and (randint(1, 4) == 1):
                cast["coin"].append(Coin())

            