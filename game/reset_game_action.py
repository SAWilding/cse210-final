from game import constants
from game.action import Action
from game.point import Point
from game.player import Player
from game.obstacle import Obstacle
from game.scoreboard import Scoreboard

class ResetGameAction(Action):
    def __init__(self, cast, input_service) -> None:
        super().__init__()
        self._input_service = input_service

    def execute(self, cast):
        should_restart = False

        if len(cast["player"]) == 0:
            should_restart = True
            for actor in cast["scoreboard"]:
                scoreboard = actor
            
            if self._input_service.is_space_pressed():
                cast["player"] = [Player()]
                cast["obstacles"] = [Obstacle()]
                cast["scoreboard"] = [Scoreboard()]
        if should_restart:
            scoreboard._text = f"Score: {scoreboard._score}\nPress \"space\" to restart"