from game import constants
from game.action import Action
from game.point import Point


class HandleScoreAction(Action):
    def __init__(self, cast, audio_service) -> None:
        super().__init__()
        self._cast = cast
        self._audio_service = audio_service

    def execute(self, cast):
        player_exists = False
        obstacle_exists = False
        for group in cast.values():
            for actor in group:
                if actor.get_name() == "Scoreboard":
                    scoreboard = actor
                if actor.get_name() == "Player":
                    player = actor
                    player_position = player.get_position()
                    player_x = player_position.get_x()
                    player_exists = True
                if actor.get_name() == "Obstacle":
                    obstacle_exists = True

        for obstacle in cast["obstacles"]:
            obstacle_position = obstacle.get_position()
            obstacle_x = obstacle_position.get_x()

            if player_exists and obstacle_exists:
                if player_x == obstacle_x:
                    scoreboard.add_points(1)
                    self._audio_service.play_sound(constants.SOUND_SCORE)

            
