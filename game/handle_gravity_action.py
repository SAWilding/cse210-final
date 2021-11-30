from game import constants
from game.point import Point
from game.action import Action

class HandleGravityAction(Action):
    def __init__(self, cast) -> None:
        self._cast = cast

    def execute(self, cast):
        for actor in cast["player"]:
            player = actor
            velocity = player.get_velocity()
            velocity_y = velocity.get_y()
            if velocity_y < constants.MAX_GRAVITY_SPEED:
                velocity_y += constants.GRAVITY
                player.set_velocity(Point(0, velocity_y))
