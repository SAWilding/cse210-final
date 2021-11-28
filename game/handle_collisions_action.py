from game.action import Action
from game import constants
from game.point import Point

class HandleCollisionsAction(Action):
    def __init__(self, physics_service, audio_service, scoreboard) -> None:
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._scoreboard = scoreboard
    def execute(self, cast):
        pass
        

