from game.action import Action
from game import constants
from game.point import Point

class ControlActorsAction(Action):
    def __init__(self, input_service) -> None:
        self._input_service = input_service

    def execute(self, cast):
        pass